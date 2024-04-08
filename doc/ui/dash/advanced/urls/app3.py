from dash import Dash, Input, Output, State, callback, dcc, html, page_container

app = Dash(
   __name__,
   use_pages=True,
   routing_callback_inputs={
        # The app state is serialised in the URL hash without refreshing the page
        # This URL can be copied and then parsed on page load
        "state": State("main-url", "hash"),
   },
   pages_folder="pages3"
)

app.layout = html.Div(
    [
        dcc.Location(id="main-url"),
        html.Div(
            html.Div("My app", style={"fontWeight": "bold"}),
            style={"background": "#CCC", "padding": 10, "marginBottom": 20},
        ),
        page_container,
    ],
    style={"fontFamily": "sans-serif"}
)

if __name__ == "__main__":
    app.run(debug=True)