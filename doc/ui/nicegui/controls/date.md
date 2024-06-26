# {func}`~nicegui.ui.date` 日期

`Date Input` 元素是基于 Quasar的 [QDate组件](https://quasar.dev/vue-components/date)。日期是字符串，格式由 `mask` 参数定义。

你还可以使用 `range` 或 `multiple` 属性来选择日期范围或多个日期：

```python
ui.date({'from': '2023-01-01', 'to': '2023-01-05'}).props('range')
ui.date(['2023-01-01', '2023-01-02', '2023-01-03']).props('multiple')
ui.date([{'from': '2023-01-01', 'to': '2023-01-05'}, '2023-01-07']).props('multiple range')
```

- `value`: 初始日期
- `mask`: 日期字符串的格式（默认：`'YYYY-MM-DD'`）
- `on_change`: 更改日期时执行的回调函数


```python
from nicegui import ui

ui.date(value='2023-01-01', on_change=lambda e: result.set_text(e.value))
result = ui.label()

# ui.run()
```

## {func}`~nicegui.ui.date` + `~nicegui.ui.input`

这个示例展示了如何用输入元素实现一个日期选择器。我们在输入元素的追加插槽中放置了一个图标。当点击该图标时，我们打开一个带有日期选择器的菜单。

日期绑定到输入元素的值上。因此，无论何时更改日期，输入元素和日期选择器都会保持同步。

```python
from nicegui import ui

with ui.input('Date') as date:
    with date.add_slot('append'):
        ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
    with ui.menu() as menu:
        ui.date().bind_value(date)

# ui.run()
```

## {func}`~nicegui.ui.date` 日期过滤

这个示例展示了如何在日期选择器中过滤日期。为了将一个函数传递给日期选择器，我们使用`:options`属性。前面的冒号告诉NiceGUI该值是一个JavaScript表达式。

```python
from nicegui import ui

ui.date().props('''default-year-month=2023/01 :options="date => date <= '2023/01/15'"''')

# ui.run()
```
