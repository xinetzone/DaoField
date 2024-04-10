# NiceGUI 原生模式

你可以通过在 `ui.run` 函数中指定 `native=True` 来为 NiceGUI 启用原生模式。要自定义初始窗口大小和显示模式，分别使用 `window_size` 和 `fullscreen` 参数。此外，你还可以通过 `app.native.window_args` 和 `app.native.start_args` 提供额外的关键字参数。选择任何由内部使用的 `pywebview` 模块定义的 `webview.create_window` 和 `webview.start` 函数的参数。请注意，这些关键字参数将优先于 `ui.run` 中定义的参数。

在原生模式下，`app.native.main_window` 对象允许你访问底层窗口。它是 [`pywebview`](https://pywebview.flowrl.com/guide/api.html) 中的 Window 的异步版本。

```python
from nicegui import app, ui

app.native.window_args['resizable'] = False
app.native.start_args['debug'] = True

ui.label('app running in native mode')
ui.button('enlarge', on_click=lambda: app.native.main_window.resize(1000, 700))

# ui.run(native=True, window_size=(400, 300), fullscreen=False)
```

如果 `webview` 在寻找所需库时遇到问题，你可能会收到与 `"WebView2Loader.dll"` 相关的错误。要解决此问题，请尝试将 DLL 文件向上移动一个目录，例如：

从 `.venv/Lib/site-packages/webview/lib/x64/WebView2Loader.dll` 移动到 `.venv/Lib/site-packages/webview/lib/WebView2Loader.dll`
