# NiceGUI 添加静态文件目录

`add_static_files()` 使本地目录在指定的端点（例如 `'/static'`）可用。这对于向前端提供本地数据（如图像）非常有用。否则，浏览器将无法访问这些文件。请确保只放置非安全关键文件，因为它们可以被任何人访问。

要使单个文件可访问，您可以使用 `add_static_file()`。对于应该流式传输的媒体文件，可以使用 `add_media_files()` 或 a`dd_media_file()`。

- `url_path`：以斜杠 `"/"` 开头的字符串，标识应提供服务的文件路径
- `local_directory`：包含作为静态内容提供服务的本地文件夹
- `follow_symlin`k：是否遵循符号链接（默认：`False`）

```python
from nicegui import app, ui

app.add_static_files('/examples', 'examples')
ui.label('Some NiceGUI Examples').classes('text-h5')
ui.link('AI interface', '/examples/ai_interface/main.py')
ui.link('Custom FastAPI app', '/examples/fastapi/main.py')
ui.link('Authentication', '/examples/authentication/main.py')

ui.run()
```