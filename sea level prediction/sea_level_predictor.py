import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    #1 - Use Pandas to import the data from epa-sea-level.csv.
    df = pd.read_csv('epa-sea-level.csv')

    #2- Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level
    #  column as the y-axis.
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit.
    #  Plot the line of best fit over the top of the scatter plot.
    #  Make the line go through the year 2050 to predict the sea level rise in 2050.
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051) 
    sea_levels_extended = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_levels_extended, color='red', label='Best Fit Line (1880 - 2050)')

    #3 - Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset.
    #  Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = range(2000, 2051)
    sea_levels_recent = [slope_recent * year + intercept_recent for year in years_recent_extended]
    plt.plot(years_recent_extended, sea_levels_recent, color='green', label='Best Fit Line (2000 - 2050)')

    #4 - The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()