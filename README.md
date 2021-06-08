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
  * Director
  * Duration
  * Content Rating
  * Gross Revenue
  * Swear Count
* Can we predict the movie's rating (G,PG,PG-13,R) of the film given: 
  * Director
  * Duration
  * Content Rating
  * Gross Revenue
  * IMDB Score
  * Swear Count

### Methodology: Key Subject "Magic" Words
![Key Subject "Magic" Swear Words](https://bicontent.businessinsurance.com/4932e90f-7e6c-4bad-90b9-85f79c7723fd.jpg)

As varied and complex the English Language may be, we identify the following swear words as our key subjects, due to their notoriety and commonality. Please note that variations are also factored under the identification process:
* F*ck
* B*tch
* Sh*t

## Data
The data sources of the project's script analysis are from the following:
* [The Internet Movie script Database](https://imsdb.com/all-scripts.html)
* [IMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)

#### Web Scraping and Data Cleaning

In order to perform our profanity script analysis, Beautiful Soup was used to parse and save the available movie scripts from IMDSB site into our all_script.csv.  Individual script files were then parsed through a function that counted the frequency of each of chosen key swear words (including variations of) as well as a total swear words counter. Duplicate records were removed from the movie_metadata.csv and the genre list values were split up across multiple new genre columns into a series of dummy  boolean variables. The two datasets were then merged to create the combined dataframe that contains movie and script information.

## Home Page 
<img src="/Images/Landing_Page.PNG" alt="My cool logo"/>

## API

After data processing, the movie, scripts, and merged datasets were loaded into a SQLite database using SQLAlchemy and Flask to create an API that returns the datasets in JSON format. In addition to the route to fetch data, the rest of our website application can be accessed locally through the following routes:

|Route|Description|
|-|-|
|/api/v1.0/timeseries_viz|Time Series Interactive Dashboard|
|/api/v1.0/contentrating_viz|Director's Interactive Dashboard|
|/api/v1.0/content_rating_ML|Machine Learning Model that predicts content Rating|
|/api/v1.0/breakeven_ML|Machine Learning Model that predicts movie will breakeven|
|/api/v1.0/bonus_visuals|Bonus visuals on swear words and movies|
|/api/v1.0/get_movie_swear	|API Data for Merged movie_swear dataset in JSON format


## Visualizations

### Time Series
Utilizing the dataset, shows various visualization of how the use of swear words has changed over time in film. Within the last 10 years, there has been an increase in the presence of swear in various genres including thriller, comedy, and action. Visualizations also include if a film broke even based on swear count. These are also useful to reference for application of the ML portion.

<img src="/Images/Director's%20Dashboard.PNG" alt="My cool logo"/>

### Directors
An analysis on directors was done to see what directors had more films with greater swear words per minute, the director's that had their films at least break even, directors' most common swear word from our selected three, and the directors that used the most swear words in our dataset. These are also useful to reference for application of the ML portion.

<img src="/Images/Director1.PNG" alt="My cool logo"/>
<img src="/Images/Director2.PNG" alt="My cool logo"/>


### Bonus
Includes visualizations to aid users in changing aspects in ML to produce different results. Mainly focuses on profanity, genre, rating, and popularity. 

## Machine Learning
With Azure, created two machine learning models with accuracies between 70 and 80% for user application on whether a film breaks even and content rating of film.
### Breakeven
Insert director's name, duration of film, content rating, gross revenue, swear count, and true or false to indicate use of profanity to get a percentage on the likelihood that a film will break even or not with your above criteria.
<img src="/Images/BreakEvenML.PNG" alt="My cool logo"/>

### Content Rating
Insert director's name, duration of film, an actor's name, movie release year, gross revenue, iMDb score, swear count, and true or false to indicate use of profanity to get the content rating of a film with your above criteria.

<img src="/Images/Content_Rating%20ML.PNG" alt="My cool logo"/>



## Key Takeaways
Films have become more likely to use profanity and succeed with praises from audience as time has progressed. This indicates that swear words have grown in their use in American colloquialism.



