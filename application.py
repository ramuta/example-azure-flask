import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import linechart, barchart, home , scatterplot


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return home.layout
    elif pathname == '/linechart':
         return linechart.layout
    elif pathname == '/barchart':
         return barchart.layout
    elif pathname == '/scatterplot':
         return scatterplot.layout
    else:
        return '404'

external_css = ["hhttps://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]
                
if __name__ == '__main__':
    app.run_server(debug=True)