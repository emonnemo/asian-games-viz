from src.base_chart import BaseChart

import json
import pygal

class IndonesiaSports2018Chart(BaseChart):

    def __init__(self, **kwargs):
        self.output = 'asset/sports-indonesia.png'
        self.title = 'Perolahan Medali Indonesia Per Cabang 2018'
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
        self.config = pygal.Config()
        self.config.css.append('file://' + custom_css_file)
        super().__init__(**kwargs)


    def filter(self, filter_config):
        '''
        Filter by changing the data in shown_data
        according to filter_config
        '''
        pass

    def fill_data(self):
        
        # draw using the json data
        sport_names = []
        golds, silvers, bronzes = [], [], []
        rest = []
        for sports in self.shown_data:
            sport_name = sports['Cabor']
            medals = sports['Medali']

            total = int(medals["Total Seluruh Medali"])
            gold = (int(medals['Emas']) / total) * 100
            silver = (int(medals['Perak']) / total) * 100
            bronze = (int(medals['Perunggu']) / total) * 100

            rest_medal = 100 - (gold + silver + bronze)

            idx = 0
            while idx < len(rest):
                if rest[idx] > rest_medal:
                    idx += 1
                else:
                    break
                
            sport_names.insert(idx, sport_name)
            golds.insert(idx, gold)
            silvers.insert(idx, silver)
            bronzes.insert(idx, bronze)
            rest.insert(idx, rest_medal)
        
        return golds, silvers, bronzes, rest, sport_names

    
    def draw(self):

        self.chart = pygal.HorizontalStackedBar(self.config, style=self.style, fill=True, legend_at_bottom=True, legend_at_bottom_columns=4)
        self.chart.title = self.title

        self.chart.x_title = "Persentase Medali"

        golds, silvers, bronzes, rest, sport_names = self.fill_data()

        self.chart.x_labels = sport_names
        self.chart.add('Emas', golds)
        self.chart.add('Perak', silvers)
        self.chart.add('Perunggu', bronzes)
        self.chart.add('Medali Tersisa', rest)


    def render_to_png(self):
        self.chart.render_to_png(self.output)


    def render(self):
        return self.chart.render_data_uri()