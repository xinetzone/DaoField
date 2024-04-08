from dash import Dash, Input, Output, State, callback, dcc, html, page_container

TRANSLATIONS = {
    "en": {
        "title": "My app",
    },
    "fr": {
        "title": "Mon app",
    },
}
DEFAULT_LANGUAGE = "en"

app = Dash(
   __name__,
   use_pages=True,
   routing_callback_inputs={
        # The language will be passed as a `layout` keyword argument to page layout functions
        "language": Input("language", "value"),
   },
   pages_folder="pages2"
)

app.layout = html.Div(
    [
        html.Div(
            [
                # We will need to update the title when the language changes as it is
                # rendered outside the page layout function
                html.Div(TRANSLATIONS[DEFAULT_LANGUAGE]["title"], id="app-title", style={"fontWeight": "bold"}),
                html.Div(
                    [
                        # Language dropdown
                        dcc.Dropdown(
                            id="language",
                            options=[
                                {"label": "English", "value": "en"},
                                {"label": "Français", "value": "fr"},
                            ],
                            value=DEFAULT_LANGUAGE,
                            persistence=True,
                            clearable=False,
                            searchable=False,
                            style={"minWidth": 150},
                        ),
                    ],
                    style={"marginLeft": "auto", "display": "flex", "gap": 10}
                )
            ],
            style={
                "background": "#CCC",
                "padding": 10,
                "marginBottom": 20,
                "display": "flex",
                "alignItems": "center",
            },
        ),
        page_container,
    ],
    style={"fontFamily": "sans-serif"}
)

@callback(
    Output("app-title", "children"),
    Input("language", "value"),
)
def update_main_layout_language(language: str):
    """Translate the parts of the layout outside of the pages layout functions."""
    return TRANSLATIONS.get(language, {}).get("title")

if __name__ == "__main__":
    app.run(debug=True)