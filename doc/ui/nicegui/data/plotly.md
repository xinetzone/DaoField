# {func}`~nicegui.ui.plotly` Plotly 图表

渲染一个Plotly图表。有两种方法可以传递一个用于渲染的Plotly图形，参见参数 `figure``:

- 传递 [`go.Figure` 对象](https://plotly.com/python/)
- [传递包含键 `data`, `layout`, `config`（可选）的 Python 字典对象](https://plotly.com/javascript/)
- 为了获得最佳性能，请使用声明式字典方法创建Plotly图表。

`figure`: 需要渲染的Plotly图形。可以是 `go.Figure` 实例，或者是一个带有键 `data`, `layout`, `config`（可选）的字典对象。

```python
import plotly.graph_objects as go
from nicegui import ui

fig = go.Figure(go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 2.5]))
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
ui.plotly(fig).classes('w-full h-40')

# ui.run()
```

## {func}`~nicegui.ui.plotly` 字典接口

这个演示展示了如何使用声明式字典接口创建图表。对于具有许多迹线和数据点的图表，这比面向对象接口更高效。定义对应于[JavaScript Plotly API](https://plotly.com/javascript/)。由于默认值不同，生成的图表可能与使用面向对象接口创建的相同图表略有不同，但功能是相同的。

```python
from nicegui import ui

fig = {
    'data': [
        {
            'type': 'scatter',
            'name': 'Trace 1',
            'x': [1, 2, 3, 4],
            'y': [1, 2, 3, 2.5],
        },
        {
            'type': 'scatter',
            'name': 'Trace 2',
            'x': [1, 2, 3, 4],
            'y': [1.4, 1.8, 3.8, 3.2],
            'line': {'dash': 'dot', 'width': 3},
        },
    ],
    'layout': {
        'margin': {'l': 15, 'r': 0, 't': 0, 'b': 15},
        'plot_bgcolor': '#E5ECF6',
        'xaxis': {'gridcolor': 'white'},
        'yaxis': {'gridcolor': 'white'},
    },
}
ui.plotly(fig).classes('w-full h-40')

# ui.run()
```

## {func}`~nicegui.ui.plotly` 更新图

这个演示展示了如何实时更新图表。点击按钮向图表中添加新的痕迹线。要发送新的图表到浏览器，确保明确调用 `plot.update()` 或 `ui.update(plot)`。

```python
import plotly.graph_objects as go
from nicegui import ui
from random import random

fig = go.Figure()
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
plot = ui.plotly(fig).classes('w-full h-40')

def add_trace():
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[random(), random(), random()]))
    plot.update()

ui.button('Add trace', on_click=add_trace)

# ui.run()
```

## {func}`~nicegui.ui.plotly` 事件

这个演示展示了如何处理Plotly事件。尝试点击一个数据点以查看事件数据。

目前，支持以下事件：`"plotly_click"`（点击），`"plotly_legendclick"`（图例点击），`"plotly_selecting"`（选择中），`"plotly_selected"`（选中），`"plotly_hover"`（悬停），`"plotly_unhover"`（取消悬停），`"plotly_legenddoubleclick"`（双击图例），`"plotly_restyle"`（重新样式化），`"plotly_relayout"`（重新布局），`"plotly_webglcontextlost"`（WebGL上下文丢失），`"plotly_afterplot"`（绘制后），`"plotly_autosize"`（自动调整大小），`"plotly_deselect"`（取消选择），`"plotly_doubleclick"`（双击），`"plotly_redraw"`（重绘），`"plotly_animated"`（动画）。更多信息请参阅[Plotly文档](https://plotly.com/javascript/plotlyjs-events/)。

```python
import plotly.graph_objects as go
from nicegui import ui

fig = go.Figure(go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 2.5]))
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
plot = ui.plotly(fig).classes('w-full h-40')
plot.on('plotly_click', ui.notify)

# ui.run()
```