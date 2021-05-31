import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
import sqlalchemy
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

conn = sqlalchemy.create_engine('mysql+pymysql://root:admin@mysql:3306/richest_people')
richest = pd.read_sql_table('richest', conn)

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

fig = px.line(richest, x="Ranking", y="Net_Worth_in_Billion_USD", title='Net Worth for 100 Richest people (2019)', labels={'Net_Worth_in_Billion_USD':'Net Worth (Billion USD)'})

app.layout = html.Div(children=[
    html.H1('DATA ANALYTICS WITH CONTAINERS'),

    html.Div(children='''
        Dash app
    '''),

    dcc.Graph(
        id='graph-line',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True, port=8050)