import dash
import dash_core_components as dcc
import dash_html_components as html

print(dcc.__version__) # 0.6.0 or above is required

app = dash.Dash()

server = app.server
app.config.suppress_callback_exceptions = True

# if __name__ == '__main__':
#     app.run_server(debug=True)