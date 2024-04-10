# NiceGUI 安装包

NiceGUI 应用也可以使用[PyInstaller](https://www.pyinstaller.org/)打包成一个可执行文件。这允许你将你的应用程序作为一个可以在任何计算机上执行的单个文件进行分发。

只需确保你的`ui.run`命令不使用`reload`参数。运行下面的`build.py`将在`dist`文件夹中创建一个可执行的`myapp`：

:::::{tab-set}

::::{tab-item} main.py
```python
from nicegui import native, ui

ui.label('Hello from PyInstaller')

ui.run(reload=False, port=native.find_open_port())
```
::::

::::{tab-item} build.py
```python
import os
import subprocess
from pathlib import Path
import nicegui

cmd = [
    'python',
    '-m', 'PyInstaller',
    'main.py', # your main file with ui.run()
    '--name', 'myapp', # name of your app
    '--onefile',
    #'--windowed', # prevent console appearing, only use with ui.run(native=True, ...)
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'
]
subprocess.call(cmd)
```
::::

:::::

打包技巧：

- 在构建PyInstaller应用程序时，你的主脚本可以通过使用ui.run(reload=False, native=True)来使用原生窗口（而不是浏览器窗口）。native参数可以是True或False，取决于你是希望有一个原生窗口还是在用户的浏览器中打开页面 - 两者在PyInstaller生成的应用程序中都可以工作。
- 向PyInstaller指定 `--windowed` 将防止终端控制台出现。然而，只有在你在 `ui.run` 命令中也指定了 `native=True` 时，你才应该使用这个选项。没有终端控制台，用户将无法通过按 Ctrl-C 来退出应用程序。有了native=True选项，当窗口关闭时，应用程序将自动关闭，如预期的那样。
- 向PyInstaller指定 `--windowed` 将在Mac上创建一个 `.app` 文件，这可能更方便分发。当你双击应用程序运行它时，它不会显示任何控制台输出。你还可以从命令行运行应用程序，使用 `./myapp.app/Contents/MacOS/myapp` 来查看控制台输出。
- 向PyInstaller指定 `--onefile` 将创建一个单独的可执行文件。虽然方便分发，但它启动起来会更慢。这不是 NiceGUI 的错，而是 Pyinstaller 将东西压缩成单个文件的方式，然后在运行前将一切解压缩到临时目录中。你可以通过从 PyInstaller 命令中移除 `--onefile` 来缓解这个问题，并自己压缩生成的dist目录，分发它，你的最终用户可以解压一次就可以直接使用，而不需要因为 `--onefile` 标志而不断地扩展文件。

不同选项的用户体验总结：

PyInstaller	`ui.run(...)`	解释
- `onefile	native=False`	在dist/中生成单个可执行文件，运行在浏览器中
- `onefile	native=True`	在dist/中生成单个可执行文件，运行在弹出窗口中
- `onefile and windowed	native=True`	在 `dist/` 中生成单个可执行文件（在Mac上生成包含图标的适当 `dist/myapp.app`），运行在弹出窗口中，不出现控制台
- `onefile and windowed	native=False`	避免（无法退出应用程序）
- 不指定		`A dist/myapp` 目录创建，可以手动压缩并分发；使用 `dist/myapp/myapp` 运行

如果你正在使用Python虚拟环境，请确保你在虚拟环境中安装pyinstaller，以便使用正确的PyInstaller，否则由于选择了错误的PyInstaller版本，你可能会得到损坏的应用程序。这就是为什么构建脚本使用 `python -m PyInstaller` 调用PyInstaller，而不仅仅是pyinstaller。

```bash
python -m venv venv
source venv/bin/activate
pip install nicegui
pip install pyinstaller
```

注意：如果你遇到了错误 "TypeError: a bytes-like object is required, not 'str'"，请尝试在 main.py 文件的顶部添加以下代码行：

```python
import sys
sys.stdout = open('logs.txt', 'w')
```

更多信息请参考 https://github.com/zauberzeug/nicegui/issues/681。

macOS 打包：

在你的主应用程序文件中的任何其他内容之前，添加以下代码段，以防止在新进程中无休止地生成新进程：

```python
# macOS 打包支持
from multiprocessing import freeze_support  # noqa
freeze_support()  # noqa

# 你的所有其他导入和代码
```

`# noqa` 注释指示 Pylance 或 autopep8 不要对这两行代码应用任何 PEP 规则，以确保它们始终位于其他内容的顶部。这是防止进程生成的关键。
