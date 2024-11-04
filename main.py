import os
import fitz  # PyMuPDF
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from tqdm import tqdm  # 导入 tqdm


def preprocess_image(image):
    """对图像进行预处理，以提高OCR识别率"""
    # 转换为灰度图像
    image = image.convert("L")
    # 去噪声
    image = image.filter(ImageFilter.MedianFilter(size=3))
    # 二值化
    threshold = 128
    image = image.point(lambda p: p > threshold and 255)
    # 增加对比度
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    return image


def pdf_to_md(pdf_path, md_path, tesseract_path=None, ocr_enabled=False):
    """将PDF文件转换为Markdown格式，使用OCR识别图像中的文本"""
    # 获取Markdown文件的目录
    md_directory = os.path.dirname(md_path)

    # 如果目录不存在，则创建
    if not os.path.exists(md_directory):
        os.makedirs(md_directory)

    text = ""
    image_counter = 0  # 图像计数器，用于生成唯一的图像文件名

    # 设置Tesseract路径
    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    # 打开PDF文档
    doc = fitz.open(pdf_path)

    # 使用 tqdm 显示处理进度
    for page in tqdm(doc, desc="[DFC] Processing Pages", unit="page"):
        # 提取页面文本
        page_text = page.get_text()  # 直接提取原文内容
        text += page_text + "\n\n"

        # 提取图像
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_filename = os.path.join(md_directory, f"image_{image_counter}.png")
            try:
                with open(image_filename, "wb") as img_file:
                    img_file.write(image_bytes)
                text += f"![Image]({os.path.basename(image_filename)})\n\n"  # 添加图像到Markdown文本
                image_counter += 1

                # 使用OCR识别图像中的文本（如果用户选择了OCR）
                if ocr_enabled:
                    image = Image.open(image_filename)
                    image = preprocess_image(image)  # 预处理图像
                    # 指定简体中文识别
                    ocr_text = pytesseract.image_to_string(image, lang='chi_sim')
                    if ocr_text.strip():
                        text += ocr_text + "\n\n"
            except Exception as e:
                print(f"[DFC] 处理图像时出错: {e}")

    # 将最终文本保存为Markdown文件
    with open(md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(text)


def main():
    pdf_path = input("[DFC] 请输入PDF文件路径：")
    md_path = input("[DFC] 请输入输出Markdown文件路径（包括文件名）：")

    if not os.path.exists(pdf_path):
        print("[DFC] 文件路径无效，请检查后重试。")
        return

    tesseract_path = input(
        "[DFC] 请输入Tesseract的完整路径（如C:\\Program Files\\Tesseract-OCR\\tesseract.exe），如果已添加至PATH可直接按回车：")
    if not tesseract_path:
        tesseract_path = None  # 如果用户按回车，则不设置Tesseract路径

    ocr_choice = input("[DFC] 是否将图片内容转换为文本？(Y/N)：").strip().lower()
    ocr_enabled = (ocr_choice == 'y')

    pdf_to_md(pdf_path, md_path, tesseract_path, ocr_enabled)
    print("[DFC] PDF转换为Markdown完成！")


if __name__ == "__main__":
    main()
