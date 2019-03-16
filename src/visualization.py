import json
import pygal


class IndonesiaProgressChart:


    def __init__(self, data):
        self.chart = pygal.StackedLine(fill=True)
        self.output = 'asset/indonesia-progress.png'
        self.title = 'Indonesia progress medal'
        self.data = data


    def draw(self):
        self.chart.title = self.title

        # draw using the json data
        years, golds, silvers, bronzes, ranks = [], [], [], [], []
        for yearly_medal in self.data:
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
    # indonesia progress chart
    with open('data/indonesia_progress.json') as json_file:
        data = json.load(json_file)
    indonesia_progress_chart = IndonesiaProgressChart(data)
    indonesia_progress_chart.draw()
    indonesia_progress_chart.render_to_png()
#    custom_style = Style(
#        background='transparent',
#        plot_background='transparent',
#        foreground='#53E89B',
#        foreground_strong='#53A0E8',
#        foreground_subtle='#630C0D',
#        opacity='.6',
#        opacity_hover='.9',
#        transition='400ms ease-in',
#        colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))

