# {func}`~nicegui.ui.switch` 开关

这个元素是基于Quasar的[QToggle](https://quasar.dev/vue-components/toggle)组件。

- `text`：显示在开关旁边的标签
- `value`：初始是否应勾选（默认为 `False`）
- `on_change`：值改变时执行的回调函数

```python
from nicegui import ui

switch = ui.switch('switch me')
ui.label('Switch!').bind_visibility_from(switch, 'value')

# ui.run()
```
