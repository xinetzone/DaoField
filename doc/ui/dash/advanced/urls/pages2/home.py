from dash import Input, Output, State, callback, dcc, html, register_page

register_page(__name__, "/")

TRANSLATIONS = {
    "en": {
        "title": "Hello world",
        "subtitle": "This is the home page.",
        "country": "Country",
        "year": "Year",
    },
    "fr": {
        "title": "Bonjour le monde",
        "subtitle": "Ceci est la page d'accueil.",
        "country": "Pays",
        "year": "Année",
    }
}

def layout(language: str = "en", **_kwargs):
    """Home page layout

    It takes in a keyword arguments defined in `routing_callback_inputs`:
    * language (input coming from the language dropdown), it triggers re-render
    """
    default_country = "USA"
    default_year = 2020

    return [
        html.H1(TRANSLATIONS.get(language, {}).get("title")),
        html.H2(TRANSLATIONS.get(language, {}).get("subtitle")),
        html.Div(
            [
                dcc.Dropdown(
                    id={"type": "control", "id": "country"},
                    value=default_country,
                    options=["France", "USA", "Canada"],
                    style={"minWidth": 200},
                ),
                dcc.Dropdown(
                    id={"type": "control", "id": "year"},
                    value=default_year,
                    options=[{"label": str(y), "value": y} for y in range(1980, 2021)],
                    style={"minWidth": 200},
                ),
            ],
            style={"display": "flex", "gap": "1rem", "marginBottom": "2rem"},
        ),
        html.Div(contents(language, country=default_country, year=default_year), id="contents")
    ]

def contents(language: str, country: str, year: int, **_kwargs):
    lang = TRANSLATIONS.get(language, {})
    return f"{lang.get('country')}: {country}, {lang.get('year')}: {year}"


@callback(
    Output("contents", "children"),
    Input({"type": "control", "id": "country"}, "value"),
    Input({"type": "control", "id": "year"}, "value"),
    # NOTE: no need to make language an input here as the whole page will
    # re-render if language changes
    State("language", "value"),
    prevent_initial_call=True,
)
def update_contents(country, year, language):
    """Update the contents when the dropdowns are updated."""
    return contents(language, country, year)