# NiceGUI 添加媒体文件目录

`add_media_files()` 允许从指定的端点（例如 `'/media'`）流式传输本地文件。这应用于支持适当流式传输的媒体文件。否则，浏览器将无法访问和增量加载文件，或者在流中跳转到不同位置。请确保只放置非安全关键文件，因为它们可以被任何人访问。

要使单个文件可通过流式传输访问，您可以使用 `add_media_file()`。对于小型静态文件，可以使用 `add_static_files()` 或 `add_static_file()`。

- `url_path`：以斜杠 `"/"` 开头的字符串，标识应提供服务的文件路径
- `local_directory`：包含作为媒体内容提供服务的本地文件夹

```python
import requests
from nicegui import app, ui
from pathlib import Path

media = Path('media')
media.mkdir(exist_ok=True)
r = requests.get('https://cdn.coverr.co/videos/coverr-cloudy-sky-2765/1080p.mp4')
(media  / 'clouds.mp4').write_bytes(r.content)
app.add_media_files('/my_videos', media)
ui.video('/my_videos/clouds.mp4')

# ui.run()
```
