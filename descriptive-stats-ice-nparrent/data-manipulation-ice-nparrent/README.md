[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/coA8kJak)
# Using and Manipulating Data ICE
Create a new script file for Python. Do not type all of your code into the console and attempt to copy it into a script file. Code your script file first, then run the code. This can be line-by-line or all at once. I recommend running it line-by-line to better identify bugs.

Take screen captures of the output in the Python console and link it into your GitHub markup document `submission.md`.

To submit, please perform the following:
1. Save a script file for Python with the following name: `ice_lastname_firstname.py` where lastname is your last name and firstname is your first name.
1. Save your screenshots of your output to the directory `assets`. You may need to create it.
1. Link your screenshots in `submission.md` where appropriate. That is, if you have screenshots supporting your answers, link those screenshots next to your answer.
1. Answer questions in `submission.md`, linking any screenshots as necessary.
1. Push your assignment to GitHub.

### Accessing data (5 pts.)
Using the dataset [car.test.frame.txt](/data/car.test.frame.txt), please perform the following operations in order:
* Open the file within Python
* Find out what the column header names are
* Determine the number of columns
* Determine the number of rows
* Determine which columns are categorical and convert them from *object* to *category*
* How many unique values does `Type` have?
* How many unique values does `Country` have?
* * What is the value of the 57th row and 3rd column?
* What are the values for the 24th row?
* Using three different methods, select row with index value 29 with 1st, 2nd, 3rd columns
* Using two different ways, select the row with index value 45 with the 3rd and 7th columns
* Create a new dataframe for the column `HP` using two different methods

### Sorting and ordering data (5 pts.)
Now that you have learned to subsample your data, it is your turn to try your new knowledge. Using the `car.test.frame` dataset, please perform the following operations in order:
* Select compact cars that have a reliability greater than and equal to 4.
* Find compact cars that have a reliability greater than and equal to 3 from Japan, but not from the US
* How many cars are manufactured with the label `Japan/USA`?
* How many cars are manufactured in the `US` or `Japan`?
* How many cars are manufactured in the `US` or `Japan` with a reliability greater than and equal to 4?
* Create a subsample of 70% of your data
* Create samples for a 8-fold cross validation test
* Select columns that are numeric and save it as a new dataframe
* Remove the columns HP and Price from the dataframe
* Save the columns Country and Weight as a new datafame
* Rename these two columns in the new dataframe
