from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers import FunctionHandler, DirectoryHandler
from bokeh.server.server import IOLoop
from src.models import CustomHandler
from src.dashboard.dashboard import Dashboard
from os.path import join, realpath, dirname


if __name__ == '__main__':

    instance = Dashboard([])
    
    dir_path = dirname(realpath(__file__))
    ch = CustomHandler(
        callback_function=instance.render,
        template_path=join(dir_path, 'src', 'dashboard', 'template', 'index.html'),
        static_path=join(dir_path, 'src', 'dashboard', 'static')
    )
    
    app = Application(ch)

    server = Server(
        app,
        port=8080)

    server.run_until_shutdown()