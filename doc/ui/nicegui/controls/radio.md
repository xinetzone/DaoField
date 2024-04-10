# {func}`~nicegui.ui.radio` 单选按钮

这个元素是基于Quasar的[QRadio](https://quasar.dev/vue-components/radio)组件。

选项可以指定为值的列表，或者作为映射值到标签的字典。在操作选项后，调用 `update()` 来更新UI中的选项。

- `options`：一个列表 `['value1', ...]` 或字典 `{'value1':'label1', ...}` 指定选项
- `value`：初始值
- `on_change`：选择改变时执行的回调函数

```python
from nicegui import ui

radio1 = ui.radio([1, 2, 3], value=1).props('inline')
radio2 = ui.radio({1: 'A', 2: 'B', 3: 'C'}).props('inline').bind_value(radio1, 'value')

# ui.run()
```
