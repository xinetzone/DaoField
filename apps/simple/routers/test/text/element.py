from pathlib import Path
from nicegui import ui
from ..utils import create_doc

ROOT = Path(__file__).parent

def create():
    from nicegui import ui

    with ui.element('div').classes('p-2 bg-blue-100'):
        ui.label('inside a colored div')

    # ui.run()

def create2():
    from nicegui import ui

    with ui.card() as a:
        ui.label('A')
        x = ui.label('X')

    with ui.card() as b:
        ui.label('B')

    ui.button('Move X to A', on_click=lambda: x.move(a))
    ui.button('Move X to B', on_click=lambda: x.move(b))
    ui.button('Move X to top', on_click=lambda: x.move(target_index=0))

    # ui.run()

def create3():
    from nicegui import ui

    ui.button.default_props('rounded outline')
    ui.button('Button A')
    ui.button('Button B')

    # ui.run()

def create4():
    from nicegui import ui

    ui.label.default_classes('bg-blue-100 p-2')
    ui.label('Label A')
    ui.label('Label B')

    # ui.run()

def create5():
    from nicegui import ui

    ui.label.default_style('color: tomato')
    ui.label('Label A')
    ui.label('Label B')

    # ui.run()

def callback():
    ui.markdown("""
    # 通用元素

    这个类是所有其他UI元素的基类。但是，您可以使用它来创建具有任意HTML标签的元素。

    - `tag`：元素的HTML标签
    - `_client`：此元素的客户端（仅用于内部使用）
    """)
    create_doc(create)
    ui.markdown("""
    ## 移动元素

    此演示展示了如何在容器之间或在容器内移动元素。
    """)
    create_doc(create2)
    ui.markdown("""
    ## 默认属性

    您可以为某个类的所有元素设置默认属性。这样，您就可以避免一遍又一遍地重复相同的属性。

    默认属性仅适用于在设置默认属性后创建的元素。子类继承其父类的默认属性。
    """)
    create_doc(create3)
    ui.markdown("""
    ## 默认类

    您可以为某个类的所有元素设置默认类。这样，您就可以避免一遍又一遍地重复相同的类。

    默认类仅适用于在设置默认类后创建的元素。子类继承其父类的默认类。
    """)
    create_doc(create4)
    ui.markdown("""
    ## 默认样式

    您可以为某个类的所有元素设置默认样式。这样，您就可以避免一遍又一遍地重复相同的样式。

    默认样式仅适用于在设置默认样式后创建的元素。子类继承其父类的默认样式。
    """)
    create_doc(create5)
