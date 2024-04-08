(dash:dcc/range-slider)=
# `dcc.RangeSlider`

参考：[dcc.RangeSlider | Dash for Python Documentation | Plotly](https://dash.plotly.com/dash-core-components/rangeslider)

## `dcc.RangeSlider` 简单例子

一个绑定回调的基本 RangeSlider 的例子。


```{include} ../../tests/dash-examples/simple_range_slider.py
:code: python
```

## 标记和步长

如果滑块 `marks` 被定义并且 `step` 被设置为 `None`，那么滑块将只能选择标记预定义的值。注意，默认值是 `step=1`，因此必须显式指定 `None` 以获得此行为。

```{include} ../../tests/dash-examples/mark_range_slider.py
:code: python
```

待续。。。