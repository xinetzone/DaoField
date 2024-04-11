# {func}`~nicegui.ui.tabs` 标签页

元素 `ui.tabs`、`ui.tab`、`ui.tab_panels` 和 `ui.tab_panel` 类似于 Quasar 的[标签页](https://quasar.dev/vue-components/tabs)和[标签面板](https://quasar.dev/vue-components/tab-panels%3E) API。

`ui.tabs` 创建一个容器来容纳标签页。例如，它可以放置在一个 `ui.header` 中。`ui.tab_panels` 创建一个带有实际内容的标签面板的容器。每个 `ui.tab_panel` 都与一个 `ui.tab` 元素相关联。

```python
from nicegui import ui

with ui.tabs().classes('w-full') as tabs:
    one = ui.tab('One')
    two = ui.tab('Two')
with ui.tab_panels(tabs, value=two).classes('w-full'):
    with ui.tab_panel(one):
        ui.label('First tab')
    with ui.tab_panel(two):
        ui.label('Second tab')

# ui.run()
```

## {func}`~nicegui.ui.tabs` 名称、标签、图标

`ui.tab` 元素具有一个 `label` 属性，可用于显示与 `name` 不同的文本。`name` 也可以代替 `ui.tab` 对象，将 `ui.tab` 与 `ui.tab_panel` 关联起来。此外，每个标签页都可以有一个图标。

```python
from nicegui import ui

with ui.tabs() as tabs:
    ui.tab('h', label='Home', icon='home')
    ui.tab('a', label='About', icon='info')
with ui.tab_panels(tabs, value='h').classes('w-full'):
    with ui.tab_panel('h'):
        ui.label('Main Content')
    with ui.tab_panel('a'):
        ui.label('Infos')

# ui.run()
```

## {func}`~nicegui.ui.tabs` 通过编程切换标签页

`ui.tabs` 和 `ui.tab_panels` 元素派生自 `ValueElement`，它具有 `set_value` 方法。可以使用该方法通过编程方式切换标签页。

```python
from nicegui import ui

content = {'Tab 1': 'Content 1', 'Tab 2': 'Content 2', 'Tab 3': 'Content 3'}
with ui.tabs() as tabs:
    for title in content:
        ui.tab(title)
with ui.tab_panels(tabs).classes('w-full') as panels:
    for title, text in content.items():
        with ui.tab_panel(title):
            ui.label(text)

ui.button('GoTo 1', on_click=lambda: panels.set_value('Tab 1'))
ui.button('GoTo 2', on_click=lambda: tabs.set_value('Tab 2'))

# ui.run()
```

## {func}`~nicegui.ui.tabs` 带有分隔符的垂直标签页

与 [Quasar 的垂直标签页示例](https://quasar.dev/vue-components/tabs#vertical)类似，我们可以将 ui.splitter 和 tab 元素结合起来创建一个垂直标签页布局。

```python
from nicegui import ui

with ui.splitter(value=30).classes('w-full h-56') as splitter:
    with splitter.before:
        with ui.tabs().props('vertical').classes('w-full') as tabs:
            mail = ui.tab('Mails', icon='mail')
            alarm = ui.tab('Alarms', icon='alarm')
            movie = ui.tab('Movies', icon='movie')
    with splitter.after:
        with ui.tab_panels(tabs, value=mail) \
                .props('vertical').classes('w-full h-full'):
            with ui.tab_panel(mail):
                ui.label('Mails').classes('text-h4')
                ui.label('Content of mails')
            with ui.tab_panel(alarm):
                ui.label('Alarms').classes('text-h4')
                ui.label('Content of alarms')
            with ui.tab_panel(movie):
                ui.label('Movies').classes('text-h4')
                ui.label('Content of movies')

# ui.run()
```
