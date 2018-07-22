from bokeh.plotting import figure
from bokeh.models import RangeTool, ColumnarDataSource
from bokeh.layouts import column

from datetime import datetime

class Dashboard:
    def __init__(self, data):
        self._data = data
    
    def init_componets(self):
        ''' 
            init of components, must be done in a seperate function.

            On load of page, a standard document is offerd to the renderer function,
            the components created in this function are
        '''

        dates = [datetime(2017,1,1), datetime(2018,1,1)]
        
        self.main_vw = figure(
            name='main_view',
            sizing_mode='scale_width',
            plot_height=100, plot_width=500,
            x_axis_type="datetime", x_range=(dates[0], dates[1])
        )

        self.select_vw = figure(
            name='select_view',
            sizing_mode='scale_width',
            plot_height=100, plot_width=500,
            x_axis_type="datetime", y_axis_type=None,
            tools="", toolbar_location=None 
        )

        range_rool = RangeTool(x_range=self.main_vw.x_range)
        range_rool.overlay.fill_color = "navy"
        range_rool.overlay.fill_alpha = 0.2

        self.select_vw.ygrid.grid_line_color = None
        self.select_vw.add_tools(range_rool)
        self.select_vw.toolbar.active_multi = range_rool

    def render(self, doc):
        ''' 
            renderer function, attaches dashboard specific instanes to the root
            of the document
        '''
        self.init_componets()
        doc.add_root(self.main_vw)
        doc.add_root(self.select_vw)


        return doc
    