# {func}`~nicegui.ui.step` 分步器

这个元素代表了 Quasar 的 [QStepper 组件](https://quasar.dev/vue-components/stepper#qstepper-api)。它包含各个独立的步骤。

为了避免在切换步骤时出现动态元素的问题，这个元素使用了 Vue 的 keep-alive 组件。如果客户端性能是一个问题，您可以禁用此功能。

`value`：ui.step 或最初选择的步骤的名称（默认：`None`，表示第一步）
`on_value_change`：当选定的步骤发生变化时要执行的回调函数
`keep_alive`：是否在内容上使用 Vue 的 keep-alive 组件（默认：`True`）

```python
from nicegui import ui

with ui.stepper().props('vertical').classes('w-full') as stepper:
    with ui.step('Preheat'):
        ui.label('Preheat the oven to 350 degrees')
        with ui.stepper_navigation():
            ui.button('Next', on_click=stepper.next)
    with ui.step('Ingredients'):
        ui.label('Mix the ingredients')
        with ui.stepper_navigation():
            ui.button('Next', on_click=stepper.next)
            ui.button('Back', on_click=stepper.previous).props('flat')
    with ui.step('Bake'):
        ui.label('Bake for 20 minutes')
        with ui.stepper_navigation():
            ui.button('Done', on_click=lambda: ui.notify('Yay!', type='positive'))
            ui.button('Back', on_click=stepper.previous).props('flat')

# ui.run()
```

## {func}`~nicegui.ui.step` 动态分步器

步骤可以动态添加，并通过 `ui.move()` 定位。

```python
from nicegui import ui

def next_step() -> None:
    if extra_step.value and len(stepper.default_slot.children) == 2:
        with stepper:
            with ui.step('extra') as extra:
                ui.label('Extra')
                with ui.stepper_navigation():
                    ui.button('Back', on_click=stepper.previous).props('flat')
                    ui.button('Next', on_click=stepper.next)
            extra.move(target_index=1)
    stepper.next()

with ui.stepper().props('vertical').classes('w-full') as stepper:
    with ui.step('start'):
        ui.label('Start')
        extra_step = ui.checkbox('do extra step')
        with ui.stepper_navigation():
            ui.button('Next', on_click=next_step)
    with ui.step('finish'):
        ui.label('Finish')
        with ui.stepper_navigation():
            ui.button('Back', on_click=stepper.previous).props('flat')

# ui.run()
```
