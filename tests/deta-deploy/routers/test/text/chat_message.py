from pathlib import Path
from nicegui import ui
from ..utils import create_doc

ROOT = Path(__file__).parent

def create():
    from nicegui import ui

    ui.chat_message('Hello NiceGUI!',
                    name='Robot',
                    stamp='now',
                    avatar='https://robohash.org/ui')

    # ui.run()

def create2():
    from nicegui import ui

    ui.chat_message('Without <strong>HTML</strong>')
    ui.chat_message('With <strong>HTML</strong>', text_html=True)

    # ui.run()

def create3():
    from nicegui import ui

    ui.chat_message('This is a\nlong line!')

    # ui.run()

def create4():
    from nicegui import ui

    ui.chat_message(['Hi! 😀', 'How are you?']
                    )

    # ui.run()

def create5():
    from nicegui import ui

    with ui.chat_message():
        ui.label('Guess where I am!')
        ui.image('https://picsum.photos/id/249/640/360').classes('w-64')

    # ui.run()

def callback():
    with open(f"{ROOT}/doc/chat_message.md", encoding="utf-8") as fp:
        content = fp.read()
    ui.markdown(content)
    create_doc(create)
    ui.markdown("""
    ## HTML文本

    使用 `text_html` 参数，您可以向聊天发送HTML文本。
    """)
    create_doc(create2)
    ui.markdown("""
    ## 换行

    您可以在聊天消息中使用换行符。
    """)
    create_doc(create3)
    ui.markdown("""
    ## 多部分消息

    您可以通过传递字符串列表来发送多个消息部分。
    """)
    create_doc(create4)
    ui.markdown("""
    ## 带有子元素的聊天消息

    您可以向聊天消息添加子元素。
    """)
    create_doc(create5)