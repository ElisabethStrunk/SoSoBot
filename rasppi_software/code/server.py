# ***************************************************************
# Imports
# ***************************************************************
from flask import Flask

from motor_ctrl import motor_left, motor_right


# ***************************************************************
# Global-Functions
# ***************************************************************
def calculate_velocity(velocity):
    calc_velocity = velocity
    if velocity <= 0.0:
        calc_velocity = 0.0
    elif velocity >= 1.0:
        calc_velocity = 1.0
    return calc_velocity


# ***************************************************************
# Classes
# ***************************************************************
app = Flask(__name__)


@app.route('/move/<string:direct>/')
@app.route('/move/<string:direct>/<float:velocity>/')
def motor(direct,  velocity=1.0):
    velocity = calculate_velocity(velocity)
    if direct == 'right':
        return motor_left.forward(velocity)
    elif direct == 'left':
        return motor_right.forward(velocity)
    elif direct == 'forward':
        ret = motor_left.forward(velocity)
        ret = ret + '\n' + motor_right.forward(velocity)
        return ret
    elif direct == 'backward':
        ret = motor_left.backward(velocity)
        ret = ret + '\n' + motor_right.backward(velocity)
        return ret
    else:
        return 'ERROR: Invalid direction'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
