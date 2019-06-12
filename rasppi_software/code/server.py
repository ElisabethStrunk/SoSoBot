# ***************************************************************
# Imports
# ***************************************************************
from flask import Flask

from motor_ctrl import motor_left, motor_right


# ***************************************************************
# Classes
# ***************************************************************
app = Flask(__name__)


@app.route('/move/<string:direct>/')
@app.route('/move/<string:direct>/<float:velocity>/')
def motor(direct,  velocity=1.0):
    if direct == 'forward':
        motor_left.forward(velocity)
        motor_right.forward(velocity)
        return "Driving forward!", 200

    # your code her for moving the car backward, left, right and stop

    else:
        return 'ERROR: Invalid direction', 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
