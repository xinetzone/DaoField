# Highcharts 图表

使用[Highcharts](https://www.highcharts.com/)创建图表的元素。可以通过更改 `options` 属性来向图表推送更新。数据变更后，调用 `update` 方法刷新图表。

由于Highcharts的限制性许可证，该元素不是标准NiceGUI包的一部分。它维护在一个[单独的仓库](https://github.com/zauberzeug/nicegui-highcharts/)中，可以通过 `pip install nicegui[highcharts]` 进行安装。

默认情况下，会创建一个 `Highcharts.chart`。要使用例如 `Highcharts.stockChart`，请将 `type` 属性设置为 `"stockChart"`。

- `options`: Highcharts 选项的字典
- `type`: 图表类型（例如`"chart"`, `"stockChart"`, `"mapChart"`...; 默认：`"chart"`）
- `extras`: 要包含的额外依赖项列表（例如`"annotations"`, `"arc-diagram"`, `"solid-gauge"`...）
- `on_point_click`: 点击点时调用的回调函数
- `on_point_drag_start`: 开始拖动点时调用的回调函数
- `on_point_drag`: 拖动点时调用的回调函数
- `on_point_drop`: 放下点时调用的回调函数

```python
from nicegui import ui
from random import random

chart = ui.highchart({
    'title': False,
    'chart': {'type': 'bar'},
    'xAxis': {'categories': ['A', 'B']},
    'series': [
        {'name': 'Alpha', 'data': [0.1, 0.2]},
        {'name': 'Beta', 'data': [0.3, 0.4]},
    ],
}).classes('w-full h-64')

def update():
    chart.options['series'][0]['data'][0] = random()
    chart.update()

ui.button('Update', on_click=update)

ui.run()
```

## 外部依赖

要使用默认依赖项中未包含的图表类型，您可以指定额外的依赖项。这个演示展示了一个实心仪表盘图。

```python
from nicegui import ui

ui.highchart({
    'title': False,
    'chart': {'type': 'solidgauge'},
    'yAxis': {
        'min': 0,
        'max': 1,
    },
    'series': [
        {'data': [0.42]},
    ],
}, extras=['solid-gauge']).classes('w-full h-64')

ui.run()
```

## 可拖曳点

这个图表允许拖动序列点。您可以为以下事件注册回调函数：

- `on_point_click`: 点击点时调用
- `on_point_drag_start`: 开始拖动点时调用
- `on_point_drag`: 拖动点时调用
- `on_point_drop`: 放下点时调用

```python
from nicegui import ui

ui.highchart(
    {
        'title': False,
        'plotOptions': {
            'series': {
                'stickyTracking': False,
                'dragDrop': {'draggableY': True, 'dragPrecisionY': 1},
            },
        },
        'series': [
            {'name': 'A', 'data': [[20, 10], [30, 20], [40, 30]]},
            {'name': 'B', 'data': [[50, 40], [60, 50], [70, 60]]},
        ],
    },
    extras=['draggable-points'],
    on_point_click=lambda e: ui.notify(f'Click: {e}'),
    on_point_drag_start=lambda e: ui.notify(f'Drag start: {e}'),
    on_point_drop=lambda e: ui.notify(f'Drop: {e}')
).classes('w-full h-64')

ui.run()
```