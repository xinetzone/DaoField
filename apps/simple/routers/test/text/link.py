from pathlib import Path
from nicegui import ui
from ..utils import create_doc

ROOT = Path(__file__).parent

def create_link():
    from nicegui import ui

    ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

    # ui.run()

def create_link2():
    from nicegui import ui

    navigation = ui.row()
    ui.link_target('target_A')
    ui.label(
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
        'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    )
    label_B = ui.label(
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. '
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
        'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    )
    with navigation:
        ui.link('Goto A', '#target_A')
        ui.link('Goto B', label_B)

    # ui.run()

def create_link3():
    from nicegui import ui

    @ui.page('/some_other_page')
    def my_page():
        ui.label('This is another page')

    ui.label('Go to other page')
    ui.link('... with path', '/some_other_page')
    ui.link('... with function reference', my_page)

    # ui.run()

def create_link4():
    from nicegui import ui

    with ui.link(target='https://github.com/zauberzeug/nicegui'):
        ui.image('https://picsum.photos/id/41/640/360').classes('w-64')

    # ui.run()

def callback():
    with open(f"{ROOT}/doc/link.md", encoding="utf-8") as fp:
        content = fp.read()
    ui.markdown(content)
    create_doc(create_link)
    with open(f"{ROOT}/doc/link2.md", encoding="utf-8") as fp:
        content = fp.read()
    ui.markdown(content)
    create_doc(create_link2)
    with open(f"{ROOT}/doc/link3.md", encoding="utf-8") as fp:
        content = fp.read()
    ui.markdown(content)
    create_doc(create_link3)
    with open(f"{ROOT}/doc/link4.md", encoding="utf-8") as fp:
        content = fp.read()
    ui.markdown(content)
    create_doc(create_link4)
   