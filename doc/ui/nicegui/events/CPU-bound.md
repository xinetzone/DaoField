# {func}`~nicegui.run.cpu_bound` 运行 CPU 密集型任务

NiceGUI 提供了一个 `cpu_bound` 函数，用于在单独的进程中运行 CPU 密集型任务。对于那些长时间运行的计算而言，这非常有用，否则这些计算会阻塞事件循环并使 UI 无响应。该函数返回一个可以被等待的 `future`。

```python
import time
from nicegui import run, ui

def compute_sum(a: float, b: float) -> float:
    time.sleep(1)  # simulate a long-running computation
    return a + b

async def handle_click():
    result = await run.cpu_bound(compute_sum, 1, 2)
    ui.notify(f'Sum is {result}')

ui.button('Compute', on_click=handle_click)

# ui.run()
```
