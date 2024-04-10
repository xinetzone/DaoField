# {func}`~nicegui.ui.input` 输入

这个元素是基于Quasar框架中的[QInput](https://quasar.dev/vue-components/input)组件。

`on_change` 事件在每次按键时被触发，并且值会相应地更新。如果你希望等到用户确认输入后再进行操作，你可以注册一个自定义的事件回调，例如 `ui.input(...).on('keydown.enter', ...)` 或者 `ui.input(...).on('blur', ...)`。

你可以使用`validation`参数来定义一个验证规则的字典，例如`{'Too long!': lambda value: len(value) < 3}`。第一个失败的规则的键将作为错误消息显示。或者，你可以传递一个返回可选错误消息的可调用对象。要禁用每次值更改时的自动验证，你可以使用`without_auto_validation`方法。

关于输入样式的说明：Quasar的`QInput`组件是围绕原生输入元素的包装器。这意味着你不能直接样式化输入，但你可以`input-class`和`input-style`属性来样式化原生输入元素。有关更多详细信息，请参阅[`QInput`文档](https://quasar.dev/vue-components/input)中的“Style”属性部分。

- `label`: 文本输入的显示标签
- `placeholder`: 如果没有输入值，显示的文本
- `value`: 文本输入的当前值
- `password`: 是否隐藏输入（默认：`False`）
- `password_toggle_button`: 是否显示一个按钮来切换密码可见性（默认：`False`）
- `on_change`: 当值改变时执行的回调函数
- `autocomplete`: 用于自动完成的字符串列表（可选）
- `validation`: 验证规则的字典或返回可选错误消息的可调用对象

```python
from nicegui import ui

ui.input(label='Text', placeholder='start typing',
         on_change=lambda e: result.set_text('you typed: ' + e.value),
         validation={'Input too long': lambda value: len(value) < 20})
result = ui.label()

# ui.run()
```

## {func}`~nicegui.ui.input` 自动完成

自动完成功能在你输入时提供建议，使得输入更简单、更快。参数`options`是一个字符串列表，包含了将会出现的可用选项。

```python
from nicegui import ui

options = ['AutoComplete', 'NiceGUI', 'Awesome']
ui.input(label='Text', placeholder='start typing', autocomplete=options)

# ui.run()
```

## {func}`~nicegui.ui.input` 文本 `clearable`

`clearable` 属性是 Quasar 框架中的一个特性，它为输入框添加了一个清除按钮，用于清空文本。

```python
from nicegui import ui

i = ui.input(value='some text').props('clearable')
ui.label().bind_text_from(i, 'value')

# ui.run()
```

## {func}`~nicegui.ui.input` 风格

Quasar提供了许多属性来[改变风格](https://quasar.dev/vue-components/input)。甚至可以通过`input-style`和`input-class`属性样式化底层的输入，并使用提供的插槽来添加自定义元素。
```python
from nicegui import ui

ui.input(placeholder='start typing').props('rounded outlined dense')
ui.input('styling', value='some text') \
    .props('input-style="color: blue" input-class="font-mono"')
with ui.input(value='custom clear button').classes('w-64') as i:
    ui.button(color='orange-8', on_click=lambda: i.set_value(None), icon='delete') \
        .props('flat dense').bind_visibility_from(i, 'value')

# ui.run()
```

## {func}`~nicegui.ui.input` 输入验证

可以通过两种方式来验证输入：

通过传递一个返回错误消息或 `None` 的可调用对象，或者
通过传递一个字典，该字典将错误消息映射到返回 `True`（错误）或 `False`（无错误）的可调用对象。

```python
from nicegui import ui

ui.input('Name', validation=lambda value: 'Too short' if len(value) < 5 else None)
ui.input('Name', validation={'Too short': lambda value: len(value) >= 5})

# ui.run()
```
