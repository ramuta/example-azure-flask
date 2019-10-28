import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def get_header():
    header = html.Div([

        html.Div([
            html.H1(
                'Dash Boiler Plate')
        ], className="twelve columns padded"),       

    ], className="row gs-header gs-text-header")
    return header

def get_menu():
    menu = html.Div([

        dcc.Link('Home   ', href='/', className="p-2 text-dark"),
        dcc.Link('Line Chart   ', href='/linechart', className="p-2 text-dark"),
        dcc.Link('Bar Chart   ', href='/barchart', className="p-2 text-dark"),
        dcc.Link('Scatterplot    ', href='/scatterplot', className="p-2 text-dark"),

    ], className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm")
    return menu    