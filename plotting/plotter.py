from bokeh.embed import components
from bokeh.models import AjaxDataSource
from bokeh.plotting import figure

def make_ajax_plots(request, sensor):
    plots = []
    plots.append(make_temperature_plot(request, sensor["temp"]))
    ## ovdje ubacite humidty sensor plot (make_humidity_plot)
    return plots

def make_temperature_plot(request, sensor):
    source = AjaxDataSource(data_url=request.url_root + 'temp_data',
                            polling_interval=2000, mode='append')

    source.data = dict(y=[sensor.get_temp()], x=[0])

    plot = figure(height=100, sizing_mode='scale_width')
    plot.line('x', 'y', source=source, line_width=4, color='navy', alpha=0.5)

    script, div = components(plot)
    return script, div

## sve napravite po uzoru na make_temperature_plot
## promijenite ime funkcije i ubacite drugi senzor kao parametar, putanju za podatke (data_url)
## možda boju linije?
def make_humidity_plot(request, sensor):
    pass