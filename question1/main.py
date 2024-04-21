import plotly.graph_objects as go
from tradeAnalayzerClass import DataAnalyzer



#################################### START QUESTION 1 ####################################

class PlotOccurences(DataAnalyzer):
    def __init__(self, ticker, start_date):
        super().__init__(ticker, start_date)
        super().fetch_data()
        super().process_data()

        
    def plot_data(self):
            # Plot data
            colors = {
                '3-5%': 'rgba(255, 0, 0, 0.5)',  # Red
                '5-10%': 'rgba(0, 255, 0, 0.5)',  # Green
                'above 10%': 'rgba(0, 0, 255, 0.5)'  # Blue
            }

            fig = go.Figure()

            fig.add_trace(go.Scatter(x=self.index_data.index, y=self.index_data['Close'], mode='lines', name='SPY'))
            fig.add_trace(go.Scatter(x=self.index_data.index, y=self.sg_filter, mode='lines', name='Savitzky-Golay Filter'))
            fig.add_trace(go.Scatter(x=self.index_data.index[self.peaks], y=self.index_data['Close'][self.peaks], mode='markers', marker=dict(color='red'), name='SG Peaks'))
            fig.add_trace(go.Scatter(x=self.index_data.index[self.troughs], y=self.index_data['Close'][self.troughs], mode='markers', marker=dict(color='green'), name='SG Troughs'))

            for category, trends in self.downward_trends.items():
                for peak_idx, trough_idx in trends:
                    peak_date = self.index_data.index[peak_idx]
                    trough_date = self.index_data.index[trough_idx]
                    fig.add_trace(go.Scatter(x=[peak_date, peak_date, trough_date, trough_date, peak_date],
                                            y=[self.index_data['Close'][peak_idx], self.index_data['Close'][trough_idx], self.index_data['Close'][trough_idx], self.index_data['Close'][peak_idx], self.index_data['Close'][peak_idx]],
                                            mode='lines',
                                            fill='toself',
                                            fillcolor=colors[category],
                                            line=dict(color=colors[category], width=0),
                                            name=f'{category} Downward Trend'))

            fig.update_layout(title='SPY Stock Data with Downward Trend Groups',
                            xaxis_title='Date',
                            yaxis_title='Price',
                            showlegend=True)

            fig.show()

#################################### END QUESTION 1##########################################



#################################### START QUESTION 2 & 3####################################
import numpy as np
import pandas as pd
from scipy import stats
class ProbCorrections(DataAnalyzer):
    def __init__(self, ticker, start_date):
        super().__init__(ticker, start_date)  
        self.fetch_data()
        self.process_data()
        self.df = self.calculate()
        
    def fetch_data(self):
        super().fetch_data()  

    def process_data(self):
        super().process_data()
        
    def calculate_days_since_previous_trend_end(self):
        df = pd.DataFrame(index=self.index_data.index)

        # Initialize the new column
        df['Days_Since_Previous_Trend_End'] = np.nan

        count = 1

        # Iterate over each date
        for idx, date in enumerate(df.index):
            # Check if the count should be reset
            if idx > 0:
                # Check if the current date marks the end of a trend
                if idx in [trough[1] for trends in self.downward_trends.values() for trough in trends]:
                    count = 0  # Reset count if it's the end of a trend
                else:
                    count += 1  # Increment count otherwise

            # Assign count to the DataFrame
            df.at[date, 'Days_Since_Previous_Trend_End'] = count

        return df 
    
    def calculate_average_intervals(self, category):
        # Calculate historical intervals between corrections
        correction_dates = [self.index_data.index[trough] for peak, trough in self.downward_trends[category]]
        intervals = [(correction_dates[i] - correction_dates[i-1]).days for i in range(1, len(correction_dates))]
        return np.mean(intervals) if intervals else None

    def calculate(self):
        # Calculate historical average intervals for each category
        average_intervals = {
            '3-5%': self.calculate_average_intervals('3-5%'),
            '5-10%': self.calculate_average_intervals('5-10%'),
            'above 10%': self.calculate_average_intervals('above 10%')
        }

        # Use the existing function to get 'Days_Since_Previous_Trend_End'
        days_since_corr_df = self.calculate_days_since_previous_trend_end()

        # For each date, calculate the expected number of days until the next correction
        for category, average in average_intervals.items():
            days_since_corr_df[category] = average - days_since_corr_df['Days_Since_Previous_Trend_End']

        # Any negative values would mean a correction is overdue based on the average, set to zero as we can't predict past corrections
        days_since_corr_df[days_since_corr_df < 0] = 0

        days_since_corr_df.to_excel("output.xlsx")
        return days_since_corr_df
    
    def save_excel(self):
        file_name = "output.xlsx"
        self.days_since_corr.to_excel(file_name)
      
    def plot_data(self):
        if self.df is None:
            self.calculate()

        for category in ['3-5%', '5-10%', 'above 10%']:
            # Calculate statistics
            mean_val = self.df[category].mean()
            mode_val = stats.mode(self.df[category])[0][0]
            median_val = self.df[category].median()


            fig = go.Figure()

            # Add line plot for average days
            fig.add_trace(go.Scatter(x=self.df.index, y=self.df[category],
                                     mode='lines', name=f'Avg Days Until Next {category} Correction'))


            fig.add_trace(go.Table(
                header=dict(values=['Mean', 'Mode', 'Median'],
                            fill_color='paleturquoise',
                            align='left'),
                cells=dict(values=[[f"{mean_val:.2f}"], [f"{mode_val:.2f}"], [f"{median_val:.2f}"]],
                           fill_color='lavender',
                           align='left'),
                domain=dict(x=[0.7, 1.0], y=[0, 0.3])  
            ))


            fig.update_layout(
                title=f'Prediction of Days Until Next Correction for {category}',
                xaxis_title='Date',
                yaxis_title='Average Days Until Next Correction',
                showlegend=True,
                xaxis=dict(domain=[0, 0.65]),  
                yaxis=dict(domain=[0, 1])      
            )


            fig.show()
#################################### END QUESTION 2####################################

def plot_corrections(ticker,start_date):
    analyzer = PlotOccurences(ticker, start_date)
    analyzer.plot_data()

def prob_corrections(ticker,start_date):
    analyzer = ProbCorrections(ticker, start_date)
    analyzer.plot_data()

def main():
    plot_corrections('SPY','2014-01-01')
    prob_corrections('SPY','2014-01-01')
    
if __name__ == "__main__":
    main()

def prob_corrections_test(ticker, start_date):
    ProbCorrections('SPY','2014-01-01')
    
def plot_corrections_test(ticker, start_date):
    PlotOccurences('SPY','2014-01-01')