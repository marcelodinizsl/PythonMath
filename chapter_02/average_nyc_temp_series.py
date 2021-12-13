from matplotlib.pyplot import margins
from pylab import plot, show, legend, title, xlabel, ylabel

nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 54.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.2, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
months = range(1, 13)

def plot_data():
    """
    Plot method
    """
    plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
    legend([2000, 2006, 2012])

    title('Average monthly temperature in NYC')
    xlabel('Month')
    ylabel('Temperature')

    show()

def main():
    plot_data()

if __name__=="__main__":
   main()

