# {func}`~nicegui.ui.page`

这个装饰器用于将函数标记为页面构建器。每个访问给定路由的用户都将看到新实例的页面。这意味着它对用户是私有的，不会与他人共享（与在页面装饰器外部放置元素时所做的操作不同）。

- `path`: 新页面的路由（路径必须以'/'开头）
- `title`: 可选的页面标题
- `viewport`: 可选的视口元标签内容
- `favicon`: 可选的相对文件路径或绝对URL，指向 favicon（默认：`None`，将使用 NiceGUI 图标）
- `dark`: 是否使用 Quasar 的深色模式（默认为 `run` 命令的 `dark` 参数）
- `language`: 页面的语言（默认为 `run` 命令的语言参数）
- `response_timeout`: 装饰函数构建页面的最大时间（默认：3.0 秒）
- `reconnect_timeout`: 服务器等待浏览器重新连接的最大时间（默认：0.0 秒）
- `api_router`: 要使用的 APIRouter 实例，可以保留为 `None` 以使用默认值
- `kwargs`: 传递给 FastAPI 的 `@app.get` 方法的其他关键字参数

```python
from nicegui import ui

@ui.page('/other_page')
def other_page():
    ui.label('Welcome to the other side')

@ui.page('/dark_page', dark=True)
def dark_page():
    ui.label('Welcome to the dark side')

ui.link('Visit other page', other_page)
ui.link('Visit dark page', dark_page)

# ui.run()
```

## {func}`~nicegui.ui.page` 具有路径参数的页面

页面路由可以像 FastAPI 一样包含参数。如果进行了类型注解，它们将自动转换为布尔值、整数、浮点数和复数值。如果页面函数期望一个请求参数，请求对象将自动提供。客户端参数提供了对 `websocket` 连接、布局等的访问。

```python
from nicegui import ui

@ui.page('/repeat/{word}/{count}')
def page(word: str, count: int):
    ui.label(word * count)

ui.link('Say hi to Santa!', '/repeat/Ho! /3')

# ui.run()
```

## NiceGUI 等待客户端连接

要等待客户端连接，您可以将客户端参数添加到装饰的页面函数中，并等待 `client.connected()`。在该语句下方的所有代码都是在建立服务器与客户端之间的websocket连接后执行的。

例如，这允许您运行 JavaScript 命令；这只有在有客户端连接的情况下才可能（参见 [#112](https://github.com/zauberzeug/nicegui/issues/112)）。同时，当用户已经看到一些内容时，也可以进行异步操作。

```python
import asyncio
from nicegui import Client, ui

@ui.page('/wait_for_connection')
async def wait_for_connection(client: Client):
    ui.label('This text is displayed immediately.')
    await client.connected()
    await asyncio.sleep(2)
    ui.label('This text is displayed 2 seconds after the page has been fully loaded.')
    ui.label(f'The IP address {client.ip} was obtained from the websocket.')

ui.link('wait for connection', wait_for_connection)

# ui.run()
```

## NiceGUI 使用 `APIRouter` 模块化

您可以使用 NiceGUI 对 FastAPI 的 `APIRouter` 进行专门化，通过将页面和其他路由组合在一起来模块化您的代码。如果您想要为多个页面重用相同的前缀，这特别有用。路由器及其页面可以整齐地放在单独的模块（例如文件）中，并且只需导入并在主应用程序中包含该路由器即可。请参阅我们的模块化示例，了解多文件应用程序结构。

```python
from nicegui import APIRouter, app, ui

router = APIRouter(prefix='/sub-path')

@router.page('/')
def page():
    ui.label('This is content on /sub-path')

@router.page('/sub-sub-path')
def page():
    ui.label('This is content on /sub-path/sub-sub-path')

ui.link('Visit sub-path', '/sub-path')
ui.link('Visit sub-sub-path', '/sub-path/sub-sub-path')

app.include_router(router)

# ui.run()
```
