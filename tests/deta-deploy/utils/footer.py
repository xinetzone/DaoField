from nicegui import app as gui, ui

def create_footer():
    with ui.footer().style('background-color: grey').classes('items-center justify-between'):
        ui.label("工具链")
