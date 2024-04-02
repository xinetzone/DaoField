from pathlib import Path
from nicegui import ui
from ..utils import create_doc

ROOT = Path(__file__).parent

def create():
    from nicegui import ui

    ui.markdown('This is **Markdown**.')

    # ui.run()

def create2():
    from nicegui import ui

    ui.markdown('''
        ## Example

        This line is not indented.

            This block is indented.
            Thus it is rendered as source code.
        
        This is normal text again.
    ''')

    # ui.run()

def create3():
    from nicegui import ui

    ui.markdown('''
        ```python
        from nicegui import ui

        ui.label('Hello World!')

        ui.run(dark=True)
        ```
    ''')

    # ui.run()

def create4():
    from nicegui import ui

    ui.markdown('''
        | First name | Last name |
        | ---------- | --------- |
        | Max        | Planck    |
        | Marie      | Curie     |
    ''', extras=['tables'])

    # ui.run()

def create5():
    from nicegui import ui

    markdown = ui.markdown('Sample content')
    ui.button('Change Content', on_click=lambda: markdown.set_content('This is new content'))

    # ui.run()

def callback():
    ui.markdown("""
    # Markdown 元素

    将 Markdown 渲染到页面上。

    - `content`：要显示的 Markdown 内容
    - `extras`：[markdown2 扩展列表](https://github.com/trentm/python-markdown2/wiki/Extras#implemented-extras)
    （默认：`['fenced-code-blocks', 'tables']`）
    """)
    create_doc(create)
    ui.markdown("""
    ## 带有缩进的 Markdown

    每行开头的常见缩进会自动被去除。因此，您可以对 Markdown 元素进行缩进，它们仍然会被正确渲染。
    """)
    create_doc(create2)
    ui.markdown("""
    ## 带有代码块的 Markdown

    您可以使用代码块来显示代码示例。如果您在开头的三个反引号后面指定语言，代码将会被语法高亮显示。请参阅 [Pygments](https://pygments.org/languages/) 网站以获取支持的语言列表。。
    """)
    create_doc(create3)
    ui.markdown("""
    ## Markdown 表格

    通过激活 `"tables"` 额外功能，您可以使用 Markdown 表格。请参阅 [markdown2 文档](https://github.com/trentm/python-markdown2/wiki/Extras#implemented-extras)以获取可用额外功能的列表。
    """)
    create_doc(create4)
    ui.markdown("""
    ## 更改 Markdown 内容

    您可以通过设置其 `content` 属性或调用 `set_content` 来更改 Markdown 元素的内容。
    """)
    create_doc(create5)
