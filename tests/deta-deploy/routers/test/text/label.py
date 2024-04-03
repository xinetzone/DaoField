from pathlib import Path
from nicegui import ui
from ..utils import create_doc

ROOT = Path(__file__).parent

def create_label():
    from nicegui import ui

    ui.label('一些标记')

    # ui.run()

def text_change():
    from nicegui import ui

    class status_label(ui.label):
        def _handle_text_change(self, text: str) -> None:
            super()._handle_text_change(text)
            if text == 'ok':
                self.classes(replace='text-positive')
            else:
                self.classes(replace='text-negative')

    model = {'status': 'error'}
    status_label().bind_text_from(model, 'status')
    ui.switch(on_change=lambda e: model.update(status='ok' if e.value else 'error'))
    # ui.run()

def callback():
    with open(f"{ROOT}/doc/label1.md", encoding="utf-8") as fp:
        content = fp.read()
    ui.markdown(content)
    create_doc(create_label)
    with open(f"{ROOT}/doc/label2.md", encoding="utf-8") as fp:
        content = fp.read()
    ui.markdown(content)
    create_doc(text_change)
