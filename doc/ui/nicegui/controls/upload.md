# {func}`~nicegui.ui.upload` 文件上传

`File Upload` 基于 Quasar 的[QUploader组件](https://quasar.dev/vue-components/uploader)。

- `multiple`: 允许一次上传多个文件（默认：`False`）
- `max_file_size`: 文件的最大大小，以字节为单位（默认：`0`）
- `max_total_size`: 所有文件的最大总大小，以字节为单位（默认：`0`）
- `max_files`: 最大文件数量（默认：`0`）
- `on_upload`: 每个上传文件时执行的回调函数（类型：`nicegui.events.UploadEventArguments`）
- `on_rejected`: 每个被拒绝的文件执行的回调函数
- `label`: 上传器的标签（默认：`''`）
- `auto_upload`: 当文件被选择时自动上传（默认：`False`）

```python
from nicegui import ui

ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full')

# ui.run()
```

## {func}`~nicegui.ui.upload` 限制上传 

在这个示例中，上传被限制为最大文件大小1MB。当文件被拒绝时，会显示一个通知。

```python
from nicegui import ui

ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}'),
          on_rejected=lambda: ui.notify('Rejected!'),
          max_file_size=1_000_000).classes('max-w-full')

# ui.run()
```

## {func}`~nicegui.ui.upload` 显示内容

在这个示例中，上传的Markdown文件会在一个对话框中显示。

```python
from nicegui import events, ui

with ui.dialog().props('full-width') as dialog:
    with ui.card():
        content = ui.markdown()

def handle_upload(e: events.UploadEventArguments):
    text = e.content.read().decode('utf-8')
    content.set_content(text)
    dialog.open()

ui.upload(on_upload=handle_upload).props('accept=.md').classes('max-w-full')

# ui.run()
```
