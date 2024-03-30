from pathlib import Path
from nicegui import ui

ROOT = Path(__file__).parent

header = """
通过按钮、对话框、3D场景、图表等与 Python 进行交互。

[NiceGUI](https://nicegui.io) 处理了 Web 开发的细节，让你专注于编写各种应用的 Python 代码，包括机器人技术、物联网解决方案、智能家居自动化和机器学习。NiceGUI 专为与连接的外部设备（如网络摄像头和 IoT 设置中的 GPIO 引脚）顺畅工作而设计，简化了在一个地方管理所有代码的过程。

NiceGUI 学习曲线平缓，对初学者友好，并为有经验的用户提供高级定制功能，确保基本任务的简单性和复杂项目的可行性。

NiceGUI 是开源的 Python 库，用于编写在浏览器中运行的图形用户界面。它具有非常平缓的学习曲线，同时仍提供高级定制选项。NiceGUI 遵循后端优先的理念：它处理所有 web 开发细节。您可以专注于编写 Python 代码。这使得它非常适合各种项目，包括短脚本、仪表板、机器人项目、物联网解决方案、智能家居自动化和机器学习。
"""

def callback():
    ui.markdown(f"# NiceGUI 简介")
    with ui.card():
        ui.markdown(header)
    with open(f"{ROOT}/intro.md", encoding="utf-8") as fp:
        content = fp.read()
    ui.markdown(content)
