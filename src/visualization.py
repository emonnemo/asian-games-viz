from host_progress_chart import HostProgressChart
from indonesia_progress_chart import IndonesiaProgressChart
from indonesia_sports_2018_chart import IndonesiaSports2018Chart
from pygal.style import Style

import json
import pygal


if __name__ == '__main__':
    # basic style
    indonesia_progress_style = Style(
        background='transparent',
        plot_background='transparent',
        foreground='#000000',
        foreground_strong='#000000',
        #foreground_subtle='#630C0D',
        opacity='1',
        opacity_hover='.9',
        transition='400ms ease-in',
        colors=('rgba(255,223,0,1)', 'rgba(192,192,192,1)', 'rgba(205,127,50,1)', 'rgba(0,0,0,0.1)'),
    )

    sports_style = Style(
        background='transparent',
        plot_background='transparent',
        foreground='#000000',
        foreground_strong='#53A0E8',
        foreground_subtle='#630C0D',
        opacity=1,
        transition='400ms ease-in',
        colors=('rgba(255,223,0,1)', 'rgba(192,192,192,1)', 'rgba(205,127,50,1)', 'rgba(0,0,0,0.1)'),
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
        colors=('#f58231', '#fabebe', '#e6194b', '#3cb44b', '#f032e6', '#4363d8', '#911eb4'),
    )

    host_style2 = Style(
        background='transparent',
        plot_background='transparent',
        foreground='#000000',
        foreground_strong='#53A0E8',
        foreground_subtle='#630C0D',
        opacity='1',
        opacity_hover='.9',
        transition='400ms ease-in',
        colors=('#a0a0a0', '#a0a0a0', '#e6194b', '#a0a0a0', '#a0a0a0', '#a0a0a0', '#a0a0a0', '#00ff00'),
    )

    # indonesia progress chart
    with open('data/indonesia_progress.json') as json_file:
        data = json.load(json_file)

    indonesia_progress_chart = IndonesiaProgressChart(data=data, style=indonesia_progress_style)
    indonesia_progress_chart.draw()
    indonesia_progress_chart.render_to_png()

    # indonesia sports 2018 chart
    with open('data/indonesia_2018.json') as json_file:
        sports_2018_data = json.load(json_file)

    indonesia_sports_2018_chart = IndonesiaSports2018Chart(data=sports_2018_data, style=sports_style)
    indonesia_sports_2018_chart.draw()
    indonesia_sports_2018_chart.render_to_png()

    # host progress chart
    with open('data/asia_medal.json') as json_file:
        asia_progress_data = json.load(json_file)

    host_progress_chart = HostProgressChart(data=asia_progress_data, style=host_style)
    host_progress_chart.draw()
    host_progress_chart.render_to_png()

    host_progress_chart2 = HostProgressChart(data=asia_progress_data, style=host_style2)
    host_progress_chart2.draw2()
    host_progress_chart2.render_to_png()
