# {func}`~nicegui.ui.dark_mode` 深色模式

您可以使用此元素在页面上启用、禁用或切换深色模式。值 `None` 表示自动模式，将使用客户端的系统首选项。

请注意，此元素会覆盖 `ui.run` 函数和页面装饰器的 `dark` 参数。

- `value`：是否启用深色模式。如果为 `None`，则深色模式设置为自动。
- `on_change`：当值发生变化时调用的回调函数。

```python
from nicegui import ui

dark = ui.dark_mode()
ui.label('Switch mode:')
ui.button('Dark', on_click=dark.enable)
ui.button('Light', on_click=dark.disable)

# ui.run()
```

