import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return '<h1>Hello World!</h1>  <br/><br/>This is a Python app running on Cloud Foundry.'

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))