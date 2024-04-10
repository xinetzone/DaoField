# {func}`~nicegui.ui.joystick` 操纵杆

基于[nipple.js](https://yoannmoi.net/nipplejs/)创建操纵杆。

- `on_start`: 当用户触摸操纵杆时的回调
- `on_move`: 当用户移动操纵杆时的回调
- `on_end`: 用户释放操纵杆时的回调
- `throttle`: 移动事件的 Throttle `interval` (以秒为单位)(默认值: `0.05`)
- `options`: 像 `color` 这样的参数应该传递给底层的 [`nipple.js` 库](https://github.com/yoannmoinet/nipplejs#options)

```python
from nicegui import ui

ui.joystick(color='blue', size=50,
            on_move=lambda e: coordinates.set_text(f"{e.x:.3f}, {e.y:.3f}"),
            on_end=lambda _: coordinates.set_text('0, 0'))
coordinates = ui.label('0, 0')

# ui.run()
```
