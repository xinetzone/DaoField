# {func}`~nicegui.ui.echart` ECharts 图表

使用 [ECharts](https://echarts.apache.org/) 创建图表的元素。通过更改 `options` 属性可以向图表推送更新。数据变更后，调用 `update` 方法刷新图表。

- `options`: EChart 选项的字典
- `on_click_point`: 点击点时调用的回调函数

```python
from nicegui import ui
from random import random

echart = ui.echart({
    'xAxis': {'type': 'value'},
    'yAxis': {'type': 'category', 'data': ['A', 'B'], 'inverse': True},
    'legend': {'textStyle': {'color': 'gray'}},
    'series': [
        {'type': 'bar', 'name': 'Alpha', 'data': [0.1, 0.2]},
        {'type': 'bar', 'name': 'Beta', 'data': [0.3, 0.4]},
    ],
})

def update():
    echart.options['series'][0]['data'][0] = random()
    echart.update()

ui.button('Update', on_click=update)

# ui.run()
```

## {func}`~nicegui.ui.echart` 可点击的点

您可以注册回调函数，用于处理点击序列点时的事件。

```python
from nicegui import ui

ui.echart({
    'xAxis': {'type': 'category'},
    'yAxis': {'type': 'value'},
    'series': [{'type': 'line', 'data': [20, 10, 30, 50, 40, 30]}],
}, on_point_click=ui.notify)

# ui.run()
```

## {func}`~nicegui.ui.echart` 动态属性

可以将动态属性传递给图表元素以自定义它们，例如应用轴标签格式。要使属性动态化，请在属性名称前加上冒号`":"`。

```python
from nicegui import ui

ui.echart({
    'xAxis': {'type': 'category'},
    'yAxis': {'axisLabel': {':formatter': 'value => "$" + value'}},
    'series': [{'type': 'line', 'data': [5, 8, 13, 21, 34, 55]}],
})

# ui.run()
```

## {func}`~nicegui.ui.echart` 元素

您可以使用`from_pyecharts`方法从`pyecharts`对象创建`EChart`元素。要定义动态选项，如格式化函数，可以使用`pyecharts.commons.utils`中的`JsCode`类。或者，您可以使用冒号`":"`前缀属性名称，表示该值是JavaScript表达式。

```python
from nicegui import ui
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.options import AxisOpts

ui.echart.from_pyecharts(
    Bar()
    .add_xaxis(['A', 'B', 'C'])
    .add_yaxis('ratio', [1, 2, 4])
    .set_global_opts(
        xaxis_opts=AxisOpts(axislabel_opts={
            ':formatter': r'(val, idx) => `group ${val}`',
        }),
        yaxis_opts=AxisOpts(axislabel_opts={
            'formatter': JsCode(r'(val, idx) => `${val}%`'),
        }),
    )
)

ui.run()
```

## {func}`~nicegui.ui.echart` 运行方法

您可以使用`run_chart_method`方法运行EChart实例的方法。这个演示展示了如何显示和隐藏加载动画，如何获取图表的当前宽度，以及如何使用自定义格式化器添加提示工具。

方法名`"setOption"`前面的冒号`":"`表示该参数是一个JavaScript表达式，在传递给方法之前会在客户端进行求值。

```python
from nicegui import ui

echart = ui.echart({
    'xAxis': {'type': 'category', 'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']},
    'yAxis': {'type': 'value'},
    'series': [{'type': 'line', 'data': [150, 230, 224, 218, 135]}],
})

ui.button('Show Loading', on_click=lambda: echart.run_chart_method('showLoading'))
ui.button('Hide Loading', on_click=lambda: echart.run_chart_method('hideLoading'))

async def get_width():
    width = await echart.run_chart_method('getWidth')
    ui.notify(f'Width: {width}')
ui.button('Get Width', on_click=get_width)

ui.button('Set Tooltip', on_click=lambda: echart.run_chart_method(
    ':setOption', r'{tooltip: {formatter: params => "$" + params.value}}',
))

ui.run()
```

## {func}`~nicegui.ui.echart` 任意图表事件

您可以使用`on`方法以及`"chart:"`前缀为图表注册任意事件监听器。这个演示展示了如何为`"selectchanged"`事件注册回调函数，该事件在用户选择点时触发。

```python
from nicegui import ui

ui.echart({
    'toolbox': {'feature': {'brush': {'type': ['rect']}}},
    'brush': {},
    'xAxis': {'type': 'category'},
    'yAxis': {'type': 'value'},
    'series': [{'type': 'line', 'data': [1, 2, 3]}],
}).on('chart:selectchanged', lambda e: label.set_text(
    f'Selected point {e.args["fromActionPayload"]["dataIndexInside"]}'
))
label = ui.label()

# ui.run()
```
