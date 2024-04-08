from dash.dependencies import Input, Output
from dash import dcc, html
import pandas as pd
import json

import plotly.express as px
from sanstyle.github.file import lfs_url

from app import app
import dash
dash.register_page(__name__)
url = lfs_url('SanstyleLab/plotly-dastsets',
              'gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


df = pd.read_csv(url)

available_countries = df['country'].unique()
layout = html.Div([
    dcc.Graph(
        id='clientside-graph-px'
    ),
    dcc.Store(
        id='clientside-figure-store-px'
    ),
    'Indicator',
    dcc.Dropdown(
        id='clientside-graph-indicator-px',
        options=[
            {'label': 'Population', 'value': 'pop'},
            {'label': 'Life Expectancy', 'value': 'lifeExp'},
            {'label': 'GDP per Capita', 'value': 'gdpPercap'}
        ],
        value='pop'
    ),
    'Country',
    dcc.Dropdown(
        id='clientside-graph-country-px',
        options=[
            {'label': country, 'value': country}
            for country in available_countries
        ],
        value='Canada'
    ),
    'Graph scale',
    dcc.RadioItems(
        id='clientside-graph-scale-px',
        options=[
            {'label': x, 'value': x} for x in ['linear', 'log']
        ],
        value='linear'
    ),
    html.Hr(),
    html.Details([
        html.Summary('Contents of figure storage'),
        dcc.Markdown(
            id='clientside-figure-json-px'
        )
    ])
])


@app.callback(
    Output('clientside-figure-store-px', 'data'),
    Input('clientside-graph-indicator-px', 'value'),
    Input('clientside-graph-country-px', 'value')
)
def update_store_data(indicator, country):
    dff = df[df['country'] == country]
    return px.scatter(dff, x='year', y=str(indicator))


app.clientside_callback(
    """
    function(figure, scale) {
        if(figure === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign({}, figure, {
            'layout': {
                ...figure.layout,
                'yaxis': {
                    ...figure.layout.yaxis, type: scale
                }
             }
        });
        return fig;
    }
    """,
    Output('clientside-graph-px', 'figure'),
    Input('clientside-figure-store-px', 'data'),
    Input('clientside-graph-scale-px', 'value')
)


@app.callback(
    Output('clientside-figure-json-px', 'children'),
    Input('clientside-figure-store-px', 'data')
)
def generated_px_figure_json(data):
    return '```\n'+json.dumps(data, indent=2)+'\n```'
