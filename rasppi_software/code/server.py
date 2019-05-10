
from flask import Flask, request
from flask_restful import Api, Resource
from motor_ctrl import motor_left, motor_right

#***************************************************************
#	Global-Functions
#***************************************************************

class Motor(Resource):
    def put(self, direction):
        try:
            motor_status = request.args.get('on')
        except:
            motor_status = None
        if direction == 'right':
            if motor_status == '1':
                motor_right.forward()
                return {"message": "RIGHT motor turned ON"}, 200
            elif motor_status == '0':
                motor_right.stop()
                return {"message": "RIGHT motor turned OFF"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direction == 'left':
            if motor_status == '1':
                motor_left.forward()
                return {"message": "LEFT motor turned ON"}, 200
            elif motor_status == '0':
                motor_left.stop()
                return {"message": "LEFT motor turned OFF"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direction == 'both':
            if motor_status == '1':
                motor_right.forward()
                motor_left.forward()
                return {"message": "BOTH motors turned ON"}, 200
            elif motor_status == '0':
                motor_right.stop()
                motor_left.stop()
                return {"message": "BOTH motors turned OFF"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        else:
            return {"message": "Motor '{}' not found".format(direction)}, 400


app = Flask(__name__)
api = Api(app)
api.add_resource(Motor, '/motor/<string:direction>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
