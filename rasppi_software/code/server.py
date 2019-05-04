
from flask import Flask, request
from flask_restful import Api, Resource


class Motor(Resource):
    def put(self, direction):
        try:
            motor_status = request.args.get('on')
        except:
            motor_status = None
        if direction == 'right':
            if motor_status == '1':
                # TODO: call function for turning the right motor on
                return {"message": "RIGHT motor turned ON"}, 200
            elif motor_status == '0':
                # TODO: call function for turning the right motor off
                return {"message": "RIGHT motor turned OFF"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direction == 'left':
            if motor_status == '1':
                # TODO: call function for turning the left motor on
                return {"message": "LEFT motor turned ON"}, 200
            elif motor_status == '0':
                # TODO: call function for turning the left motor off
                return {"message": "LEFT motor turned OFF"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direction == 'both':
            if motor_status == '1':
                # TODO: call function for turning both motors on
                return {"message": "BOTH motors turned ON"}, 200
            elif motor_status == '0':
                # TODO: call function for turning both motors off
                return {"message": "BOTH motors turned OFF"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        else:
            return {"message": "Motor '{}' not found".format(direction)}, 400


app = Flask(__name__)
api = Api(app)
api.add_resource(Motor, '/motor/<string:direction>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
