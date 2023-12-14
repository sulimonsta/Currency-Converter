### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
python is more server side development but javascript is more client side. Python is usually executed on a server and javascript is mostly executed in browsers.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
you can use the get method or using exception handling.
- What is a unit test?
test where individual components are tested to make sure they work.
- What is an integration test?
testing combined parts of a system to make sure they work together.
- What is the role of web application framework, like Flask?
it simplifies builing web apps, handles routes and requests and allows template rendering and interacting with databases.
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
/foods/ is when data is essential and the other is when the data is optional.
- How do you collect data from a URL placeholder parameter using Flask?
from flask import Flask

app = Flask(__name__)

@app.route('/foods/<food_type>')
def get_food(food_type):
    return f'The requested food type is {food_type}'

- How do you collect data from the query string using Flask?
from flask import Flask, request

app = Flask(__name__)

@app.route('/foods')
def get_food():
    food_type = request.args.get('type')
    return f'The requested food type is {food_type}'

- How do you collect data from the body of the request using Flask?
from flask import Flask, request

app = Flask(__name__)

@app.route('/foods', methods=['POST'])
def create_food():
    data = request.json  # Assuming the request body is in JSON format
    # Process data and create a new food item
    return 'Food created successfully'

- What is a cookie and what kinds of things are they commonly used for?
small piece of data used for tracking users, personalization, and session management.
- What is the session object in Flask?
dictionary that allows user-specific information for requests.
- What does Flask's `jsonify()` do?
converts python dictionary into a json formatted response