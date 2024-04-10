# NiceGUI 绑定属性

NiceGUI 能够直接将 UI 元素绑定到模型。可以对 UI 元素的 `text`、`value` 或 `visibility` 属性以及（嵌套的）类属性进行绑定。每个元素都提供了如 `bind_value` 和 `bind_visibility` 之类的方法来创建与相应属性的双向绑定。要定义单向绑定，请使用这些方法的 `_from` 和 `_to` 变体。只需将这些方法的参数设置为模型的属性即可创建绑定。值将在立即更新，并在其中一个值更改时更新。

```python
from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('visible', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=3).bind_value(demo, 'number')
    ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

# ui.run()
```

## NiceGUI 绑定到字典

在这里，我们将标签的文本绑定到一个字典。

```python
from nicegui import ui

data = {'name': 'Bob', 'age': 17}

ui.label().bind_text_from(data, 'name', backward=lambda n: f'Name: {n}')
ui.label().bind_text_from(data, 'age', backward=lambda a: f'Age: {a}')

ui.button('Turn 18', on_click=lambda: data.update(age=18))

# ui.run()
```

## NiceGUI 绑定到变量

在这里，我们将 `datepicker` 的值绑定到普通变量。因此，我们使用了包含所有全局变量的字典 `globals()`。这个示例基于[官方的 `datepicker` 示例](https://nicegui.io/documentation/date#input_element_with_date_picker)。

```python
from nicegui import ui

date = '2023-01-01'

with ui.input('Date').bind_value(globals(), 'date') as date_input:
    with ui.menu() as menu:
        ui.date(on_change=lambda: ui.notify(f'Date: {date}')).bind_value(date_input)
    with date_input.add_slot('append'):
        ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')

# ui.run()
```

## NiceGUI 绑定到存储

绑定也可以与 `app.storage` 一起使用。在这里，我们在访问之间存储 `textarea` 的值。同一个用户的所有标签页之间也会共享这个笔记。

```python
from nicegui import app, ui

@ui.page('/')
def index():
    ui.textarea('This note is kept between visits').classes('w-full').bind_value(app.storage.user, 'note')

# ui.run()
```
