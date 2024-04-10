# NiceGUI 可刷新的 UI 函数

`@ui.refreshable` 装饰器允许您创建具有 `refresh` 方法的函数。该方法将自动删除由该函数创建的所有元素并重新创建它们。

```python
import random
from nicegui import ui

numbers = []

@ui.refreshable
def number_ui() -> None:
    ui.label(', '.join(str(n) for n in sorted(numbers)))

def add_number() -> None:
    numbers.append(random.randint(0, 100))
    number_ui.refresh()

number_ui()
ui.button('Add random number', on_click=add_number)

# ui.run()
```

## 带参数的可刷新 UI

这里是一个演示，展示了如何使用 `refreshable` 装饰器创建一个可以使用不同参数刷新的 UI。

```python
import pytz
from datetime import datetime
from nicegui import ui

@ui.refreshable
def clock_ui(timezone: str):
    ui.label(f'Current time in {timezone}:')
    ui.label(datetime.now(tz=pytz.timezone(timezone)).strftime('%H:%M:%S'))

clock_ui('Europe/Berlin')
ui.button('Refresh', on_click=clock_ui.refresh)
ui.button('Refresh for New York', on_click=lambda: clock_ui.refresh('America/New_York'))
ui.button('Refresh for Tokyo', on_click=lambda: clock_ui.refresh('Asia/Tokyo'))

# ui.run()
```

## NiceGUI 用于输入验证的可刷新 UI

这里是一个演示，展示了如何使用 `refreshable` 装饰器来提供有关用户输入有效性的反馈。

```python
import re
from nicegui import ui

pwd = ui.input('Password', password=True, on_change=lambda: show_info.refresh())

rules = {
    'Lowercase letter': lambda s: re.search(r'[a-z]', s),
    'Uppercase letter': lambda s: re.search(r'[A-Z]', s),
    'Digit': lambda s: re.search(r'\d', s),
    'Special character': lambda s: re.search(r"[!@#$%^&*(),.?':{}|<>]", s),
    'min. 8 characters': lambda s: len(s) >= 8,
}

@ui.refreshable
def show_info():
    for rule, check in rules.items():
        with ui.row().classes('items-center gap-2'):
            if check(pwd.value or ''):
                ui.icon('done', color='green')
                ui.label(rule).classes('text-xs text-green strike-through')
            else:
                ui.icon('radio_button_unchecked', color='red')
                ui.label(rule).classes('text-xs text-red')

show_info()

# ui.run()
```

# NiceGUI 带有响应式状态的可刷新 UI

您可以使用 `ui.state` 函数创建响应式状态变量，如本演示中的 `count` 和 `color`。它们可以像普通变量一样用于创建 UI 元素，如 `ui.label`。可以使用相应的设置器函数来设置新值，这将自动刷新 UI。

```python
from nicegui import ui

@ui.refreshable
def counter(name: str):
    with ui.card():
        count, set_count = ui.state(0)
        color, set_color = ui.state('black')
        ui.label(f'{name} = {count}').classes(f'text-{color}')
        ui.button(f'{name} += 1', on_click=lambda: set_count(count + 1))
        ui.select(['black', 'red', 'green', 'blue'],
                  value=color, on_change=lambda e: set_color(e.value))

with ui.row():
    counter('A')
    counter('B')

# ui.run()
```
