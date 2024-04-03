from multiprocessing import set_start_method
# set_start_method('fork') # 修改启动进程的方式 'forkserver' 'fork'
set_start_method("spawn", force=True)
from fastapi import FastAPI
from nicegui import app as gui, ui
from routers import test
from utils import head, header, footer

gui.include_router(test.router)

@ui.page('/')
def root():
    head.add_head_html()
    header.create_header()
    footer.create_footer()

    # NOTE 深色模式将为每个用户在标签页和服务器重启之间保持持久
    ui.dark_mode().bind_value(gui.storage.user, 'dark_mode')
    ui.checkbox('dark mode').bind_value(gui.storage.user, 'dark_mode')

app = FastAPI()

ui.run_with(
    app,
    mount_path='/',  # NOTE 如果你希望传递给 `@ui.page` 的路径位于根目录，这个可以省略
    storage_secret='在这里选择你的私人密钥',  # NOTE 设置密钥是可选的，但允许每个用户进行持久存储。
    on_air=True,
    # native=True,
)
