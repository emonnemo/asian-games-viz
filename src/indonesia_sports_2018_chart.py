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
        average_medals, remainders, deficits = [], [], []
        

        for sports in self.shown_data:
            sport = sports['Data']
            sport_name = sports['Cabor']

            total_year = 9
            last_event = 0
            total = 0

            #Iterate all medals indonesia won over the years
            for year in sport:
                medali = year['Medali']

                gold = int(medali.get('Emas', 0))
                silver = int(medali.get('Perak', 0))
                bronze = int(medali.get('Perunggu', 0))
                
                # Only select 10 last event and seperate the last event
                if int(year.get('Tahun', 0)) != 2018 and int(year.get('Tahun', 0)) >= 1982:
                    total += gold + silver + bronze
                elif int(year.get('Tahun', 0)) == 2018:
                    last_event = gold + silver + bronze

            average_medal = (total / total_year)
            
            remainder = 0
            deficit = 0

            if last_event > average_medal :
                remainder = last_event - average_medal
            else :
                deficit = average_medal - last_event
                average_medal -= deficit
            
            total_bar = average_medal + remainder 

            # Sort the list
            idx = 0
            while idx < len(average_medals):
                cur_remainder = remainders[idx]
                cur_deficit = deficits[idx]
                if average_medals[idx] + cur_deficit + cur_remainder < total_bar:
                    idx += 1
                else:
                    break

            #Insert into list
            if (average_medal+remainder > 0) :
                sport_names.insert(idx, sport_name)
                average_medals.insert(idx, average_medal)
                remainders.insert(idx, remainder)
                deficits.insert(idx, deficit)
        
        return average_medals, remainders, deficits, sport_names

    
    def draw(self):

        self.chart = pygal.HorizontalStackedBar(self.config, style=self.style, fill=True, legend_at_bottom=True, legend_at_bottom_columns=4)
        self.chart.title = self.title

        self.chart.x_title = "Persentase Medali"

        average_medal, remainders, deficits, sport_names = self.fill_data()

        self.chart.x_labels = sport_names

        self.chart.add("Rata-rata perolehan medali", average_medal)
        self.chart.add("Perbedaan", remainders)
        self.chart.add("Defisit", deficits)
        


    def render_to_png(self):
        self.chart.render_to_png(self.output)


    def render(self):
        return self.chart.render_data_uri()