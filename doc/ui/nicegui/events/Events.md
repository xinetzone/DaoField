# NiceGUI 事件

您可以注册协程或函数，以便在以下事件发生时被调用：

- `app.on_startup`：在 NiceGUI 启动或重启时调用
- `app.on_shutdown`：在 NiceGUI 关闭或重启时调用
- `app.on_connect`：每个连接的客户端都会调用（可选参数：`nicegui.Client`）
- `app.on_disconnect`：每个断开连接的客户端都会调用（可选参数：`nicegui.Client`）
- `app.on_exception`：发生异常时调用（可选参数：`exception`）

当 NiceGUI 关闭或重启时，所有仍在执行的任务将自动取消。

```python
from datetime import datetime
from nicegui import app, ui

dt = datetime.now()

def handle_connection():
    global dt
    dt = datetime.now()
app.on_connect(handle_connection)

label = ui.label()
ui.timer(1, lambda: label.set_text(f'Last new connection: {dt:%H:%M:%S}'))

# ui.run()
```
