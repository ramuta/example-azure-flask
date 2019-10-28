import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps import barchart, barchart, commonmodules

from app import app


layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_menu(),
    html.Br(),
    html.H3('This is home screen'),
])
