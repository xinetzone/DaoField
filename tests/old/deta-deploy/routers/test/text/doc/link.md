# 链接

创建超链接。

要在页面内跳转到特定位置，您可以使用 `ui.link_target("name")` 放置可链接锚点，并使用 `ui.link(target="#name")` 进行链接。

- `text`：显示文本
- `target`：页面函数、同一页面上的 NiceGUI 元素或从基本 URL 开始的绝对 URL 或相对路径的字符串
- `new_tab`：在新标签页中打开链接（默认：`False`）