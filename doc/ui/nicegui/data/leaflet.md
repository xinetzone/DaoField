# {func}`~nicegui.ui.leaflet` Leaflet 地图

这个元素是[Leaflet](https://leafletjs.com/) JavaScript库的包装器。

- `center`: 地图的初始中心位置（纬度/经度，默认值：`(0.0, 0.0)`）
- `zoom`: 地图的初始缩放级别（默认值：`13`）
- `draw_control`: 是否显示绘图工具栏（默认值：`False`）
- `options`: 传递给Leaflet地图的其他选项（默认值：`{}`）

```python
from nicegui import ui

m = ui.leaflet(center=(51.505, -0.09))
ui.label().bind_text_from(m, 'center', lambda center: f'Center: {center[0]:.3f}, {center[1]:.3f}')
ui.label().bind_text_from(m, 'zoom', lambda zoom: f'Zoom: {zoom}')

with ui.grid(columns=2):
    ui.button('London', on_click=lambda: m.set_center((51.505, -0.090)))
    ui.button('Berlin', on_click=lambda: m.set_center((52.520, 13.405)))
    ui.button(icon='zoom_in', on_click=lambda: m.set_zoom(m.zoom + 1))
    ui.button(icon='zoom_out', on_click=lambda: m.set_zoom(m.zoom - 1))

# ui.run()
```

## {func}`~nicegui.ui.leaflet` 想更改地图样式

默认的地图样式是OpenStreetMap。您可以在 <https://leaflet-extras.github.io/leaflet-providers/preview/> 找到更多的地图样式。每次调用`tile_layer`都会叠加在前面的图层上。因此，如果您想更改地图样式，必须先移除默认的样式。

```python
from nicegui import ui

m = ui.leaflet(center=(51.505, -0.090), zoom=3)
m.clear_layers()
m.tile_layer(
    url_template=r'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
    options={
        'maxZoom': 17,
        'attribution':
            'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | '
            'Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
    },
)

# ui.run()
```

## {func}`~nicegui.ui.leaflet` 添加标记

您可以使用`marker`在地图上添加标记。`center`参数是一个包含纬度和经度的元组。这个演示通过点击地图来添加标记。请注意，`"map-click"`事件是指地图对象的点击事件，而`"click"`事件是指容器`div`的点击事件。

```python
from nicegui import events, ui

m = ui.leaflet(center=(51.505, -0.09))

def handle_click(e: events.GenericEventArguments):
    lat = e.args['latlng']['lat']
    lng = e.args['latlng']['lng']
    m.marker(latlng=(lat, lng))
m.on('map-click', handle_click)

# ui.run()
```

## {func}`~nicegui.ui.leaflet` 移到标记

您可以使用`move`方法移动标记。

```python
from nicegui import ui

m = ui.leaflet(center=(51.505, -0.09))
marker = m.marker(latlng=m.center)
ui.button('Move marker', on_click=lambda: marker.move(51.51, -0.09))

# ui.run()
```

## {func}`~nicegui.ui.leaflet` 矢量图层

Leaflet支持一系列[矢量图层](https://leafletjs.com/reference.html#:~:text=VideoOverlay-,Vector%20Layers,-Path)，如圆形、多边形等。这些可以使用`generic_layer`方法添加。我们欢迎任何关于添加更多特定图层以简化使用的`pull`请求。

```python
from nicegui import ui

m = ui.leaflet(center=(51.505, -0.09)).classes('h-32')
m.generic_layer(name='circle', args=[m.center, {'color': 'red', 'radius': 300}])

# ui.run()
```

## {func}`~nicegui.ui.leaflet` 禁用平移和缩放

Leaflet中有多种选项可以[配置地图](https://leafletjs.com/reference.html#map)。这个演示禁用了平移和缩放控件。

```python
from nicegui import ui

options = {
    'zoomControl': False,
    'scrollWheelZoom': False,
    'doubleClickZoom': False,
    'boxZoom': False,
    'keyboard': False,
    'dragging': False,
}
ui.leaflet(center=(51.505, -0.09), options=options)

# ui.run()
```

## {func}`~nicegui.ui.leaflet` 在地图上绘制

您可以启用一个工具栏在地图上绘制。可以使用`draw_control`配置工具栏。这个演示通过点击地图添加标记和多边形。

```python
from nicegui import events, ui

def handle_draw(e: events.GenericEventArguments):
    if e.args['layerType'] == 'marker':
        m.marker(latlng=(e.args['layer']['_latlng']['lat'],
                         e.args['layer']['_latlng']['lng']))
    if e.args['layerType'] == 'polygon':
        m.generic_layer(name='polygon', args=[e.args['layer']['_latlngs']])

draw_control = {
    'draw': {
        'polygon': True,
        'marker': True,
        'circle': False,
        'rectangle': False,
        'polyline': False,
        'circlemarker': False,
    },
    'edit': False,
}
m = ui.leaflet(center=(51.505, -0.09), zoom=13, draw_control=draw_control)
m.on('draw:created', handle_draw)

# ui.run()
```

## {func}`~nicegui.ui.leaflet` 运行地图方法

您可以使用`run_map_method`方法运行Leaflet地图对象的方法。这个演示展示了如何将地图适配到整个世界。

```python
from nicegui import ui

m = ui.leaflet(center=(51.505, -0.09)).classes('h-32')
ui.button('Fit world', on_click=lambda: m.run_map_method('fitWorld'))

# ui.run()
```

## {func}`~nicegui.ui.leaflet` 运行地图图层

您可以使用`run_layer_method`方法运行Leaflet图层对象的方法。这个演示展示了如何更改标记的透明度或更改其图标。

```python
from nicegui import ui

m = ui.leaflet(center=(51.505, -0.09)).classes('h-32')
marker = m.marker(latlng=m.center)
ui.button('Hide', on_click=lambda: marker.run_method('setOpacity', 0.3))
ui.button('Show', on_click=lambda: marker.run_method('setOpacity', 1.0))

icon = 'L.icon({iconUrl: "http://leafletjs.com/examples/custom-icons/leaf-green.png"})'
ui.button('Change icon', on_click=lambda: marker.run_method(':setIcon', icon))

# ui.run()
```

## {func}`~nicegui.ui.leaflet` 等待初始化

您可以使用`initialized`方法等待地图初始化。当您想在创建地图后立即运行像适应边界这样的方法时，这是必要的。

```python
from nicegui import ui

m = ui.leaflet(zoom=5)
central_park = m.generic_layer(name='polygon', args=[[
    (40.767809, -73.981249),
    (40.800273, -73.958291),
    (40.797011, -73.949683),
    (40.764704, -73.973741),
]])
await m.initialized()
bounds = await central_park.run_method('getBounds')
m.run_map_method('fitBounds', [[bounds['_southWest'], bounds['_northEast']]])

ui.run()
```
