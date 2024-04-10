# NiceGUI 运行 JavaScript

此函数在浏览器中执行页面上的任意 JavaScript 代码。在该函数被调用之前，客户端必须连接。要通过 ID 访问客户端对象，请使用 JavaScript 函数 `getElement()`。

如果等待该函数，将返回 JavaScript 代码的结果。否则，将执行 JavaScript 代码，无需等待响应。

参数：
- `code`: 要运行的 JavaScript 代码
- `timeout`: 超时时间（秒）（默认值：`1.0`）
- `check_interval`: 检查响应的时间间隔（秒）（默认值：`0.01`）
- 返回值：可等待的 `AwaitableResponse`，可以等待以获取 JavaScript 代码的结果

```python
from nicegui import ui

def alert():
    ui.run_javascript('alert("Hello!")')

async def get_date():
    time = await ui.run_javascript('Date()')
    ui.notify(f'Browser time: {time}')

def access_elements():
    ui.run_javascript(f'getElement({label.id}).innerText += " Hello!"')

ui.button('fire and forget', on_click=alert)
ui.button('receive result', on_click=get_date)
ui.button('access elements', on_click=access_elements)
label = ui.label()

# ui.run()
```

## NiceGUI 运行异步 JavaScript

使用 `run_javascript`，您还可以在浏览器中运行异步代码。以下演示展示了如何获取用户的当前位置。

```python
from nicegui import ui

async def show_location():
    response = await ui.run_javascript('''
        return await new Promise((resolve, reject) => {
            if (!navigator.geolocation) {
                reject(new Error('Geolocation is not supported by your browser'));
            } else {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        resolve({
                            latitude: position.coords.latitude,
                            longitude: position.coords.longitude,
                        });
                    },
                    () => {
                        reject(new Error('Unable to retrieve your location'));
                    }
                );
            }
        });
    ''', timeout=5.0)
    ui.notify(f'Your location is {response["latitude"]}, {response["longitude"]}')

ui.button('Show location', on_click=show_location)

# ui.run()
```
