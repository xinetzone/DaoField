from fastapi import Request, FastAPI
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
from nicegui import Client, app as gui, ui
from .routers import test

# in reality users passwords would obviously need to be hashed
passwords = {'admin': 'admin'}

unrestricted_page_routes = {'/login'}

class AuthMiddleware(BaseHTTPMiddleware):
    """This middleware restricts access to all NiceGUI pages.

    It redirects the user to the login page if they are not authenticated.
    """

    async def dispatch(self, request: Request, call_next):
        if not gui.storage.user.get('authenticated', False):
            if request.url.path in Client.page_routes.values() and request.url.path not in unrestricted_page_routes:
                gui.storage.user['referrer_path'] = request.url.path  # remember where the user wanted to go
                return RedirectResponse('/login')
        return await call_next(request)

gui.add_middleware(AuthMiddleware)
gui.include_router(test.router)

@ui.page('/')
def main_page() -> None:
    with ui.column().classes('absolute-center items-center'):
        ui.label(f'Hello {gui.storage.user["username"]}!').classes('text-2xl')
        ui.button(on_click=lambda: (gui.storage.user.clear(), ui.navigate.to('/login')), icon='logout') \
            .props('outline round')


@ui.page('/subpage')
def test_page() -> None:
    ui.label('This is a sub page.')

@ui.page('/login')
def login() -> RedirectResponse|None:
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        if passwords.get(username.value) == password.value:
            gui.storage.user.update({'username': username.value, 'authenticated': True})
            ui.navigate.to(gui.storage.user.get('referrer_path', '/'))  # go back to where the user wanted to go
        else:
            ui.notify('Wrong username or password', color='negative')

    if gui.storage.user.get('authenticated', False):
        return RedirectResponse('/')
    with ui.card().classes('absolute-center'):
        username = ui.input('用户名').on('keydown.enter', try_login)
        password = ui.input('密码', password=True, password_toggle_button=True).on('keydown.enter', try_login)
        ui.button('登录', on_click=try_login)
    return None

app = FastAPI()

ui.run_with(
    app,
    mount_path='/',  # NOTE 如果你想让传递给 @ui.page 的路径位于根目录，则可以省略这一步
    storage_secret='pick your private secret here',  # NOTE 设置密钥是可选的，但允许每个用户进行持久存储
)
