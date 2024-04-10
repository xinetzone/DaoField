# `ui.log` 日志视图

创建一个日志视图，允许添加新行而无需将整个历史记录重新发送给客户端。

`max_lines`: 在丢弃最旧的行之前的最大行数（默认：`None`）

```python
from datetime import datetime
from nicegui import ui

log = ui.log(max_lines=10).classes('w-full h-20')
ui.button('Log time', on_click=lambda: log.push(datetime.now().strftime('%X.%f')[:-5]))

# ui.run()
```

## `ui.log` 附加日志

你可以将 `ui.log` 元素附加到 Python 日志记录器对象上，这样日志消息就会被推送到日志元素中。

```python
import logging
from datetime import datetime
from nicegui import ui

logger = logging.getLogger()

class LogElementHandler(logging.Handler):
    """A logging handler that emits messages to a log element."""

    def __init__(self, element: ui.log, level: int = logging.NOTSET) -> None:
        self.element = element
        super().__init__(level)

    def emit(self, record: logging.LogRecord) -> None:
        try:
            msg = self.format(record)
            self.element.push(msg)
        except Exception:
            self.handleError(record)

log = ui.log(max_lines=10).classes('w-full')
logger.addHandler(LogElementHandler(log))
ui.button('Log time', on_click=lambda: logger.warning(datetime.now().strftime('%X.%f')[:-5]))

# ui.run()
```

