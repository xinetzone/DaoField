# NiceGUI 异步事件处理器

大多数元素也支持异步事件处理器。

注意：您还可以将 `functools.partial` 传递给 `on_click` 属性，以包装带参数的异步函数。

```python
import asyncio
from nicegui import ui

async def async_task():
    ui.notify('Asynchronous task started')
    await asyncio.sleep(5)
    ui.notify('Asynchronous task finished')

ui.button('start async task', on_click=async_task)

# ui.run()
```
