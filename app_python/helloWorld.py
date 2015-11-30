import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello World!</h1>  <br/>This is a Python app running on Cloud Foundry.<br/><br/><br/><b>Time:</b>  %s' % datetime.now().time()

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
    

    
#use 2 envrionment variables to add New Relic:
#  NEW_RELIC_APP_NAME
#  NEW_RELIC_LICENSE_KEY 
