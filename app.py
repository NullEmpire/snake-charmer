import os
from flask import Flask

#----------------------------------------
# Config
#----------------------------------------

env = {}
execfile("env.conf", env)

# Check to the environment
ENV = 'development'

if 'staging' in os.environ:
	ENV = 'staging'
elif 'production' in os.environ:
	ENV = 'production'

config = env[ENV]

#----------------------------------------
# Initialization
#----------------------------------------

app = Flask(__name__)

app.config.update(
    DEBUG = True,
)

#----------------------------------------
# Database
#----------------------------------------

# from mongoengine import connect
 
connect('myproject', host=config.dbURI, username='webapp', password='pwd123')

#----------------------------------------
# Controllers
#----------------------------------------

@app.route("/")

def hello():
    return "Hi."

#----------------------------------------
# Launch
#----------------------------------------

if __name__ == "__main__":
	print ' * Environment : '+ ENV
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

