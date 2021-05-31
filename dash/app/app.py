import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import flask
import sqlalchemy
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

conn = sqlalchemy.create_engine('mysql+pymysql://root:admin@mysql:3306/richest_people')
richest = pd.read_sql_table('richest', conn)

def generate_table(dataframe, max_rows=100):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns]) ] +
        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True


countPerCountry = richest.groupby(richest['Country']).size()

fig = px.line(richest, x="Ranking", y="Net_Worth_in_Billion_USD", title='Net Worth for 100 Richest people (2019)', labels={'Net_Worth_in_Billion_USD':'Net Worth (Billion USD)'})
fig2 = px.pie(values = countPerCountry.values, names = countPerCountry.index, title='Percent of richest people by country')
fig3 = px.bar(x = countPerCountry.index, y = countPerCountry.values, title='Number of richest people by country', labels={'x':'Countries', 'y':'Number of people'})


app.layout = html.Div(children=[
    
    html.Div([
    html.H1('DATA ANALYTICS WITH CONTAINERS'),
    html.Div(
        html.P('Container-based data analytics development solution: Visualizations of a database with a data source (The 100 richest people in the year 2019) using the Dash application.'))
    ]),

    html.Div(generate_table(richest)),

    html.Div([
    html.H2('VISUALIZATIONS'),
        html.Div([
            html.P('The following graphical visualization (line graph) represents the relationship between the ranking of the 100 richest people in 2019 and their net worth (Billion USD):'),
            dcc.Graph(
            id='line-graph',
            figure=fig)
        ]),
        
        html.Div([
            html.P('The following graphical visualization (pie graph) represents the percentage of the number of rich people (The 100 richest people in 2019) by country:'),
            dcc.Graph(
            id='pie-graph',
            figure=fig2)
        ]),
        
        html.Div([
            html.P('The following graphical visualization (bar graph) represents the number of rich people (The 100 richest people in 2019) by country:'),
            dcc.Graph(
            id='bar-graph',
            figure=fig3)
        ]),

        html.Br(),
        html.A('Data Analytics With Containers Github repository', href='https://github.com/fuentesDeveloper/Data-analytics-with-containers', target='_blank', style={'color': 'gray', 'fontSize': 12})
    ])
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True, port=8050)