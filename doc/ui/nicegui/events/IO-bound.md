# 运行 I/O 密集型任务

NiceGUI 提供了一个 `io_bound` 函数，用于在单独的线程中运行 I/O 密集型任务。对于那些长时间运行的 I/O 操作而言，这非常有用，否则这些操作会阻塞事件循环并使 UI 无响应。该函数返回一个可以被等待的 future。

```python
import requests
from nicegui import run, ui

async def handle_click():
    URL = 'https://httpbin.org/delay/1'
    response = await run.io_bound(requests.get, URL, timeout=3)
    ui.notify(f'Downloaded {len(response.content)} bytes')

ui.button('Download', on_click=handle_click)

# ui.run()
```
