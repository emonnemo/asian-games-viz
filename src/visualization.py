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
        self.title = 'Indonesia progress medal'
        super().__init__(**kwargs)


    def filter(self, filter_config):
        '''
        Filter by changing the data in shown_data
        according to filter_config
        '''
        pass

    
    def draw(self):
        self.chart = pygal.StackedLine(fill=True, style=self.style)
        self.chart.title = self.title

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


if __name__ == '__main__':
    # basic style
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
    indonesia_progress_chart.render_to_png()

