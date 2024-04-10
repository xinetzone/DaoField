# NiceGUI 自动索引页面

使用 `@ui.page` 装饰器创建的页面是“私有”的。它们的内容会为每个客户端重新创建。因此，当浏览器重新加载页面时，私人页面上显示的 ID 会发生变化。

未包裹在装饰过的页面函数中的UI元素被放置在根路由"/"处的自动生成的索引页面上。这个自动索引页面在启动时创建一次，并被所有可能连接的客户端共享。因此，每个连接的客户端将看到相同的元素。在右侧的演示中，当浏览器重新加载页面时，自动索引页面上显示的 ID 保持不变。

```python
from nicegui import ui
from uuid import uuid4

@ui.page('/private_page')
async def private_page():
    ui.label(f'private page with ID {uuid4()}')

ui.label(f'shared auto-index page with ID {uuid4()}')
ui.link('private page', private_page)

# ui.run()
```
