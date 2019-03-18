from flask import Flask
from flask import render_template
from pygal.style import Style
from src.visualization import IndonesiaProgressChart, IndonesiaSports2018Chart, HostProgressChart
import json
app = Flask(__name__, template_folder='../templates/')


@app.route('/')
def home():
    # Style
    indonesia_progress_style = Style(
        background='transparent',
        plot_background='transparent',
        foreground='#00000',
        foreground_strong='#000000',
        #foreground_subtle='#630C0D',
        opacity='1',
        opacity_hover='.9',
        transition='400ms ease-in',
        font_family='googlefont:Roboto Slab',
        colors=('#FEE101', 'rgba(192,192,192,1)', '#AD8A56'),
    )

    sports_style = Style(
        background='white',
        plot_background='transparent',
        foreground='#000000',
        foreground_strong='rgba(0,0,0,1)',
        foreground_subtle='#630C0D',
        opacity=1,
        transition='400ms ease-in',
        font_family='googlefont:Roboto Slab',
        colors=('#FEE101', 'rgba(192,192,192,1)', '#AD8A56', 'rgba(0,0,0,0.1)'),
    )

    host_style = Style(
        background='transparent',
        plot_background='transparent',
        foreground='#000000',
        foreground_strong='#000000',
        foreground_subtle='#000000',
        opacity='1',
        opacity_hover='.9',
        transition='400ms ease-in',
        font_family='googlefont:Roboto Slab',
        colors=('#f58231', '#fabebe', '#e6194b', '#3cb44b', '#f032e6', '#4363d8', '#911eb4'),
    )

    # indonesia progress chart
    with open('data/indonesia_progress.json') as json_file:
        indonesia_progress_data = json.load(json_file)

    indonesia_progress_chart = IndonesiaProgressChart(data=indonesia_progress_data, style=indonesia_progress_style)
    indonesia_progress_chart.draw()
    indonesia_progress_chart_rendered = indonesia_progress_chart.render()

    # sports chart
    with open('data/indonesia_2018.json') as json_file:
        sports_2018_data = json.load(json_file)
    
    indonesia_2018_sports_chart = IndonesiaSports2018Chart(data=sports_2018_data, style=sports_style)
    indonesia_2018_sports_chart.draw()
    indonesia_2018_sports_chart_rendered = indonesia_2018_sports_chart.render()

    # host progress chart
    with open('data/asia_medal.json') as json_file:
        asia_progress_data = json.load(json_file)

    host_progress_chart = HostProgressChart(data=asia_progress_data, style=host_style)
    host_progress_chart.draw()
    host_progress_chart_rendered = host_progress_chart.render()

    return render_template('index.html', indonesia_progress_chart=indonesia_progress_chart_rendered, sports_chart=indonesia_2018_sports_chart_rendered, host_chart=host_progress_chart_rendered) 
