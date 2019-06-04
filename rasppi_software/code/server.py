#***************************************************************
#	Imports
#***************************************************************
from flask import Flask, request
from flask_restful import Api, Resource

from motor_ctrl import motor_left # Add your import here

#***************************************************************
#	Classes
#***************************************************************
app = Flask(__name__)
@app.route('/move/<string:direct>/')
@app.route('/move/<string:direct>/<float:velocity>/')
def motor(direct,  velocity = 1.0):
  if direct == 'right':
    return motor_left.forward(velocity)
  # Your code for left, forward, backward direction
  else:
    return 'ERROR: Invalid direction'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)