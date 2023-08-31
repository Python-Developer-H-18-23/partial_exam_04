from flask import Flask, render_template, request, app, jsonify
from plotting.plotter import make_ajax_plots
from sim_sensors import temp_sensor, humidity_sensor

### glavni dio zadatka se nalaži u plotting/plotter.py
### također trebate popuniti praznu funkciju u ovoj dataoteci
### sretno!

t_sensor = temp_sensor.TempSensor()

hum_sensor = humidity_sensor.HumiditySensor()

sensors = {"temp": t_sensor, "hum": hum_sensor}

app = Flask(__name__, template_folder='templates')

x1=0
x2=0

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dashboard')
def show_dashboard():
    plots = make_ajax_plots(request, sensors)
    return render_template('dashboard.html', plots=plots)

@app.route('/temp_data', methods=['POST'])
def temp_data():
    global x1
    y = t_sensor.get_temp()
    x1 += 1
    return jsonify(x=[x1], y=[y])

## po uzoru na temp_data, napravite novu rutu koja ce vracati podatke o vlagi
@app.route('/humidity_data', methods=['POST'])
def humidity_data():
    pass