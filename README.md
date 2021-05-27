# Movie Magic and The "Magical" Swear Words
![Profanity in Film](https://nofilmschool.com/sites/default/files/styles/article_1500/public/wow.jpg?itok=6r6h97Z1)

Profanity in media is nothing groundbreaking. In fact, profanity has become such a commonplace in media that Netflix even has a [new comedy series "History of Swear Words"](https://www.netflix.com/title/81305757) dedicated to explaining and uncovering the origin and impacts of the common foulmouthery. 

But what of these "magical words" and their place on the big screen? Has the increased frequency of spoken vulgarities become an indicator of a more popular, more trendy, more succesful film? We seek to solve this mystery!

## This is where the magic happens

### Questions
This project is built as a website with interactive visualizations using Tableau and machine learning components using Azure ML. Our key questions we hope to answer include the following:

* Are there more movies with higher profanity counts in recent years?
* How does profanity impact profit or budgets?
* Which directors are notorious for including profanity?
* Can we predict if a movie can breakeven (defined by profit - budget) based on the following:
  * Profanity Count
  * Director
  * Genre
  * Rating
  * Year
* Can we predict the movie's rating (G,PG,PG-13,R) of the film given: 
  * Director
  * Genre
  * Rating
  * Year
  * Profanity Count 

### Methodology: Key Subject "Magic" Words
![Key Subject "Magic" Swear Words](https://bicontent.businessinsurance.com/4932e90f-7e6c-4bad-90b9-85f79c7723fd.jpg)

As varied and complex the English Language may be, we identify the following swear words as our key subjects, due to their notoriety and commonality. Please note that variations are also factored under the identification process:
* F*ck
* B*tch
* Sh*t

### Data

The data sources of the project's script analysis are from the following:
* [The Internet Movie script Database](https://imsdb.com/all-scripts.html)
* [IMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)

#### Web Scraping and Data Cleaning

In order to perform our profanity script analysis, Beautiful Soup was used to parse and save the available movie scripts from IMDSB site into our all_script.csv.  Individual script files were then parsed through a function that counted the frequency of each of chosen key swear words (including variations of) as well as a total swear words counter. Duplicate records were removed from the movie_metadata.csv and the genre list values were split up across multiple new genre columns into a series of dummy  boolean variables. The two datasets were then merged to create the combined dataframe that contains movie and script information.

#### API

After data processing, the movie, scripts, and merged datasets were loaded into a SQLite database using SQLAlchemy and Flask to create an API that returns the datasets in JSON format.


