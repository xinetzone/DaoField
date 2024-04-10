# NiceGUI 环境变量

你可以设置以下环境变量来配置 NiceGUI：

- `MATPLOTLIB`（默认值：`true`）可以设置为 `false` 以避免可能代价高昂的 Matplotlib 导入。这将使 `ui.pyplot` 和 `ui.line_plot` 不可用。
- `NICEGUI_STORAGE_PATH`（默认值：本地 `".nicegui"`）可以设置为更改存储文件的位置。
- `MARKDOWN_CONTENT_CACHE_SIZE`（默认值：`1000`）：内存中缓存的 Markdown 内容片段的最大数量。
- `RST_CONTENT_CACHE_SIZE`（默认值：`1000`）：内存中缓存的 ReStructuredText 内容片段的最大数量。

```python
from nicegui import ui
from nicegui.elements import markdown

ui.label(f'Markdown content cache size is {markdown.prepare_content.cache_info().maxsize}')

# ui.run()
```
