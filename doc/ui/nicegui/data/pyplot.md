# {func}`~nicegui.ui.pyplot` Matplotlib 绘图

创建上下文来配置 [Matplotlib 绘图](https://matplotlib.org/)。

- `close`: 是否应在退出上下文后关闭图形；如果您稍后想要更新它，请设置为 `False`（默认：`True`）
- `kwargs`: 应传递给 [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html) 的参数，如 `figsize`

```python
import numpy as np
from matplotlib import pyplot as plt
from nicegui import ui

with ui.pyplot(figsize=(3, 2)):
    x = np.linspace(0.0, 5.0)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    plt.plot(x, y, '-')

# ui.run()
```
