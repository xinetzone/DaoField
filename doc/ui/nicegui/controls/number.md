# {func}`~nicegui.ui.number` 数字输入

这个元素是基于 Quasar 框架中的 [QInput](https://quasar.dev/vue-components/input) 组件。

你可以使用 `validation` 参数来定义一个验证规则的字典，例如 `{'Too small!': lambda value: value < 3}`。第一个失败的规则的键将作为错误消息显示。或者，你可以传递一个返回可选错误消息的可调用对象。要禁用每次值更改时的自动验证，你可以使用 `without_auto_validation` 方法。

- `label`: 数字输入的显示名称
- `placeholder`: 如果没有输入值，显示的文本
- `value`: 字段的初始值
- `min`: 允许的最小值
- `max`: 允许的最大值
- `precision`: 允许的小数位数（默认：无限制，负数：小数点前的位数）
- `step`: 步进按钮的步进大小
- `prefix`: 在显示值前添加的前缀
- `suffix`: 在显示值后添加的后缀 
- `format`: 用于格式化显示值的字符串，如 `"%.2f"`
- `on_change`: 当值改变时执行的回调函数
- `validation`: 验证规则的字典或返回可选错误消息的可调用对象

```python
from nicegui import ui

ui.number(label='Number', value=3.1415927, format='%.2f',
          on_change=lambda e: result.set_text(f'you entered: {e.value}'))
result = ui.label()

# ui.run()
```

## {func}`~nicegui.ui.number` `clearable`

`clearable` 属性是 Quasar 框架中的一个特性，它为输入框添加了一个清除按钮，用于清空文本。

```python
from nicegui import ui

i = ui.number(value=42).props('clearable')
ui.label().bind_text_from(i, 'value')

# ui.run()
```

## {func}`~nicegui.ui.number` 小数点后位数

你可以使用 `precision` 参数来指定小数位数。负值表示小数点前的位数。当输入失去焦点、当像 `min`、`max` 或 `precision` 这样的清理参数发生变化，或者当手动调用 `sanitize()` 函数时，会进行四舍五入。

```python
from nicegui import ui

n = ui.number(value=3.14159265359, precision=5)
n.sanitize()

# ui.run()
```
