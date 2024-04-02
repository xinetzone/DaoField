from pathlib import Path
from nicegui import ui
from ..utils import create_doc

ROOT = Path(__file__).parent

def create():
    from nicegui import ui

    ui.restructured_text('This is **reStructuredText**.')

    # ui.run()

def create2():
    from nicegui import ui

    ui.restructured_text('''
        This is an example of a reStructuredText paragraph with several indentation levels.

        You can use multiple levels of indentation to structure your content.
        Each level of indentation represents a different level of hierarchy.

        - Level 1
            - Level 2
                - Level 3
                    - Level 4
                        - Level 5
    ''')

    # ui.run()

def create3():
    from nicegui import ui

    ui.restructured_text('''
        .. code-block:: python3
        
            from nicegui import ui

            ui.label('Hello World!')

            ui.run()
    ''')

    # ui.run()

def create4():
    from nicegui import ui

    ui.restructured_text('''
        +-------+-------+---------+--------+
        | A     | B     | A and B | A or B |
        +=======+=======+=========+========+
        | False | False | False   | False  |
        +-------+-------+---------+--------+
        | True  | False | False   | True   |
        +-------+-------+---------+--------+
        | False | True  | False   | True   |
        +-------+-------+---------+--------+
        | True  | True  | True    | True   |
        +-------+-------+---------+--------+
    ''')

    # ui.run()

def callback():
    ui.markdown("""
    # ReStructuredText

    将 ReStructuredText 渲染到页面上。

    `content`：要显示的 ReStructuredText 内容
    """)
    create_doc(create)
    ui.markdown("""
    ## 带有缩进的 reStructuredText

    您可以对 reStructuredText 元素进行缩进来创建层次结构。为了保持相对缩进，每行开头的常见缩进会自动被去除，因此您可以缩进多行字符串。
    """)
    create_doc(create2)
    ui.markdown("""
    ## 带有代码块的 reStructuredText

    您可以使用代码块来显示代码示例。如果指定了语言，代码将会被语法高亮显示。请参阅此链接以获取支持的语言列表。
    """)
    create_doc(create3)
    ui.markdown("""
    ## 带有表格的 reStructuredText

    有关 reStructuredText 表格的更多信息，请参阅 [Sphinx 文档](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables)。
    """)
    create_doc(create4)
