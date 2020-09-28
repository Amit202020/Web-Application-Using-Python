from flask import Flask,jsonify,render_template,request

# Create the application instance
app = Flask(__name__, template_folder="templates")

#store contain dictionary
stores = [
 {
  "name":"cricketstore",
  "items":[
     {
	"name":"My Item",
    "price":15.99
     }
   ]
 }
]


#web application
@app.route('/')
def home():
	return render_template('home.html')



#get  item in store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
   for store in stores:
   	   if store['name'] == name:
		         return jsonify({'items':store['items']})
   return jsonify({'message':'store not found'})



#get store by name
@app.route('/store/<string:name>')
def get_store(name):
        for store in stores:
	           if store['name'] == name:
        	      return jsonify(store)
        return jsonify({'message':'store not found'})


#get all
@app.route('/store')
def get_all_store():
    return jsonify({"stores":stores})



#post create store
@app.route('/store',methods=['POST'])
def create_store():
   request_data = request.get_json()
   new_store = {
      "name":request_data['name'],
       "item":[]
   }
   stores.append(new_store)
   return jsonify(new_store)


#post create item
@app.route('/store/<string:name>/item',methods=['POST'])
def create_items_in_store(name):
   request_data = request.get_json()
   for store in stores:
        if store['name'] == name:
                new_item = {
			             'name':request_data['name'],
                         'price':request_data['price'],
                }
                store['items'].append(new_item)
                return jsonify(new_item)
   return jsonify({'message':'store not found'})



app.run(port=5000)
