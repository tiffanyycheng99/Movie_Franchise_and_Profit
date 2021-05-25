"""
Routes and views for the flask application.
"""
import json
import urllib.request
import os
from os import environ

from flask import Flask
app = Flask(__name__)


from datetime import datetime
from flask import render_template, request, redirect
# from FlaskAppAML import app
#testing
# from FlaskAppAML.forms import SubmissionForm
from wtforms import Form, StringField, TextAreaField, validators


class SubmissionForm(Form):
    title = StringField('Title', [validators.Length(min=2, max=30)])
    category = StringField('Category', [validators.Length(min=0, max=30)])
    text = TextAreaField('Text', [validators.Length(min=1, max=500)])

Movie_ML_KEY=os.environ.get('API_KEY', "ZllqwGHyixSUlBpCUbYQTqJlzaJQ5XnTcemxOMRYQ946q+ck/OGnLY+XEg6b/tXKwAeWNNkQ6UyeW/L3gyQXUA==")
Movie_URL = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/0c8068a6b23d4d5096f6671ba367b97c/services/b628a3ec7b46444588460dda21404182/execute?api-version=2.0&details=true")
# Deployment environment variables defined on Azure (pull in with os.environ)

# Construct the HTTP request header
# HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ API_KEY)}

HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ Movie_ML_KEY)}

# Our main app page/route
@app.route('/', methods=['GET', 'POST'])
# def root():
#     return render_template('contact.html')
@app.route('/home', methods=['GET', 'POST'])
def home():
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
                    "0"
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
                'result.html',
                title="This is the result from AzureML running our example Student Brain Weight Prediction:",
                result=result)

        # An HTTP error
        except urllib.error.HTTPError as err:
            result="The request failed with status code: " + str(err.code)
            return render_template(
                'result.html',
                title='There was an error',
                result=result)
            #print(err)

    # Just serve up the input form
    return render_template(
        'form.html',
        form=form,
        title='Run App',
        year=datetime.now().year,
        message='Demonstrating a website using Azure ML Api')


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

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
    output='For a brain with the size of : '+value[4]+ "<br/>Our Algorithm would calculate the weight to be: "+ value[2]
    # Build the entire html table for the results data representation
    #tablestr = 'Cluster assignment: %s<br><br><table border="1"><tr><th>Cluster</th><th>Distance From Center</th></tr>'+ repstr + "</table>"
    #return tablestr % data
    return output


if __name__ == '__main__':
    app.run()