from fastapi import FastAPI
from nicegui import app as gui, ui

class status_label(ui.label):
    def _handle_text_change(self, text: str) -> None:
        super()._handle_text_change(text)
        if text == 'ok':
            self.classes(replace='text-positive')
        else:
            self.classes(replace='text-negative')

@ui.page('/')
async def home():
    model = {'status': 'error'}
    status_label().bind_text_from(model, 'status')
    ui.switch(on_change=lambda e: model.update(status='ok' if e.value else 'error'))


app = FastAPI()
ui.run_with(
    app,
    # mount_path='/gui',  # NOTE 如果你希望传递给 `@ui.page` 的路径位于根目录，这个可以省略
    storage_secret='在这里选择你的私人密钥',  # NOTE 设置密钥是可选的，但允许每个用户进行持久存储。
)
