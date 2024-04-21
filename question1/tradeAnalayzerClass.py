from abc import ABC, abstractmethod
from scipy.signal import savgol_filter, find_peaks
import yfinance as yf

class DataAnalyzer(ABC):
    def __init__(self, ticker, start_date):
        self.ticker = ticker
        self.start_date = start_date
        self.index_data = None
        self.sg_filter = None
        self.peaks = None
        self.troughs = None
        self.downward_trends = {}
    
    
    def fetch_data(self):
         self.index_data = yf.download(self.ticker, start=self.start_date)

    
    def process_data(self):
        if self.index_data is not None:
            window_length = 11
            polyorder = 3
            distance = 10
            prominence = 10

            self.sg_filter = savgol_filter(self.index_data['Close'], window_length, polyorder)
            self.peaks, _ = find_peaks(self.sg_filter, distance=distance, prominence=prominence)
            self.troughs, _ = find_peaks(-self.sg_filter, distance=distance, prominence=prominence)
            
            self.calculate_percentage_changes()
            self.identify_downward_trends()


    
    def calculate_percentage_changes(self):
        self.percentage_changes = []
        for peak_idx, trough_idx in zip(self.peaks, self.troughs):
            peak_price = self.sg_filter[peak_idx]
            trough_price = self.sg_filter[trough_idx]
            percentage_change = ((trough_price - peak_price) / peak_price) * 100
            self.percentage_changes.append(percentage_change)

    def identify_downward_trends(self):
        self.downward_trends = {'3-5%': [], '5-10%': [], 'above 10%': []}
        for idx, change in enumerate(self.percentage_changes):
            if 3 <= abs(change) < 5:
                self.downward_trends['3-5%'].append((self.peaks[idx], self.troughs[idx]))
            elif 5 <= abs(change) < 10:
                self.downward_trends['5-10%'].append((self.peaks[idx], self.troughs[idx]))
            elif abs(change) >= 10:
                self.downward_trends['above 10%'].append((self.peaks[idx], self.troughs[idx]))
    
    @abstractmethod
    def plot_data(self):
        pass