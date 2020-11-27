import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    plt.rcParams.update({'font.size': 14})
    
    # Read data from file
    filename = 'epa-sea-level.csv'
    df = pd.read_csv(filename)
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8,6))
    scatter = ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5)

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level', fontsize=14)
    
    x = np.arange(1850, 2055)
    
    # Create first line of best fit
    slope1, intercept1, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    y1 = intercept1 + slope1*x
    
    line1 = plt.plot(x, y1, 'r-', linewidth=1.5, label='all-years')
    plt.plot(x[idx], y1[idx], 'k+', markersize=10)
    plt.text(x[idx], y1[idx], '{:1.2f}'.format(y1[idx]), horizontalalignment='right', verticalalignment='bottom')

    # Create second line of best fit
    cond = (df['Year']>=2000)
    slope2, intercept2, r_value, p_value, std_err = linregress(df[cond]['Year'], df[cond]['CSIRO Adjusted Sea Level'])
    y2 = intercept2 + slope2*x

    line2 = plt.plot(x, y2, 'm-', linewidth=1.5, label='from 2000')
    plt.plot(x[idx], y2[idx], 'k+', markersize=10)
    plt.text(x[idx], y2[idx], '{:1.2f}'.format(y2[idx]), horizontalalignment='right', verticalalignment='bottom')

    # Add labels and title
    plt.legend()
    plt.grid(True)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()