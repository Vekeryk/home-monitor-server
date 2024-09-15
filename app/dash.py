import dash
import plotly.express as px
import dash.dependencies as dd
from dash import html, dcc
from datetime import datetime, timedelta
from .utils import fetch_measurement


def init_dash(server):
    dash_app = dash.Dash(__name__, server=server,
                         url_base_pathname='/dashboard/')
    dash_app.layout = serve_layout

    @dash_app.callback(
        dd.Output('page-content', 'children'),
        [dd.Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/dashboard/today':
            start_time = datetime.now() - timedelta(days=1)
            return get_graph(start_time, "Today's Data")
        elif pathname == '/dashboard/week':
            start_time = datetime.now() - timedelta(days=7)
            return get_graph(start_time, "Last Week Data")
        elif pathname == '/dashboard/month':
            start_time = datetime.now() - timedelta(days=30)
            return get_graph(start_time, "Last Month Data")
        elif pathname == '/dashboard/all':
            return get_graph(None, "All Data")
        else:
            return html.Div([
                html.H1("Welcome to HomeMonitor Dashboard"),
                html.P("Please select a time period:"),
                html.Ul([
                    html.Li(html.A("Today", href="/dashboard/today")),
                    html.Li(html.A("Last Week", href="/dashboard/week")),
                    html.Li(html.A("Last Month", href="/dashboard/month")),
                    html.Li(html.A("All", href="/dashboard/all")),
                ])
            ])


def serve_layout():
    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])


def get_graph(start_time, header):
    df = fetch_measurement(start_time)

    fig_temp = px.line(df, x='timestamp', y='temperature',
                       title='Temperature Over Time', markers=True, text='temperature')
    fig_temp.update_traces(textposition='top center', textfont_size=12)

    fig_humidity = px.line(df, x='timestamp', y='humidity',
                           title='Humidity Over Time', markers=True, text='humidity')
    fig_humidity.update_traces(textposition='top center', textfont_size=12)

    fig_co2 = px.line(df, x='timestamp', y='co2',
                      title='CO2 Over Time', markers=True, text='co2')
    fig_co2.update_traces(textposition='top center', textfont_size=12)

    return html.Div([
        html.H1(children=header, style={"text-align": "center"}),
        dcc.Graph(id='temperature-graph', figure=fig_temp),
        dcc.Graph(id='humidity-graph', figure=fig_humidity),
        dcc.Graph(id='co2-graph', figure=fig_co2)
    ])
