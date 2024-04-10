# NiceGUI 自动上下文

为了便于编写直观的 UI 描述，NiceGUI 会自动跟踪创建元素的上下文。这意味着没有显式的父参数。相反，父上下文是使用 `with` 语句定义的。它也会被传递给事件处理器和计时器。

在示例中，标签 "Card content" 被添加到卡片中。因为 `ui.button` 也被添加到卡片中，所以标签 `"Click!"` 也将在此上下文中创建。一秒后添加的标签 `"Tick!"` 也被添加到卡片中。

这种设计决策允许轻松创建模块化组件，这些组件在 UI 中移动后仍能正常工作。例如，您可以将标签和按钮移动到其他地方，也许将它们包装在另一个容器中，代码仍然可以正常工作。

```python
from nicegui import ui

with ui.card():
    ui.label('Card content')
    ui.button('Add label', on_click=lambda: ui.label('Click!'))
    ui.timer(1.0, lambda: ui.label('Tick!'), once=True)

# ui.run()
```
