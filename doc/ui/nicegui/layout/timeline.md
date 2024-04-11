# {func}`~nicegui.ui.timeline` 时间轴

这个元素代表了 Quasar 的 [QTimeline 组件](https://quasar.dev/vue-components/timeline#qtimeline-api)。

- `side`：Side（`"left"` 或 `"right"`；默认："`left"`）。
- `layout`：Layout（`"dense"`, `"comfortable"` 或 `"loose"`；默认：`"dense"`）。
- `color`：图标的颜色。

```python
from nicegui import ui

with ui.timeline(side='right'):
    ui.timeline_entry('Rodja and Falko start working on NiceGUI.',
                      title='Initial commit',
                      subtitle='May 07, 2021')
    ui.timeline_entry('The first PyPI package is released.',
                      title='Release of 0.1',
                      subtitle='May 14, 2021')
    ui.timeline_entry('Large parts are rewritten to remove JustPy '
                      'and to upgrade to Vue 3 and Quasar 2.',
                      title='Release of 1.0',
                      subtitle='December 15, 2022',
                      icon='rocket')

# ui.run()
```
