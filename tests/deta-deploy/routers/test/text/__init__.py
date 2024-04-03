from pathlib import Path
from nicegui import ui
from . import label, link, chat_message, element, markdown, rst, mermaid, html

ROOT = Path(__file__).parent

def text_intro():
    with ui.splitter(value=10).classes('w-full h-full') as splitter:
        with splitter.before:
            with ui.tabs().props('vertical').classes('w-full') as tabs:
                label_tab = ui.tab('标签', icon='label')
                link_tab = ui.tab('链接', icon='link')
                chat_tab = ui.tab('聊天消息', icon='chat')
                elem_tab = ui.tab('通用元素')
                md_tab = ui.tab("markdown")
                rst_tab = ui.tab("rst")
                mermaid_tab = ui.tab("mermaid")
                html_tab = ui.tab("html")
        with splitter.after:
            with ui.tab_panels(tabs, value=label_tab).props('vertical').classes('w-full h-full'):
                with ui.tab_panel(label_tab):
                    label.callback()
                with ui.tab_panel(link_tab):
                    link.callback()
                with ui.tab_panel(chat_tab):
                    chat_message.callback()
                with ui.tab_panel(elem_tab):
                    element.callback()
                with ui.tab_panel(md_tab):
                    markdown.callback()
                with ui.tab_panel(rst_tab):
                    rst.callback()
                with ui.tab_panel(mermaid_tab):
                    mermaid.callback()
                with ui.tab_panel(html_tab):
                    html.callback()
