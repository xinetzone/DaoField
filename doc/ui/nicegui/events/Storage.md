
# NiceGUI 存储

NiceGUI 为应用程序内的数据持久性提供了一种简便的方法。它具有三种内置存储类型：

- `app.storage.user`：存储在服务器端，每个字典都与浏览器会话cookie中的唯一标识符相关联。对于每个用户都是唯一的，这种存储可以在他们所有的浏览器标签页中访问。`app.storage.browser['id']` 用于识别用户。
- `app.storage.general`：也存储在服务器端，这个字典提供了一个所有用户都可以访问的共享存储空间。
- `app.storage.browser`：与前两种类型不同，这个字典直接作为浏览器会话cookie存储，在同一用户的所有浏览器标签页之间共享。然而，由于 `app.storage.user` 在减少数据负载、增强安全性和提供更大的存储容量方面的优势，通常更倾向于使用它。默认情况下，NiceGUI 在 `app.storage.browser['id']` 中保存浏览器会话的唯一标识符。

用户存储和浏览器存储仅在页面构建器函数 [pages](../pages/index) 中可用，因为它们正在访问 FastAPI 的底层请求对象。此外，这两种类型需要在 `ui.run()` 中的 `storage_secret` 参数来加密浏览器会话 cookie。

```python
from nicegui import app, ui

@ui.page('/')
def index():
    app.storage.user['count'] = app.storage.user.get('count', 0) + 1
    with ui.row():
       ui.label('your own page visits:')
       ui.label().bind_text_from(app.storage.user, 'count')

# ui.run(storage_secret='private key to secure the browser session cookie')
```

## NiceGUI 统计页面访问次数

在这里，我们使用自动可用的浏览器存储的会话 ID 来计算唯一页面访问次数。

```python
from collections import Counter
from datetime import datetime
from nicegui import app, ui

counter = Counter()
start = datetime.now().strftime('%H:%M, %d %B %Y')

@ui.page('/')
def index():
    counter[app.storage.browser['id']] += 1
    ui.label(f'{len(counter)} unique views ({sum(counter.values())} overall) since {start}')

# ui.run(storage_secret='private key to secure the browser session cookie')
```

## NiceGUI 存储 UI 状态

存储也可以与[绑定](https://nicegui.io/documentation/bindings)结合使用。在这里，我们正在保存访问之间的文本区域值。同一用户的所有标签页之间也共享该便签。

```python
from nicegui import app, ui

@ui.page('/')
def index():
    ui.textarea('This note is kept between visits') \
        .classes('w-full').bind_value(app.storage.user, 'note')

# ui.run()
```
