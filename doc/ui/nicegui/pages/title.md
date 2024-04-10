# NiceGUI 页面标题

设置当前客户端的页面标题。

`title`：页面标题

```python
from nicegui import ui

ui.button('Change page title', on_click=lambda: ui.page_title('New Title'))

# ui.run()
```
