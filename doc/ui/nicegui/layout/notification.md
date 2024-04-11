# {func}`nicegui.ui.notify` 通知

## {func}`nicegui.ui.notify` 在屏幕上显示通知。

- `message`：通知内容
- `position`：屏幕上的位置（`"top-left"`、`"top-right"`、`"bottom-left"`、`"bottom-right"`、`"top"`、`"bottom"`、`"left"`、`"right"` 或 - - `"center"`，默认为 `"bottom"`）
- `close_button`：可选的按钮标签，用于关闭通知（默认：`False`）
- `type`：可选类型（`"positive"`、`"negative"`、`"warning"`、`"info"` 或 `"ongoing"`）
- `color`：可选的颜色名称
- `multi_line`：启用多行通知

注意：您可以根据 Quasar 的 [Notify API](https://quasar.dev/quasar-plugins/notify#notify-api) 传递其他关键字参数。

```python
from nicegui import ui

ui.button('Say hi!', on_click=lambda: ui.notify('Hi!', close_button='OK'))

# ui.run()
```

## {func}`nicegui.ui.notify` 通知类型

可以使用不同的类型来指示通知的性质。

```python
from nicegui import ui

ui.button('negative', on_click=lambda: ui.notify('error', type='negative'))
ui.button('positive', on_click=lambda: ui.notify('success', type='positive'))
ui.button('warning', on_click=lambda: ui.notify('warning', type='warning'))

# ui.run()
```

## {func}`nicegui.ui.notify` 多行通知

要允许通知文本跨越多行，只需设置 `multi_line=True`。如果需要手动换行符（如 `\n`），您需要定义一个 CSS 样式，并像示例中所示将其传递给通知。

```python
from nicegui import ui

ui.html('<style>.multi-line-notification { white-space: pre-line; }</style>')
ui.button('show', on_click=lambda: ui.notify(
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit. \n'
    'Hic quisquam non ad sit assumenda consequuntur esse inventore officia. \n'
    'Corrupti reiciendis impedit vel, '
    'fugit odit quisquam quae porro exercitationem eveniet quasi.',
    multi_line=True,
    classes='multi-line-notification',
))

# ui.run()
```

## {func}`nicegui.ui.notify` 通知元素

在屏幕上显示一个通知。与 `ui.notify` 不同，此元素允许在通知显示后更新通知消息和其他属性。可以使用 `dismiss()` 方法移除通知。

- `message`：通知内容
- `position`：屏幕上的位置（`"top-left"`、`"top-right"`、`"bottom-left"`、`"bottom-right"`、`"top"`、`"bottom"`、`"left"`、`"right"` 或 - - `"center"`，默认为 `"bottom"`）
- `close_button`：可选的按钮标签，用于关闭通知（默认：False）
- `type`：可选类型（`"positive"`、`"negative"`、`"warning"`、`"info"` 或 `"ongoing"`）
- `color`：可选的颜色名称
- `multi_line`：启用多行通知
- `icon`：可选的图标名称，以在通知中显示（默认：`None`）
- `spinner`：在通知中显示一个旋转器（默认：`False`）
- `timeout`：可选的超时时间（秒），在此之后通知将被移除（默认：`5.0`）

注意：您可以根据 Quasar 的 [Notify API](https://quasar.dev/quasar-plugins/notify#notify-api) 传递其他关键字参数。

```python
import asyncio
from nicegui import ui

async def compute():
    n = ui.notification(timeout=None)
    for i in range(10):
        n.message = f'Computing {i/10:.0%}'
        n.spinner = True
        await asyncio.sleep(0.2)
    n.message = 'Done!'
    n.spinner = False
    await asyncio.sleep(1)
    n.dismiss()

ui.button('Compute', on_click=compute)

# ui.run()
```

