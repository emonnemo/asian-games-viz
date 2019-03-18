from flask import Flask
from flask import render_template
from pygal.style import Style
from src.visualization import IndonesiaProgressChart
import json
app = Flask(__name__, template_folder='../templates/')


@app.route('/')
def home():
    # Style
    custom_style = Style(
        background='transparent',
        plot_background='transparent',
        foreground='#53E89B',
        foreground_strong='#53A0E8',
        foreground_subtle='#630C0D',
        opacity='.6',
        opacity_hover='.9',
        transition='400ms ease-in',
        colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'),
    )

    # indonesia progress chart
    with open('data/indonesia_progress.json') as json_file:
        data = json.load(json_file)

    indonesia_progress_chart = IndonesiaProgressChart(data=data, style=custom_style)
    indonesia_progress_chart.draw()
    chart = indonesia_progress_chart.render()

    return render_template('index.html', indonesia_progress_chart=chart) 
