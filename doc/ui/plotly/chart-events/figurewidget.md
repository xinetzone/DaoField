(plotly:figurewidget)=
# Plotly FigureWidget 概述

参考：[Plotly FigureWidget Overview | Python | Plotly](https://plotly.com/python/figurewidget/)

## 创建一个简单的 FigureWidget

创建一个空的 FigureWidget，然后查看它。

```python
import plotly.graph_objects as go

f = go.FigureWidget()
f
```

添加轨迹或更新布局，然后观察上面的输出实时更新。


```python
f.add_scatter(y=[2, 1, 4, 3]);
```

```python
f.add_bar(y=[1, 4, 3, 2]);
```

```python
f.layout.title = 'Hello FigureWidget'
```

<img src='https://media.githubusercontent.com/media/xinet-collections/test-dastsets/main/tests/figurewidget-create.gif'>

## 更新数据和布局

```python
# update scatter data
scatter = f.data[0]
scatter.y = [3, 1, 4, 3]
```

```python
# update bar data
bar = f.data[1]
bar.y = [5, 3, 2, 8]
```

```python
f.layout.title.text = 'This is a new title'
```

## 从 Figure graph object 构建 FigureWidget

标准的 `Figure` 对象可以传递给 `FigureWidget` 构造函数。

```python
import plotly.graph_objects as go

trace = go.Heatmap(z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   y=['Morning', 'Afternoon', 'Evening'])
data=[trace]
layout = go.Layout(title='Activity Heatmap')

figure = go.Figure(data=data, layout=layout)

f2 = go.FigureWidget(figure)
f2
```

````{topic} 参考
请参阅[这些 Jupyter 笔记本](https://github.com/jonmmease/plotly_ipywidget_notebooks)，以获得更多 FigureWidget 示例。

```python
:tags: [output_scroll]

help(go.FigureWidget)
```
````