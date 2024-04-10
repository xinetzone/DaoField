# NiceGUI 轮播图

这个元素代表了 Quasar 的 [QCarousel 组件](https://quasar.dev/vue-components/carousel#qcarousel-api)。它包含各个独立的轮播幻灯片。

- `value`：`ui.carousel_slide` 或最初选择的幻灯片的名称（默认：`None`，表示第一张幻灯片）
- `on_value_change`：当选定的幻灯片发生变化时要执行的回调函数
- `animated`：是否对幻灯片过渡进行动画处理（默认：`False`）
- `arrows`：是否显示用于手动滑动导航的箭头（默认：`False`）
- `navigation`：是否显示用于手动滑动导航的导航点（默认：`False`）

```python
from nicegui import ui

with ui.carousel(animated=True, arrows=True, navigation=True).props('height=180px'):
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/30/270/180').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/31/270/180').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/32/270/180').classes('w-[270px]')

# ui.run()
```
