# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func
# import json


"""
Routes and views for the flask application.
"""
import json
import urllib.request
import os
from os import environ


from flask import Flask
from datetime import datetime
from flask import render_template, request, redirect
# from FlaskAppAML import app
#testing
# from FlaskAppAML.forms import SubmissionForm
from wtforms import Form, StringField, TextAreaField, validators


class SubmissionForm(Form):
    title = StringField('Title')
    category = StringField('Category')
    # text = TextAreaField('Text', [validators.Length(min=1, max=500)])
    duration = StringField('Duration')
    contentRating = StringField('Content Rating')
    gross = StringField('Gross')
    SwearCount = StringField('SwearCount')
    profanity = StringField('Profanity')

class SubmissionForm2(Form):
    title = StringField('Title')
    category = StringField('Category')
    # text = TextAreaField('Text', [validators.Length(min=1, max=500)])
    duration = StringField('Duration')
    actor1name = StringField('Actor 1 Name')
    titleyear = StringField('Title Year')
    gross = StringField('Gross')
    imdbScore = StringField('IMDB Score')
    SwearCount = StringField('SwearCount')
    profanity = StringField('Profanity')





Movie_ML_KEY=os.environ.get('API_KEY', "ZllqwGHyixSUlBpCUbYQTqJlzaJQ5XnTcemxOMRYQ946q+ck/OGnLY+XEg6b/tXKwAeWNNkQ6UyeW/L3gyQXUA==")
Movie_URL = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/0c8068a6b23d4d5096f6671ba367b97c/services/b628a3ec7b46444588460dda21404182/execute?api-version=2.0&details=true")
Content_ML_KEY=os.environ.get('API_KEY', "dhCcJYWaQHZEVMeMTAdWquJhVhMqfY0Lw1uhLFvIddg77k2vaiVdH9KipspipwrVXAQVRTGPiuMozV4cj9mg/A==")
Content_URL = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/0c8068a6b23d4d5096f6671ba367b97c/services/129f542f026c4def86ba4a5c3238c5f6/execute?api-version=2.0&details=true")

# Deployment environment variables defined on Azure (pull in with os.environ)

# Construct the HTTP request header
# HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ API_KEY)}

HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ Movie_ML_KEY)}
HEADERS2 = {'Content-Type':'application/json', 'Authorization':('Bearer '+ Content_ML_KEY)}

# eng = create_engine("postgresql://postgres:postgres@movie-swear-db.cfgivq9r1u3j.us-west-2.rds.amazonaws.com:5432/moviesweardb")
# con = eng.connect()
# Base = automap_base()
# Base.prepare(eng, reflect=True)
# movieSwear = Base.classes.movieSwear

# session = Session(eng)

app = Flask(__name__)

@app.route("/")
def home():
        return render_template("index.html")

@app.route("/api/v1.0/timeseries_viz")
def timeseries_viz():
        return render_template("timeseries_viz.html")

@app.route("/api/v1.0/contentrating_viz")
def contentrating_viz():
        return render_template("contentrating_viz.html")

