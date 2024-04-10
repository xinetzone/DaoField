# {func}`~nicegui.ui.run`

`ui.run()` 是 NiceGUI 的一个函数，它用于启动用户界面。这个函数可以接受一些可选参数来自定义应用的行为。下面是一些常用的参数：

- `host`: 指定启动服务器的主机地址。默认值是 `'127.0.0.1'`（在原生模式下），或者 `'0.0.0.0'`（在其他模式下）。

- `port`: 指定使用哪个端口。默认值是 `8080`（在正常模式下），或者一个自动确定的开放端口（在原生模式下）。

- `title`: 页面标题。默认值是 `'NiceGUI'`，但是可以在每个页面上重写。

- `viewport`: 页面元数据视口内容。默认值是 `'width=device-width, initial-scale=1'`，但是可以在每个页面上重写。

- `favicon`: 相对文件路径，绝对URL到一个 favicon，或者 emoji（例如 `'&#128640;'`，适用于大多数浏览器）。默认值是 `None`，将使用 NiceGUI 图标。

- `dark`: 是否使用 Quasar 的暗色模式。默认值是 `False`。如果设置为 `None`，则使用“自动”模式。

- `language`: Quasar 元素的语言。默认值是 `'en-US'`。

- `binding_refresh_interval`: 绑定更新之间的时间间隔。默认值是 `0.1` 秒。更大的值对 CPU 更友好。

- `reconnect_timeout`: 服务器等待浏览器重新连接的最大时间。默认值是 `3.0` 秒。

- `show`: 是否自动在浏览器标签页中打开用户界面。默认值是 `True`。

- `on_air`: 技术预览：如果设置为 `True`，允许临时远程访问。默认值是禁用的。

- `native`: 是否在大小为 800x600 的原生窗口中打开用户界面。默认值是 `False`。如果设置为 `True`，将停用 `show` 选项，并自动找到一个开放的端口。

- `window_size`: 以提供的尺寸在一个原生窗口中打开用户界面。例如 (1024, 786)。默认值是 `None`，也会激活 `native` 选项。

- `fullscreen`: 是否在全屏窗口中打开用户界面。默认值是 `False`。如果设置为 `True`，也会激活 `native` 选项。

- `frameless`: 是否在无边框窗口中打开用户界面。默认值是 `False`。如果设置为 `True`，也会激活 `native` 选项。

- `reload`: 是否在文件更改时自动重新加载用户界面。默认值是 `True`。

- `uvicorn_logging_level`: `uvicorn` 服务器的日志记录级别。默认值是 `'warning'`。

- `uvicorn_reload_dirs`: 以逗号分隔的列表字符串，用于监视的目录。默认值是当前工作目录。

- `uvicorn_reload_includes`: 以逗号分隔的列表字符串，用于修改时触发重新加载的 `glob` 模式。默认值是 `'*.py'`。

- `uvicorn_reload_excludes`: 以逗号分隔的列表字符串，应该忽略重新加载的 `glob` 模式。默认值是` '.*, .py[cod], .sw.*, ~*'`。

- `tailwind`: 是否使用 Tailwind。这是一个实验性的选项，默认值是 `True`。

- `prod_js`: 是否使用 Vue 和 Quasar 依赖的生产版本。默认值是 `True`。

- `endpoint_documentation`: 控制哪些端点出现在自动生成的 OpenAPI 文档中。默认值是 `'none'`，选项有 `'none'`, `'internal'`, `'page'`, `'all'`。

- `storage_secret`: 基于浏览器的存储的秘密密钥。默认值是 `None`，启用 `ui.storage.individual` 和 `ui.storage.browser` 需要一个值。

- `show_welcome_message`: 是否显示欢迎消息。默认值是 `True`。

- `kwargs`: 其他关键字参数将传递给 `uvicorn.run`。

```python
from nicegui import ui

ui.label('page with custom title')

# ui.run(title='My App')
```

## {func}`~nicegui.ui.run` Emoji favicon

你可以使用表情符号作为网页图标（favicon）。在Chrome、Firefox和Safari浏览器中都可以实现。

```python
from nicegui import ui

ui.label('NiceGUI rocks!')

# ui.run(favicon='🚀')
```

## {func}`~nicegui.ui.run` Base64 favicon

可以使用 base64 编码的图片作为图标。

```python
from nicegui import ui

ui.label('NiceGUI with a red dot!')

icon = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=='

# ui.run(favicon=icon)
```

## {func}`~nicegui.ui.run` SVG favicon

你可以使用 SVG 作为网页图标（favicon）。在Chrome、Firefox和Safari浏览器中都可以实现。

```python
from nicegui import ui

ui.label('NiceGUI makes you smile!')

smiley = '''
    <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <circle cx="100" cy="100" r="78" fill="#ffde34" stroke="black" stroke-width="3" />
        <circle cx="80" cy="85" r="8" />
        <circle cx="120" cy="85" r="8" />
        <path d="m60,120 C75,150 125,150 140,120" style="fill:none; stroke:black; stroke-width:8; stroke-linecap:round" />
    </svg>
'''

# ui.run(favicon=smiley)
```

## {func}`~nicegui.ui.run` 自定义欢迎消息

你可以通过在命令行中将 `show_welcome_message` 设置为 `False` 来关闭默认的欢迎消息。相反，你可以使用自定义启动处理程序打印自己的欢迎消息。

```python
from nicegui import app, ui

ui.label('App with custom welcome message')

app.on_startup(lambda: print('Visit your app on one of these URLs:', app.urls))

# ui.run(show_welcome_message=False)
```
