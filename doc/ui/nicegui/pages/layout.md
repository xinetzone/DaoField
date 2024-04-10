# NiceGUI 页面布局

通过 `ui.header`、`ui.footer`、`ui.left_drawer` 和 `ui.right_drawer`，您可以向页面添加额外的布局元素。`fixed` 参数控制元素是滚动还是固定在屏幕上。`top_corner` 和 `bottom_corner` 参数指示抽屉是否应扩展到页面的顶部或底部。有关可能属性的更多信息，请参阅 <https://quasar.dev/layout/header-and-footer> 和 <https://quasar.dev/layout/drawer>。通过 `ui.page_sticky`，您可以将元素“粘”在屏幕上。有关更多信息，请参阅 <https://quasar.dev/layout/page-sticky>。

```python
from nicegui import ui

@ui.page('/page_layout')
def page_layout():
    ui.label('CONTENT')
    [ui.label(f'Line {i}') for i in range(100)]
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
        ui.label('HEADER')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
        ui.label('LEFT DRAWER')
    with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
        ui.label('RIGHT DRAWER')
    with ui.footer().style('background-color: #3874c8'):
        ui.label('FOOTER')

ui.link('show page with fancy layout', page_layout)

# ui.run()
```
