import base64
import json

from dash import ALL, Input, Output, callback, html, dcc, register_page, ctx

register_page(__name__, "/", title="Home")

def layout(state: str = None, **_kwargs):
    """Home page layout

    It takes in a keyword arguments defined in `routing_callback_inputs`:
    * state (serialised state in the URL hash), it does not trigger re-render
    """

    # Define default state values
    defaults = {"country": "France", "year": 2020}
    # Decode the state from the hash
    state = defaults | (json.loads(base64.b64decode(state)) if state else {})

    return [
        html.H1("Hello world"),
        html.H2("This is the home page."),
        html.Div(
            [
                dcc.Dropdown(
                    id={"type": "control", "id": "country"},
                    value=state.get("country"),
                    options=["France", "USA", "Canada"],
                    style={"minWidth": 200},
                ),
                dcc.Dropdown(
                    id={"type": "control", "id": "year"},
                    value=state.get("year"),
                    options=[{"label": str(y), "value": y} for y in range(1980, 2021)],
                    style={"minWidth": 200},
                ),
            ],
            style={"display": "flex", "gap": "1rem", "marginBottom": "2rem"},
        ),
        html.Div(contents(**state), id="contents")
    ]

def contents(country: str, year: int, **_kwargs):
    return f"Country: {country}, Year: {year}"

@callback(
    Output("main-url", "hash", allow_duplicate=True),
    Input({"type": "control", "id": ALL}, "value"),
    prevent_initial_call=True,
)
def update_hash(_values):
    """Update the hash in the URL Location component to represent the app state.

    The app state is json serialised then base64 encoded and is treated with the
    reverse process in the layout function.
    """
    return "#" + base64.b64encode(
        json.dumps({inp["id"]["id"]: inp["value"] for inp in ctx.inputs_list[0]})
        .encode("utf-8")
    ).decode("utf-8")

@callback(
    Output("contents", "children"),
    Input({"type": "control", "id": "country"}, "value"),
    Input({"type": "control", "id": "year"}, "value"),
    prevent_initial_call=True,
)
def update_contents(country, year):
    """Update the contents when the dropdowns are updated."""
    return contents(country, year)