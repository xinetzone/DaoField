# {func}`~nicegui.ui.textarea` 文本区域

这个元素是基于Quasar的[QInput](https://quasar.dev/vue-components/input)组件。

你可以使用验证参数来定义一个验证规则的字典，例如：`{'Too long!': lambda value: len(value) < 3}`。第一个失败的规则的键将显示为错误消息。或者，你可以传递一个可调用的函数，该函数返回可选的错误消息。要禁用每次值更改时自动验证，你可以使用 `without_auto_validation` 方法。

- `label`：`textarea` 的显示名称
- `placeholder`：如果没有输入值，显示的文本
- `value`：字段的初始值
- `on_change`：当值发生变化时执行的回调函数
- `validation`：验证规则的字典或返回可选错误消息的可调用对象

```python
from nicegui import ui

ui.textarea(label='Text', placeholder='start typing',
            on_change=lambda e: result.set_text('you typed: ' + e.value))
result = ui.label()

# ui.run()
```

## {func}`~nicegui.ui.textarea` `clearable`

`clearable` 属性是 Quasar 框架中的一个特性，它为输入框添加了一个清除按钮，用于清空文本。

```python
from nicegui import ui

i = ui.textarea(value='some text').props('clearable')
ui.label().bind_text_from(i, 'value')

# ui.run()
```
