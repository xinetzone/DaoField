(dash:urls)=
# 多页面应用程序和 URL 支持

参考：[URL Routing and Multiple Apps | Dash for Python Documentation | Plotly](https://dash.plotly.com/urls)

Dash 将网络应用程序渲染为“单页应用”。当使用 `dcc.Link` 时，导航过程中应用程序不会完全重新加载，这使得浏览速度非常快。使用 Dash，您可以利用 `dcc.Location`、`dcc.Link` 组件和回调函数构建多页面应用。

[Dash Pages](pages) 使用这些组件，并抽象化了 URL 路由所需的回调逻辑，使得快速上手构建多页面应用变得简单。如果您想要在不使用 Pages 的情况下构建多页面应用，请参阅下方的 [“不使用 Pages 的多页面应用”](https://dash.plotly.com/urls#multi-page-apps-without-pages) 部分。

```{toctree}
pages
```