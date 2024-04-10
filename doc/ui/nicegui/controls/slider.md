# {func}`~nicegui.ui.slider` 滑块

这个元素是基于 Quasar 的 [QSlider](https://quasar.dev/vue-components/slider) 组件。

- `min`：滑块的下界
- `max`：滑块的上界
- `step`：步长
- `value`：设置滑块初始位置的值
- `on_change`：当用户释放滑块时调用的回调函数

```python
from nicegui import ui

slider = ui.slider(min=0, max=100, value=50)
ui.label().bind_text_from(slider, 'value')

# ui.run()
```

## {func}`~nicegui.ui.slider` 限制事件的触发频率，包括首尾事件选项

默认情况下，滑块的值改变事件被限制为0.05秒。这意味着如果你快速移动滑块，值只会每0.05秒更新一次。

默认情况下，"首部"和"尾部"事件都是激活的。这意味着第一个事件会立即触发，最后一个事件会在限制时间后触发。

这个示例展示了禁用这些选项中的任何一个是如何改变行为的。为了更清楚地看到效果，限制时间设置为1秒。第一个滑块显示默认行为，第二个只发送首部事件，第三个只发送尾部事件。

```python
from nicegui import ui

ui.label('default')
ui.slider(min=0, max=10, step=0.1, value=5).props('label-always') \
    .on('update:model-value', lambda e: ui.notify(e.args),
        throttle=1.0)

ui.label('leading events only')
ui.slider(min=0, max=10, step=0.1, value=5).props('label-always') \
    .on('update:model-value', lambda e: ui.notify(e.args),
        throttle=1.0, trailing_events=False)

ui.label('trailing events only')
ui.slider(min=0, max=10, step=0.1, value=5).props('label-always') \
    .on('update:model-value', lambda e: ui.notify(e.args),
        throttle=1.0, leading_events=False)

# ui.run()
```

## {func}`~nicegui.ui.slider` 禁用滑块

您可以使用 `disable()` 方法来禁用滑块。这将阻止用户移动滑块。滑块也会变成灰色。

```python
from nicegui import ui

slider = ui.slider(min=0, max=100, value=50)
ui.button('Disable slider', on_click=slider.disable)
ui.button('Enable slider', on_click=slider.enable)

# ui.run()
```
