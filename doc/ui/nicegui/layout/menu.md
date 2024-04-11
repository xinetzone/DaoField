# {func}`~nicegui.ui.menu_item` 菜单

基于 Quasar 的 [QMenu 组件](https://quasar.dev/vue-components/menu)创建一个菜单。菜单应该放置在它应该显示的元素内。

`value`：菜单是否已经打开（默认：`False`）

```python
from nicegui import ui

with ui.row().classes('w-full items-center'):
    result = ui.label().classes('mr-auto')
    with ui.button(icon='menu'):
        with ui.menu() as menu:
            ui.menu_item('Menu item 1', lambda: result.set_text('Selected item 1'))
            ui.menu_item('Menu item 2', lambda: result.set_text('Selected item 2'))
            ui.menu_item('Menu item 3 (keep open)',
                         lambda: result.set_text('Selected item 3'), auto_close=False)
            ui.separator()
            ui.menu_item('Close', on_click=menu.close)

# ui.run()
```

## {func}`~nicegui.ui.menu_item` 上下文菜单

基于 Quasar 的 [QMenu 组件](https://quasar.dev/vue-components/menu)创建一个上下文菜单。上下文菜单应放置在它应该显示的元素内。当用户右键单击元素时，它会自动打开，并出现在鼠标位置。

```python
from nicegui import ui

with ui.image('https://picsum.photos/id/377/640/360'):
    with ui.context_menu():
        ui.menu_item('Flip horizontally')
        ui.menu_item('Flip vertically')
        ui.separator()
        ui.menu_item('Reset')

# ui.run()
```
