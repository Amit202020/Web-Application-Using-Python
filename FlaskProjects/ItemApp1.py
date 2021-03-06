from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

items = []

#filter function does not generate any item
#actually many items can be generated by this filter function
#it does not return a list also
#it return a filter object
#list(filter(....)) it return list of item returned by filter function
#next(filter(....)) it return first item returned by filter function
#if the next function does not find an item it will return None


class Item(Resource):
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


class ItemList(Resource):
      def get(self):
          return {'items':items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')


app.run(port=5000,debug=True)
