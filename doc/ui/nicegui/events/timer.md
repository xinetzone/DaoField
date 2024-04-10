# NiceGUI 计时器

创建 NiceGUI 的主要动力之一是需要一个简单方法来定期更新界面，例如显示带有传入测量值的图表。计时器将使用给定的时间间隔重复执行回调函数。

- `interval`：调用计时器的间隔（可以在运行时更改）
- `callback`：当时间间隔过去时要执行的函数或协程
- `active`：是否应执行回调函数（可以在运行时更改）
- `once`：是否仅在间隔指定的延迟后执行一次回调（默认：`False`）

```python
from datetime import datetime
from nicegui import ui

label = ui.label()
ui.timer(1.0, lambda: label.set_text(f'{datetime.now():%X}'))

# ui.run()
```

## 激活、停用和取消 NiceGUI 计时器

您可以使用 `active` 属性来激活和停用计时器。您可以使用 `cancel` 方法来取消计时器。取消计时器后，它将无法再次激活。

```python
from nicegui import ui

slider = ui.slider(min=0, max=1, value=0.5)
timer = ui.timer(0.1, lambda: slider.set_value((slider.value + 0.01) % 1.0))
ui.switch('active').bind_value_to(timer, 'active')
ui.button('Cancel', on_click=timer.cancel)

# ui.run()
```

## NiceGUI 在延迟后调用函数

您可以使用带有 `once` 参数的计时器在延迟后调用函数。

```python
from nicegui import ui

def handle_click():
    ui.timer(1.0, lambda: ui.notify('Hi!'), once=True)
ui.button('Notify after 1 second', on_click=handle_click)

# ui.run()
```
