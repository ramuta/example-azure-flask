import dash
import dash_core_components as dcc
import dash_html_components as html

print(dcc.__version__) # 0.6.0 or above is required

dash_app = dash.Dash()

server = dash_app.server
dash_app.config.suppress_callback_exceptions = True

# if __name__ == '__main__':
#     app.run_server(debug=True)