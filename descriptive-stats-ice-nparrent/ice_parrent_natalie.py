###############################
#       Read in Libraries     #
###############################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from tabulate import tabulate

#For QQ Plot
import scipy.stats as sts
################################
#     Set Working Directory    #
################################
os.getcwd()
os.chdir(r'\Users\npleg\OneDrive\Documents\GitHub\Python\descriptive-stats-ice-nparrent\data')
os.getcwd()

################################
#         Read in Data         #
################################
pollute_data = pd.read_table('pollute.txt', sep='\t')
pollute_data.columns

ozone_data = pd.read_table('ozone.data.txt', sep='\t')
ozone_data.columns

################################
#     Descriptive Information  #
################################
pollute_data.describe()
pollute_data.dtypes
pollute_data['wind'] = pollute_data['wind'].astype(int)

# Initialize a list
descriptive_stats = []

# Iterate over each variable

for variables in pollute_data.columns:

    mean = pollute_data[variables].mean()
    median = pollute_data[variables].median()
    variance = pollute_data[variables].var()
    stand_dev = pollute_data[variables].std()
    min = pollute_data[variables].min()
    max = pollute_data[variables].max()
    data_type = pollute_data[variables].dtypes
    miss_values = len(pollute_data[variables])-(pollute_data[variables].count())
    uniq_values = len(pollute_data[variables].unique())  

    descriptive_stats.append([variables, mean, median, variance, stand_dev, min, max, data_type, miss_values, uniq_values])

# Define headers for the table
headers = ['Variable', 'Mean', 'Median', 'Variance', 'Standard Deviation', 'Min', 'Max', 'Data Type', '# Missing','# Unique']

# Print the table
print(tabulate(descriptive_stats, headers=headers, tablefmt="fancy_grid", numalign="right"))


################################
#    Plots with Python         #
################################
#Scatter Plots
save_dir = r'C:\Users\npleg\OneDrive\Documents\GitHub\Python\descriptive-stats-ice-nparrent\assets\Scatter Plots'

for variable in pollute_data.columns:
    x = pollute_data[variable]
    y = pollute_data['pollution']

    plt.scatter(x, y)
    plt.xlabel(variable)
    plt.ylabel('pollution')
    title_variable = variable.capitalize()
    plt.title(f'{title_variable} vs Pollution')
    plt.savefig(os.path.join(save_dir, f'{variable}_plot.png'))
    plt.show()
    plt.clf()
plt.close('all')

#Box Plots
save_dir_2 = r'C:\Users\npleg\OneDrive\Documents\GitHub\Python\descriptive-stats-ice-nparrent\assets\Box Plots'
for variable in pollute_data.columns:
    plt.boxplot(pollute_data[variable])
    plt.title(f'{variable} Boxplot')
    plt.savefig(os.path.join(save_dir_2, f'{variable}_plot.png'))
    plt.show()
    plt.clf()
plt.close('all')

################################
#    Assessing Normality       #
################################
save_dir_3 = r'C:\Users\npleg\OneDrive\Documents\GitHub\Python\descriptive-stats-ice-nparrent\assets\Normality'
oz_var = 'rad', 'temp', 'wind', 'ozone'
for oz_var in ozone_data:
    sts.probplot(ozone_data[oz_var], dist="norm", plot=plt)
    title_oz= oz_var.capitalize()
    plt.title(f'{title_oz} Probability Plot')
    plt.savefig(os.path.join(save_dir_3, f'{oz_var}_norm_plot.png'))
    plt.show()
    plt.clf()
plt.close('all')

shapiro_wilk = []

for var in ozone_data.columns:
    s_w = sts.shapiro(ozone_data[var])
  
    shapiro_wilk.append([var, s_w])

# Define headers for the table
headers = ['Variable', 'Shapiro_Wilk']

# Print the table
print(tabulate(shapiro_wilk, headers=headers, tablefmt="fancy_grid", numalign="right"))


################################
#    Skewness and Kurtosis     #
################################
skew_kurt = []

for var in ozone_data.columns:
    skew = ozone_data[var].skew()
    kurt = ozone_data[var].kurt()
    skew_kurt.append([var, skew, kurt])

# Define headers for the table
headers = ['Variable', 'Skewness', 'Kurtosis']

# Print the table
print(tabulate(skew_kurt, headers=headers, tablefmt="fancy_grid", numalign="right"))

## Histograms
save_dir_4 = r'C:\Users\npleg\OneDrive\Documents\GitHub\Python\descriptive-stats-ice-nparrent\assets\Histograms'

for var in ozone_data:
    ozone_data[var].plot.hist(alpha=0.5)
    title_oz= var.capitalize()
    plt.title(f'{title_oz} Histogram')
    plt.savefig(os.path.join(save_dir_4, f'{var}__plot.png'))
    plt.show()
    plt.clf()
plt.close('all')