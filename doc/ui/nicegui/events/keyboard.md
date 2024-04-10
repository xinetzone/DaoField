# NiceGUI 键盘

添加全局键盘事件跟踪。

- `on_key`：当键盘事件发生时执行的回调函数
- `active`：指示是否应执行回调函数的布尔标志（默认：`True`）
- `repeating`：指示是否应重复发送按住的键的布尔标志（默认：`True`）
- `ignore`：当这些元素类型之一获得焦点时忽略按键（默认：`['input', 'select', 'button', 'textarea']`）

```python
from nicegui import ui
from nicegui.events import KeyEventArguments

def handle_key(e: KeyEventArguments):
    if e.key == 'f' and not e.action.repeat:
        if e.action.keyup:
            ui.notify('f was just released')
        elif e.action.keydown:
            ui.notify('f was just pressed')
    if e.modifiers.shift and e.action.keydown:
        if e.key.arrow_left:
            ui.notify('going left')
        elif e.key.arrow_right:
            ui.notify('going right')
        elif e.key.arrow_up:
            ui.notify('going up')
        elif e.key.arrow_down:
            ui.notify('going down')

keyboard = ui.keyboard(on_key=handle_key)
ui.label('Key events can be caught globally by using the keyboard element.')
ui.checkbox('Track key events').bind_value_to(keyboard, 'active')

# ui.run()
```
