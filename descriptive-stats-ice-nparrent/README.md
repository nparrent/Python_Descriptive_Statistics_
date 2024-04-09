[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/vadDslbu)
# Descriptive Statistics ICE
To submit, please perform the following:
1. Save a script file for Python with the following name: `ice_lastname_firstname.py` where lastname is your last name and firstname is your first name.
1. Save your screenshots (if any) to the directory `assets`.
1. Link your screenshots (if any) in `submission.md` where appropriate.
1. Answer questions (if any) in `submission.md`.
1. Push your assignment to GitHub.

### Summarizing the Data (2 pts.)
Using the data file [pollute.txt](data/pollute.txt), assess the basic descriptive information of the data. Specifically, provide the mean, median, variance, standard deviation, min, max, data type, number of missing values, and the number of unique values for the following variables:
* pollution
* temp
* industry
* population
* wind
* rain
* wet.days

### Using Plots with Python (3 pts.)
Using the data file [pollute.txt](/data/pollute.txt), assess each variable for outliers and linearity using various plots. Provide screenshots of the plots and justify in writing (within the Word file) your choice of plot; do this for each plot. Use `pollution` as the target (i.e. *y*-variable) for the scatter plots when assessing linearity.

### Assessing Normality with Python (2 pts.)
Using the data file [ozone.data.txt](/data/ozone.data.txt), assess normality using both QQ plots and Shapiro-Wilk tests for each of the following variables:
* `rad` *solar radiation*
* `temp` *temperature*
* `wind` *wind speed*
* `ozone` *ozone*

Discuss what you see in the QQ plots and whether they agree with the results of the Shapiro-Wilk test.

### Skewness and Kurtosis (3 pts.)
Using the data file [ozone.data.txt](/data/ozone.data.txt), please do the following:
* Assess the skew and kurtosis of each variable and report on what you find. 
* Compare the values for skewness and kurtosis to histograms. 
  * Do you find that the values correspond with what you see? 
  * Which of the variables are left skewed? Right skewed? 
  * How does the kurtosis look?