@app.route("/api/v1.0/content_rating_ML", methods=['GET', 'POST'])
def content_rating_ML():
        """Renders the home page which is the CNS of the web app currently, nothing pretty."""

        form = SubmissionForm2(request.form)
        print(form.title.data.lower())
    # Form has been submitted
        if request.method == 'POST' and form.validate():
    
                # Plug in the data into a dictionary object 
                #  - data from the input form
                #  - text data must be converted to lowercase
                data =  {
                        "Inputs": {
                        "input1": {
                        "ColumnNames": [
                        "Column 0",
                        "color",
                        "director_name",
                        "num_critic_for_reviews",
                        "duration",
                        "director_facebook_likes",
                        "actor_3_facebook_likes",
                        "actor_2_name",
                        "actor_1_facebook_likes",
                        "actor_1_name",
                        "title",
                        "num_voted_users",
                        "cast_total_facebook_likes",
                        "actor_3_name",
                        "facenumber_in_poster",
                        "plot_keywords",
                        "movie_imdb_link",
                        "num_user_for_reviews",
                        "language",
                        "country",
                        "content_rating",
                        "title_year",
                        "actor_2_facebook_likes",
                        "imdb_score",
                        "aspect_ratio",
                        "movie_facebook_likes",
                        "Action",
                        "Adventure",
                        "Animation",
                        "Biography",
                        "Comedy",
                        "Crime",
                        "Documentary",
                        "Drama",
                        "Family",
                        "Fantasy",
                        "Film-Noir",
                        "Game-Show",
                        "History",
                        "Horror",
                        "Music",
                        "Musical",
                        "Mystery",
                        "News",
                        "Reality-TV",
                        "Romance",
                        "Sci-Fi",
                        "Short",
                        "Sport",
                        "Thriller",
                        "War",
                        "Western",
                        "breakeven",
                        "gross(in millions USD)",
                        "budget(in millions USD)",
                        "profit(in millions USD)",
                        "Swear_Count",
                        "Fuck_Count",
                        "Shit_Count",
                        "Bitch_Count",
                        "Cunt_Count",
                        "Profanity"
                        ],
                        "Values": [
                        [
                        "0",
                        "value",
                        form.title.data,
                        "0",
                        form.duration.data,
                        "0",
                        "0",
                        "value",
                        "0",
                        form.actor1name.data,
                        "value",
                        "0",
                        "0",
                        "value",
                        "0",
                        "value",
                        "value",
                        "0",
                        "value",
                        "0",
                        "value",
                        form.titleyear.data,
                        "0",
                        form.imdbScore.data,
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        form.gross.data,
                        "0",
                        "0",
                        form.SwearCount.data,
                        "0",
                        "0",
                        "0",
                        "0",
                        "0"
                        ],
                        [
                        "0",
                        "value",
                        "value",
                        "0",
                        "0",
                        "0",
                        "0",
                        "value",
                        "0",
                        "value",
                        "value",
                        "0",
                        "0",
                        "value",
                        "0",
                        "value",
                        "value",
                        "0",
                        "value",
                        "value",
                        "value",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        form.profanity.data
                        ]
                        ]
                        }
                },
                "GlobalParameters": {}
                }

                # Serialize the input data into json string
                body = str.encode(json.dumps(data))

                # Formulate the request
                #req = urllib.request.Request(URL, body, HEADERS)
                req = urllib.request.Request(Content_URL, body, HEADERS2)

                # Send this request to the AML service and render the results on page
                try:
                        # response = requests.post(URL, headers=HEADERS, data=body)
                        response = urllib.request.urlopen(req)
                        #print(response)
                        respdata = response.read()
                        result = json.loads(str(respdata, 'utf-8'))
                        result = do_something_pretty2(result)
                        # result = json.dumps(result, indent=4, sort_keys=True)
                        return render_template(
                                'content_result.html',
                                title="This is the result from AzureML running our algorithm to predict the content rating of a movie",
                                result=result)

                        # An HTTP error
                except urllib.error.HTTPError as err:
                        result="The request failed with status code: " + str(err.code)
                        return render_template(
                                'content_result.html',
                                title='There was an error',
                                result=result)
                        #print(err)

                # Just serve up the input form
        return render_template(
                'content_form.html',
                form=form,
                title='Run App',
                year=datetime.now().year,
                message='Demonstrating a website using Azure ML Api')

@app.route("/api/v1.0/breakeven_ML", methods=['GET', 'POST'])
def breakeven_ML():
        """Renders the home page which is the CNS of the web app currently, nothing pretty."""

        form = SubmissionForm(request.form)
        print(form.title.data.lower())
    # Form has been submitted
        if request.method == 'POST' and form.validate():
    
                # Plug in the data into a dictionary object 
                #  - data from the input form
                #  - text data must be converted to lowercase
                data =  {
                        "Inputs": {
                        "input1": {
                        "ColumnNames": [
                        "Column 0",
                        "color",
                        "director_name",
                        "num_critic_for_reviews",
                        "duration",
                        "director_facebook_likes",
                        "actor_3_facebook_likes",
                        "actor_2_name",
                        "actor_1_facebook_likes",
                        "actor_1_name",
                        "title",
                        "num_voted_users",
                        "cast_total_facebook_likes",
                        "actor_3_name",
                        "facenumber_in_poster",
                        "plot_keywords",
                        "movie_imdb_link",
                        "num_user_for_reviews",
                        "language",
                        "country",
                        "content_rating",
                        "title_year",
                        "actor_2_facebook_likes",
                        "imdb_score",
                        "aspect_ratio",
                        "movie_facebook_likes",
                        "Action",
                        "Adventure",
                        "Animation",
                        "Biography",
                        "Comedy",
                        "Crime",
                        "Documentary",
                        "Drama",
                        "Family",
                        "Fantasy",
                        "Film-Noir",
                        "Game-Show",
                        "History",
                        "Horror",
                        "Music",
                        "Musical",
                        "Mystery",
                        "News",
                        "Reality-TV",
                        "Romance",
                        "Sci-Fi",
                        "Short",
                        "Sport",
                        "Thriller",
                        "War",
                        "Western",
                        "breakeven",
                        "gross(in millions USD)",
                        "budget(in millions USD)",
                        "profit(in millions USD)",
                        "Swear_Count",
                        "Fuck_Count",
                        "Shit_Count",
                        "Bitch_Count",
                        "Cunt_Count",
                        "Profanity"
                        ],
                        "Values": [
                        [
                        "0",
                        "value",
                        form.title.data,
                        "0",
                        form.duration.data,
                        "0",
                        "0",
                        "value",
                        "0",
                        "value",
                        "value",
                        "0",
                        "0",
                        "value",
                        "0",
                        "value",
                        "value",
                        "0",
                        "value",
                        "0",
                        f'{form.contentRating.data}',
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        form.gross.data,
                        "0",
                        "0",
                        form.SwearCount.data,
                        "0",
                        "0",
                        "0",
                        "0",
                        "0"
                        ],
                        [
                        "0",
                        "value",
                        "value",
                        "0",
                        "0",
                        "0",
                        "0",
                        "value",
                        "0",
                        "value",
                        "value",
                        "0",
                        "0",
                        "value",
                        "0",
                        "value",
                        "value",
                        "0",
                        "value",
                        "value",
                        "value",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        form.profanity.data
                        ]
                        ]
                        }
                },
                "GlobalParameters": {}
                }

                # Serialize the input data into json string
                body = str.encode(json.dumps(data))

                # Formulate the request
                #req = urllib.request.Request(URL, body, HEADERS)
                req = urllib.request.Request(Movie_URL, body, HEADERS)

                # Send this request to the AML service and render the results on page
                try:
                        # response = requests.post(URL, headers=HEADERS, data=body)
                        response = urllib.request.urlopen(req)
                        #print(response)
                        respdata = response.read()
                        result = json.loads(str(respdata, 'utf-8'))
                        result = do_something_pretty(result)
                        # result = json.dumps(result, indent=4, sort_keys=True)
                        return render_template(
                                'breakeven_result.html',
                                title="This is the result from AzureML running our algorithm to predict whether a film will breakeven:",
                                result=result)

                        # An HTTP error
                except urllib.error.HTTPError as err:
                        result="The request failed with status code: " + str(err.code)
                        return render_template(
                                'breakeven_result.html',
                                title='There was an error',
                                result=result)
                        #print(err)

                # Just serve up the input form
        return render_template(
                'breakeven_form.html',
                form=form,
                title='Run App',
                year=datetime.now().year,
                message='Demonstrating a website using Azure ML Api')



