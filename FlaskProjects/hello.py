
from flask import Flask
app = Flask(__name__)   #special variable that will give each file a unique name.
                        #we can say this application is running in this name
#which request it will understand
#www.yahoo.com/career
#www.yahoo.com/loc
@app.route('/')
def home():
	return "hello world"

app.run(port=5000)
