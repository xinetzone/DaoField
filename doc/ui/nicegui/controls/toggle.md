# {func}`~nicegui.ui.toggle` 切换按钮

这个元素是基于Quasar的[QBtnToggle](https://quasar.dev/vue-components/button-toggle)组件。

选项可以指定为值的列表，或者作为映射值到标签的字典。在操作选项后，调用 `update()` 来更新UI中的选项。

- `options`：一个列表 `['value1', ...]` 或字典 `{'value1':'label1', ...}` 指定选项
- `value`：初始值
- `on_change`：选择改变时执行的回调函数
- `clearable`：是否可以通过点击所选项来清除切换按钮

```python
from nicegui import ui

toggle1 = ui.toggle([1, 2, 3], value=1)
toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(toggle1, 'value')

# ui.run()
```
