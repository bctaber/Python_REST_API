#First Python API Tutorial
#Ref: https://www.youtube.com/watch?v=5ZMpbdK0uqU&list=PLPZbGfThL-GWlUaanfM_QNkOtIjnoBNtq&index=10
#Notes: Uses Python & Flask. Description: Flask was released in 2010, a micro web framework written in python to support the deployment of web applications with a minimal amount of code. It is designed to be an easy setup, flexible and fast to deploy as a microservice. Flask is built on WSGI (Python Web Server Gateway Interface) whereby the server will tie up a worker for each request.


from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set ={'Page':'Home','Message':'Successfully loaded the Home page', 'Timestamp':time.time()}
    json_dump= json.dumps(data_set)

    return json_dump



@app.route('/user/', methods=['GET'])
def request_page():

    user_query = str(request.args.get('user')) # /user/?user=bctaber



    data_set ={'Page':'Request','Message':f'Successfully loaded the Request for {user_query}', 'Timestamp':time.time()}
    json_dump= json.dumps(data_set)

    return json_dump


if __name__=='__main__':

    app.run(port=7777)



