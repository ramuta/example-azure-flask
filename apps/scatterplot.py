import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from apps import commonmodules

from app import app
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_menu(),      
    html.H3('Scatter Chart'),    
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x = random_x,
                    y = random_y,
                    mode = 'markers',
                   
                )                
            ],
        }
    )
  
])
