# {func}`~nicegui.ui.dialog` 对话框

基于 Quasar 的 [QDialog 组件](https://quasar.dev/vue-components/dialog)创建一个对话框。默认情况下，通过点击或按 `ESC` 键可以关闭它。要使其保持打开状态，请在对话框元素上设置 `.props('persistent')`。

注意：对话框是一个元素。这意味着它关闭时不会被移除，而只是隐藏。您应该只创建一次然后重复使用它，或者在关闭后使用 `.clear()` 方法将其移除。

`value`：创建时应否打开对话框（默认：`False`）

```python
from nicegui import ui

with ui.dialog() as dialog, ui.card():
    ui.label('Hello world!')
    ui.button('Close', on_click=dialog.close)

ui.button('Open a dialog', on_click=dialog.open)

# ui.run()
```

## {func}`~nicegui.ui.dialog` 可等待的对话框

对话框可以被等待。使用 `submit` 方法关闭对话框并返回结果。通过在背景上点击或按 `ESC` 键取消对话框将返回 `None`。

```python
from nicegui import ui

with ui.dialog() as dialog, ui.card():
    ui.label('Are you sure?')
    with ui.row():
        ui.button('Yes', on_click=lambda: dialog.submit('Yes'))
        ui.button('No', on_click=lambda: dialog.submit('No'))

async def show():
    result = await dialog
    ui.notify(f'You chose {result}')

ui.button('Await a dialog', on_click=show)

# ui.run()
```

## {func}`~nicegui.ui.dialog` 替换内容

对话框的内容可以被更改。

```python
from nicegui import ui

def replace():
    dialog.clear()
    with dialog, ui.card().classes('w-64 h-64'):
        ui.label('New Content')
    dialog.open()

with ui.dialog() as dialog, ui.card():
    ui.label('Hello world!')

ui.button('Open', on_click=dialog.open)
ui.button('Replace', on_click=replace)

# ui.run()
```
