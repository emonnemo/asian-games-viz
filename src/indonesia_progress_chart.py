from src.base_chart import BaseChart

import json
import pygal

class IndonesiaProgressChart(BaseChart):


    def __init__(self, **kwargs):
        self.output = 'asset/indonesia-progress.png'
        self.title = 'Perolehan Medali Indonesia di 10 Event Terakhir'
        custom_css = '''
        {{ id }} .title .legends {
            font-size: 12px;
        }
        {{ id }} .plot_title {
            font-weight: bold;
            font-size: 16px;
        }
        '''
        custom_css_file = '/tmp/pygal_custom_style.css'
        with open(custom_css_file, 'w') as f:
            f.write(custom_css)
        self.config = pygal.Config(fill=True, interpolate='hermite')
        self.config.css.append('file://' + custom_css_file)
        super().__init__(**kwargs)


    def filter(self, filter_config):
        '''
        Filter by changing the data in shown_data
        according to filter_config
        '''
        pass

    
    def draw(self):
        self.chart = pygal.StackedLine(self.config, fill=True, style=self.style, dots_size=0, legend_at_bottom=True, legend_at_bottom_columns=3)
        self.chart.title = self.title
        self.chart.x_title = "Tahun Event"
        self.chart.y_title = "Jumlah Medali"

        # draw using the json data
        years, golds, silvers, bronzes, ranks = [], [], [], [], []
        for yearly_medal in self.shown_data:
            years.append(int(yearly_medal['Tahun']))
            medals = yearly_medal['Data']
            golds.append(int(medals['Emas']))
            silvers.append(int(medals['Perak']))
            bronzes.append(int(medals['Perunggu']))
            ranks.append(int(medals['Peringkat']))

        self.chart.x_labels = years
        self.chart.add('Emas', golds)
        self.chart.add('Perak', silvers)
        self.chart.add('Perunggu', bronzes)

    
    def draw2(self):
        custom_css_file = '/tmp/pygal_custom_style.css'
        self.config = pygal.Config(fill=True)
        self.config.css.append('file://' + custom_css_file)
        self.chart = pygal.StackedLine(self.config, fill=True, style=self.style, dots_size=0, legend_at_bottom=True, legend_at_bottom_columns=3)
        self.chart.title = self.title
        self.chart.x_title = "Tahun Event"
        self.chart.y_title = "Jumlah Medali"

        # draw using the json data
        years, golds, silvers, bronzes, ranks = [], [], [], [], []
        for yearly_medal in self.shown_data:
            years.append(int(yearly_medal['Tahun']))
            medals = yearly_medal['Data']
            golds.append(int(medals['Emas']))
            silvers.append(int(medals['Perak']))
            bronzes.append(int(medals['Perunggu']))
            ranks.append(int(medals['Peringkat']))

        self.chart.x_labels = years
        self.chart.add('Emas', golds)
        self.chart.add('Perak', silvers)
        self.chart.add('Perunggu', bronzes)


    def render_to_png(self):
        self.chart.render_to_png(self.output)


    def render(self):
        return self.chart.render_data_uri()