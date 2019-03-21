from src.base_chart import BaseChart

import json
import pygal

class HostProgressChart(BaseChart):

    def __init__(self, **kwargs):
        self.output = 'asset/host.png'
        self.title = 'Perolahan Medali Emas Tuan Rumah Asian Games 10 Acara Terakhir'
        custom_css = '''
        {{ id }} .title .legends {
            font-size: 16px;
        }
        {{ id }} .plot_title {
            font-weight: bold;
            font-size: 20px !important;
        }
        '''
        custom_css_file = '/tmp/pygal_custom_style.css'
        with open(custom_css_file, 'w') as f:
            f.write(custom_css)
        self.config = pygal.Config(fill=False)
        self.config.css.append('file://' + custom_css_file)
        super().__init__(**kwargs)


    def filter(self, filter_config):
        '''
        Filter by changing the data in shown_data
        according to filter_config
        '''
        pass

    def draw(self):

        self.chart = pygal.Line(self.config, style=self.style, margin_bottom=50, legend_at_bottom=True, legend_at_bottom_columns=4)
        self.chart.title = self.title
        self.chart.x_title = "Tahun Event"
        self.chart.y_title = "Jumlah Medali Emas"

        # draw using the json data
        years, hosts = [], []
        for event in self.shown_data:
            years.append(event['Tahun'])
            hosts.append(event['Tuan Rumah'])

        golds = {}
        for country in set(hosts):
            golds[country] = []

        for index, event in enumerate(self.shown_data):
            for country_progress in event['Data']:
                country_name = country_progress['Negara']
                if country_name in hosts:
                    gold = int(country_progress['Emas'])
                    radius = 4 if country_name == hosts[index] else 0
                    golds[country_name].append({'value': gold, 'node': {'r': radius}})

        self.chart.x_labels = years
        for country in sorted(set(hosts)):
            self.chart.add(country, golds[country], stroke_style={'width': 2})

    def draw2(self):
        self.output = 'asset/host2.png'

        self.chart = pygal.Line(style=self.style, show_legend=False)
        self.chart.title = self.title
        self.chart.x_title = "Tahun Acara"
        self.chart.y_title = "Jumlah Medali Emas"

        # draw using the json data
        years, hosts, host_golds = [], [], []
        for event in self.shown_data:
            years.append(event['Tahun'])
            hosts.append(event['Tuan Rumah'])

        golds = {}
        for country in set(hosts):
            golds[country] = []

        for index, event in enumerate(self.shown_data):
            for country_progress in event['Data']:
                country_name = country_progress['Negara']
                if country_name in hosts:
                    gold = int(country_progress['Emas'])
                    golds[country_name].append(gold)
                    if country_name == hosts[index]:
                        host_golds.append(gold)

        self.chart.x_labels = years
        for country in sorted(set(hosts)):
            self.chart.add(country, golds[country], show_dots=False, stroke_style={'width': 2})
        self.chart.add('Host %s' % country, host_golds, dots_size=4, stroke=False)

    def render_to_png(self):
        self.chart.render_to_png(self.output)


    def render(self):
        return self.chart.render_data_uri()