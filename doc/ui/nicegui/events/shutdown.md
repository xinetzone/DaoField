# 关闭 NiceGUI

这将以编程方式停止服务器。仅在禁用自动重新加载时才可能。

```python
from nicegui import app, ui

ui.button('shutdown', on_click=app.shutdown)

# ui.run(reload=False)
```
