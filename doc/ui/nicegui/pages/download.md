# {func}`~nicegui.ui.download` 下载

用于触发文件、URL 或字节的下载的函数。

- `src`：目标URL、应下载的文件的本地路径或原始数据
- `filename`：要下载的文件的名称（默认：服务器上的文件名）
- `media_type`：要下载的文件的媒体类型（默认：`""`）

```python
from nicegui import ui

ui.button('Logo', on_click=lambda: ui.download('https://nicegui.io/logo.png'))

# ui.run()
```

## {func}`~nicegui.ui.download` 从内存中下载原始字节

下载函数也可用于从内存中下载原始字节。

```python
from nicegui import ui

ui.button('Download', on_click=lambda: ui.download(b'Hello World', 'hello.txt'))

# ui.run()
```
