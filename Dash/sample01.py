
import dash
from dash import dcc
from dash import html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': '佐藤', 'value': 'satou'},
            {'label': '鈴木', 'value': 'suzuki'},
            {'label': '田中', 'value': 'tanaka'}
        ],
        value='suzuki'
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': '佐藤', 'value': 'satou'},
            {'label': '鈴木', 'value': 'suzuki'},
            {'label': '田中', 'value': 'tanaka'}
        ],
        value=['satou', 'suzuki'],
        multi=True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': '佐藤', 'value': 'satou'},
            {'label': '鈴木', 'value': 'suzuki'},
            {'label': '田中', 'value': 'tanaka'}
        ],
        value='suzuki'
    ),

    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': '佐藤', 'value': 'satou'},
            {'label': '鈴木', 'value': 'suzuki'},
            {'label': '田中', 'value': 'tanaka'}
        ],
        value=['suzuki', 'tanaka']
    ),

    html.Label('Text input'),
    dcc.Input(value='佐藤', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=5,
        marks={i: str(i) for i in range(1,6)},
        value=3
    )


], style={'columnCount': 2})

if __name__ == '__main__':
    app.run_server(debug=True)
