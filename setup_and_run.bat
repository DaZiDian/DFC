@echo off
chcp 65001
setlocal

:: 检查Python是否在环境变量中
where python >nul 2>nul
if %errorlevel% == 0 (
    echo [DFC] Python环境变量已存在。
) else (
    echo [DFC] Python环境变量不存在。
    set /p python_path="[DFC] 请输入Python的完整路径（如C:\Python39），或输入 'install' 在线安装："
    if "%python_path%" == "install" (
        echo [DFC] 请访问 https://www.python.org/downloads/ 下载并安装适合的Python版本。
        exit /b
    ) else (
        setx PATH "%PATH%;%python_path%"
        echo [DFC] Python路径已添加至环境变量。
    )
)

:: 检查并安装 Tesseract
where tesseract >nul 2>nul
if %errorlevel% == 0 (
    echo [DFC] Tesseract环境变量已存在。
) else (
    echo [DFC] Tesseract环境变量不存在。请确保已安装Tesseract并将其路径添加至环境变量。
    set /p tesseract_path="[DFC] 请输入Tesseract的完整安装路径（如C:\Program Files\Tesseract-OCR），或输入 'install' 在线安装："
    if "%tesseract_path%" == "install" (
        echo [DFC] 请访问 https://github.com/UB-Mannheim/tesseract/wiki 下载并安装适合的Tesseract版本。
        exit /b
    ) else (
        setx PATH "%PATH%;%tesseract_path%"
        echo [DFC] Tesseract路径已添加至环境变量。
    )
)

:: 创建虚拟环境
echo [DFC] 创建虚拟环境...
if exist "env" (
    rmdir /s /q "env"
)
python -m venv env

:: 激活虚拟环境
call env\Scripts\activate.bat

:: 安装依赖包
echo [DFC] 安装依赖包...
pip install -r requirements.txt

:: 运行main.py
echo [DFC] 运行main.py...
python main.py

:: 退出虚拟环境
deactivate
endlocal
