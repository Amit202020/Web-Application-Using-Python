from flask import Flask,request
from flask_restful import Resource,Api
from flask_jwt import JWT,jwt_required

from security import authenticate,identity

app = Flask(__name__)
app.secret_key = "maax" # should be secure
api = Api(app)

jwt = JWT(app,authenticate,identity)

items = []

class Item(Resource):
      @jwt_required()
      def get(self,name):
               item = next(filter(lambda x: x['name'] == name , items),None)
               return {'item':item}, 200 if item else 404
      def post(self,name):
                if next(filter(lambda x: x['name'] == name , items),None):
                	return {'message':"An item with the name already exist."}
                data=request.get_json(force=True) #not required content type error
                item = {'name':name,'price':data['price']}
                items.append(item)
                return item

      def delete(self,name):
                global items
                items =list(filter(lambda x: x['name'] != name,items))
                return {"message":"Item deleted"}

      def put(self,name):
                data = request.get_json()
                item = next(filter(lambda x: x['name'] == name,items),None)
                if item is None:
	                   item = {'name':name,'price': data['price']}
	                   items.append(item)
                else:
	                   item.update(data)
                return item



class ItemList(Resource):
      def get(self):
          return {'items':items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')


app.run(port=5000,debug=True)