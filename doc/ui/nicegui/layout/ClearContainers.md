# NiceGUI 清除容器

要从行、列或卡片容器中移除所有元素，可以调用

```python
container.clear()
```
或者，您可以通过以下方式移除单个元素：

```python
container.remove(element: Element)
container.remove(index: int)
element.delete()
```

```python
from nicegui import ui

container = ui.row()

def add_face():
    with container:
        ui.icon('face')
add_face()

ui.button('Add', on_click=add_face)
ui.button('Remove', on_click=lambda: container.remove(0) if list(container) else None)
ui.button('Clear', on_click=container.clear)

# ui.run()
```