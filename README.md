# DFC

## Document Format Converter

这是一个可以将某一种办公文档的格式转换为其他格式的文档的工具，使用[Tesseract](https://github.com/UB-Mannheim/tesseract)作为OCR识别工具，提高识别准确率，尽量做到完美转换。

在开始前，请您安装最新版的[Tesseract](https://github.com/UB-Mannheim/tesseract)，然后运行本项目中的自动运行批处理脚本 `setup_and_run.bat`。

如果脚本不可用，您可以尝试手动部署。

1. 安装Python 3 (版本 >= 3.9)，将其添加至环境变量中。
2. 使用Git clone本项目，或者直接在Releases中下载项目最新版压缩包。
3. 解压项目，进入项目根目录，使用 pip3 install 安装依赖：

   ```bash
   pip3 install -r requirements.txt

4. 之后，使用以下命令来运行脚本：

   ```bash
   python main.py
   ```

5. 如果此项目出现任何问题，请您提交issues，或者发送反馈邮件至 sdsfttt1@outlook.com。

邮件格式：

标题：【Feedback】[您发现的问题或建议]

内容：[问题正文内容] + [您的联系方式]

---

### 自定义设置

在运行转换时，您可以自定义以下设置以优化图像处理和OCR识别：

- **图像处理参数**：在代码中，您可以调整以下参数以优化图像质量：
  - **对比度增强**：可以通过更改 `enhancer.enhance(2.0)` 中的值来提高或降低对比度。
  - **去噪声设置**：您可以更改 `ImageFilter.MedianFilter(size=3)` 中的 `size` 参数，以调整去噪声的强度。

- **OCR语言选择**：在识别图像文本时，您可以选择语言类型。以下是可用语言示例：
  - 英文：`lang='eng'`
  - 中文：`lang='chi_sim'`
  - 日语：`lang='jpn'`
  - 俄语：`lang='rus'`

请确保在调用 `pytesseract.image_to_string()` 方法时指定适当的语言参数。例如：

```python
ocr_text = pytesseract.image_to_string(image, lang='chi_sim')  # 对于简体中文
```

---

This is a tool for converting one type of office document format to another, using [Tesseract](https://github.com/UB-Mannheim/tesseract) as the OCR recognition tool to improve accuracy and strive for perfect conversion.

Before you begin, please install the latest version of [Tesseract](https://github.com/UB-Mannheim/tesseract), and then run the automated batch script `setup_and_run.bat` in this project.

If the script is not available, you can try manual deployment.

1. Install Python 3 (version >= 3.9) and add it to the environment variables.
2. Clone this project using Git or download the latest release from the Releases section.
3. Extract the project, navigate to the project root directory, and install the dependencies using pip:

   ```bash
   pip3 install -r requirements.txt
   ```

4. After that, run the script using:

   ```bash
   python main.py
   ```

5. If you encounter any issues with this project, please submit an issue or send feedback via email to sdsfttt1@outlook.com.

Email format:

Subject: 【Feedback】[The issue or suggestion you discovered]

Content: [The detailed content of the issue] + [Your contact information]

### Custom Settings

When running the conversion, you can customize the following settings to optimize image processing and OCR recognition:

- **Image Processing Parameters**: In the code, you can adjust the following parameters to improve image quality:
  - **Contrast Enhancement**: You can change the value in `enhancer.enhance(2.0)` to increase or decrease contrast.
  - **Denoising Settings**: You can adjust the `size` parameter in `ImageFilter.MedianFilter(size=3)` to modify the strength of denoising.

- **OCR Language Selection**: When recognizing text in images, you can choose the type of language. Here are examples of available languages:
  - English: `lang='eng'`
  - Chinese: `lang='chi_sim'`
  - Japanese: `lang='jpn'`
  - Russian: `lang='rus'`

Make sure to specify the appropriate language parameter when calling `pytesseract.image_to_string()`. For example:

```python
ocr_text = pytesseract.image_to_string(image, lang='chi_sim')  # For Simplified Chinese
```
