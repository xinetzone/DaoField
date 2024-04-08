(plotly:figurewidget-app)=
# 使用 FigureWidget ipywidgets 进行交互式数据分析

```python
import datetime
import numpy as np
import pandas as pd

import plotly.graph_objects as go
from ipywidgets import widgets
```

## NYC Flights Database

我们会申请查看 2013 年所有离开纽约的航班的延误情况。

```python
df = pd.read_csv(
    'https://media.githubusercontent.com/media/xinet-collections/test-dastsets/main/nycflights.csv')
df = df.drop(df.columns[[0]], axis=1)
```

```python
df.sample(3)
```

让我们获得所有 `airlines` 的集合，以便稍后在搜索框中输入正确的内容。

```python
df['carrier'].unique()
```

让我们来分配我们将在应用程序中使用的小部件。一般来说，所有这些小部件都将用于筛选数据集，从而实现可视化。

```python
month = widgets.IntSlider(
    value=1.0,
    min=1.0,
    max=12.0,
    step=1.0,
    description='Month:',
    continuous_update=False
)

use_date = widgets.Checkbox(
    description='Date: ',
    value=True,
)

container = widgets.HBox(children=[use_date, month])

textbox = widgets.Dropdown(
    description='Airline:   ',
    value='DL',
    options=df['carrier'].unique().tolist()
)

origin = widgets.Dropdown(
    options=list(df['origin'].unique()),
    value='LGA',
    description='Origin Airport:',
)


# Assign an empty figure widget with two traces
trace1 = go.Histogram(x=df['arr_delay'], opacity=0.75, name='Arrival Delays')
trace2 = go.Histogram(x=df['dep_delay'], opacity=0.75, name='Departure Delays')
g = go.FigureWidget(data=[trace1, trace2],
                    layout=go.Layout(
                        title=dict(
                            text='NYC FlightDatabase'
                        ),
                        barmode='overlay'
                    ))
```

现在让我们编写一个函数来处理来自小部件的输入，并改变 graph 的状态。

```python
def validate():
    if origin.value in df['origin'].unique() and textbox.value in df['carrier'].unique():
        return True
    else:
        return False


def response(change):
    if validate():
        if use_date.value:
            filter_list = [i and j and k for i, j, k in
                           zip(df['month'] == month.value, df['carrier'] == textbox.value,
                               df['origin'] == origin.value)]
            temp_df = df[filter_list]

        else:
            filter_list = [i and j for i, j in
                           zip(df['carrier'] == 'DL', df['origin'] == origin.value)]
            temp_df = df[filter_list]
        x1 = temp_df['arr_delay']
        x2 = temp_df['dep_delay']
        with g.batch_update():
            g.data[0].x = x1
            g.data[1].x = x2
            g.layout.barmode = 'overlay'
            g.layout.xaxis.title = 'Delay in Minutes'
            g.layout.yaxis.title = 'Number of Delays'


origin.observe(response, names="value")
textbox.observe(response, names="value")
month.observe(response, names="value")
use_date.observe(response, names="value")
```

是时候试试这个应用了！！

```python
:tags: [hide-output]
container2 = widgets.HBox([origin, textbox])
widgets.VBox([container,
              container2,
              g])
```

<img src = 'https://media.githubusercontent.com/media/xinet-collections/test-dastsets/main/tests/figurewidget-app.gif' >