@app.route("/api/v1.0/bonus_visuals")
def bonus_visuals():
        return render_template("bonus_visuals.html")


def do_something_pretty(jsondata):
    """We want to process the AML json result to be more human readable and understandable"""
    import itertools # for flattening a list of tuples below

    # We only want the first array from the array of arrays under "Value" 
    # - it's cluster assignment and distances from all centroid centers from k-means model
    value = jsondata["Results"]["output1"]["value"]["Values"][0]
    #valuelen = len(value)
    print(value)
    # Convert values (a list) to a list of tuples [(cluster#,distance),...]
    # valuetuple = list(zip(range(valuelen-1), value[1:(valuelen)]))
    # Convert the list of tuples to one long list (flatten it)
    # valuelist = list(itertools.chain(*valuetuple))

    # Convert to a tuple for the list
    # data = tuple(list(value[0]) + valuelist)

    # Build a placeholder for the cluster#,distance values
    #repstr = '<tr><td>%d</td><td>%s</td></tr>' * (valuelen-1)
    # print(repstr)
    output=' Director : '+value[0]+ "<br/>  Duration:"+value[1]+ 'Minutes'"<br/>  Content Rating:"+value[2]+ "<br/>  Swear Count:"+value[5]+ "<br/>  Gross Revenue:"'$'+value[4]+ "<br/>  Profanity:"+value[7]+"<br/>Our Algorithm would calculate the probability of breaking even to be: "+ value[8]
            
    # Build the entire html table for the results data representation
    #tablestr = 'Cluster assignment: %s<br><br><table border="1"><tr><th>Cluster</th><th>Distance From Center</th></tr>'+ repstr + "</table>"
    #return tablestr % data
    return output


def do_something_pretty2(jsondata):
    """We want to process the AML json result to be more human readable and understandable"""
    import itertools # for flattening a list of tuples below

    # We only want the first array from the array of arrays under "Value" 
    # - it's cluster assignment and distances from all centroid centers from k-means model
    value = jsondata["Results"]["output1"]["value"]["Values"][0]
    #valuelen = len(value)
    print(value)
    # Convert values (a list) to a list of tuples [(cluster#,distance),...]
    # valuetuple = list(zip(range(valuelen-1), value[1:(valuelen)]))
    # Convert the list of tuples to one long list (flatten it)
    # valuelist = list(itertools.chain(*valuetuple))

    # Convert to a tuple for the list
    # data = tuple(list(value[0]) + valuelist)

    # Build a placeholder for the cluster#,distance values
    #repstr = '<tr><td>%d</td><td>%s</td></tr>' * (valuelen-1)
    # print(repstr)
    output=' G: '+value[10]+ "<br/>  PG: "+value[13] + "<br/>  PG-13: "+value[14] + "<br/>  R: "+value[15] +"<br/> <br/> <strong>Our model predicts the content rating as: <strong>" + value[17] 
            
    # Build the entire html table for the results data representation
    #tablestr = 'Cluster assignment: %s<br><br><table border="1"><tr><th>Cluster</th><th>Distance From Center</th></tr>'+ repstr + "</table>"
    #return tablestr % data
    return output


if __name__ == '__main__':
    app.run(debug=True)