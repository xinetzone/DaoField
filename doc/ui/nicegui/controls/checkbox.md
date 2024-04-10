# `ui.checkbox` 复选框

这个元素是基于 Quasar 的[QCheckbox](https://quasar.dev/vue-components/checkbox)组件。

- `text`：显示在复选框旁边的标签
- `value`：初始是否应勾选（默认为 `False`）
- `on_change`：值改变时执行的回调函数

```python
from nicegui import ui

checkbox = ui.checkbox('check me')
ui.label('Check!').bind_visibility_from(checkbox, 'value')

# ui.run()
```
