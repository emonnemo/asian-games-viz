from abc import ABC
from abc import abstractmethod
from pygal.style import Style

import json
import pygal

class BaseChart(ABC):
    '''
    Base abstract class for charts
    '''

    def __init__(self, data, style=None):
        self.data = data
        self.shown_data = data
        self.style = style


    @abstractmethod
    def filter(self, filter_config):
        pass


    def reset(self):
        self.shown_data = data


    @abstractmethod
    def draw(self):
        return NotImplementedError

    
    @abstractmethod
    def render_to_png(self):
        return NotImplementedError


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
        background='white',
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
        background='white',
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

    with open('data/indonesia_2018.json') as json_file:
        sports_2018_data = json.load(json_file)

    indonesia_progress_chart = IndonesiaProgressChart(data=data, style=indonesia_progress_style)
    indonesia_progress_chart.draw()
    indonesia_progress_chart.render_to_png()

    indonesia_2018_sports_chart = IndonesiaSports2018Chart(data=sports_2018_data, style=sports_style)
    indonesia_2018_sports_chart.draw()
    indonesia_2018_sports_chart.render_to_png()

    # host progress chart
    with open('data/asia_medal.json') as json_file:
        asia_progress_data = json.load(json_file)

    host_progress_chart = HostProgressChart(data=asia_progress_data, style=host_style)
    host_progress_chart.draw()
    host_progress_chart.render_to_png()

    host_progress_chart2 = HostProgressChart(data=asia_progress_data, style=host_style2)
    host_progress_chart2.draw2()
    host_progress_chart2.render_to_png()
