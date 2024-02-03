from flask import Flask, Response
from flask_restful import Resource, Api 

simpleapp = Flask(__name__) 
simpleappapi = Api(simpleapp) 

class Welcome(Resource): 
	def get(self): 
		return Response('Welcome to 2024') 

class Home(Resource): 
	def get(self): 
		return Response('Welcome to the homepage of simpleapp') 

simpleappapi.add_resource(Welcome, '/welcome') 
simpleappapi.add_resource(Home, '/') 

# driver function 
if __name__ == '__main__': 

	simpleapp.run(debug = True, port= 9000) 
