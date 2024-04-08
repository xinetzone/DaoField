# `ui.chat_message` 聊天消息

基于 [Quasar 的聊天消息](https://quasar.dev/vue-components/chat/)组件。

- `text`：消息正文（可以是多个消息部分的字符串列表）
- `name`：消息作者的名称
- `label`：仅渲染标签头/部分
- `stamp`：消息的时间戳
- `avatar`：头像的URL
- `sent`：将消息渲染为已发送的消息（即来自当前用户）（默认：`False`）
- `text_html`：将文本渲染为HTML（默认：`False`）

```python
from nicegui import ui

ui.chat_message('Hello NiceGUI!',
                name='Robot',
                stamp='now',
                avatar='https://robohash.org/ui')

# ui.run()
```

## `ui.chat_message` 发送 HTML 文本

使用 `text_html` 参数，您可以向聊天发送 HTML 文本。

```python
from nicegui import ui

ui.chat_message('Without <strong>HTML</strong>')
ui.chat_message('With <strong>HTML</strong>', text_html=True)

# ui.run()
```

## `ui.chat_message` 换行

您可以在聊天消息中使用换行符。

```python
from nicegui import ui

ui.chat_message('This is a\nlong line!')

# ui.run()
```

## `ui.chat_message` 多部分消息

您可以通过传递字符串列表来发送多个消息部分。

```python
from nicegui import ui

ui.chat_message(['Hi! 😀', 'How are you?']
                )

# ui.run()
```

## 带有子元素的 `ui.chat_message` 

您可以向聊天消息添加子元素。

```python
from nicegui import ui

with ui.chat_message():
    ui.label('Guess where I am!')
    ui.image('https://picsum.photos/id/249/640/360').classes('w-64')

# ui.run()
```
