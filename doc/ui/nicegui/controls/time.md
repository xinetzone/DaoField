# {func}`~nicegui.ui.time` 时间

`Time Input`元素是基于Quasar的[QTime组件](https://quasar.dev/vue-components/date)。时间是一个字符串，格式由 `mask` 参数定义。

- `value`: 初始时间
- `mask`: 时间字符串的格式（默认：`'HH:mm'`）
- `on_change`: 更改时间时执行的回调函数

```python
from nicegui import ui

ui.time(value='12:00', on_change=lambda e: result.set_text(e.value))
result = ui.label()

# ui.run()
```
