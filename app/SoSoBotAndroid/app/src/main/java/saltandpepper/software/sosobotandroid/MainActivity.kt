package saltandpepper.software.sosobotandroid

import android.os.Bundle
import android.view.MotionEvent
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity(), SliderControlFragment.OnFragmentInteractionListener {
    private val robotConnection = RobotConnection("192.168.101.62")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        leftButton.setOnTouchListener(onTouch)
        upButton.setOnTouchListener(onTouch)
        rightButton.setOnTouchListener(onTouch)
        downButton.setOnTouchListener(onTouch)
    }

    private val onTouch: (View,  MotionEvent) -> Boolean = { view, motionEvent ->
        val direction = when (view) {
            leftButton -> Direction.LEFT
            upButton -> Direction.FORWARD
            rightButton -> Direction.RIGHT
            else -> Direction.BACKWARD
        }

        when (motionEvent.actionMasked) {
            MotionEvent.ACTION_DOWN -> robotConnection.move(direction, onError = this::onError)
            MotionEvent.ACTION_UP -> robotConnection.stop(direction, this::onError)
        }
        false
    }

    override fun onFragmentInteraction(direction: Direction, power: Int) {
        robotConnection.move(direction, power.toByte())
    }

    private fun onError(message: String) {
        Toast.makeText(baseContext, message, Toast.LENGTH_LONG).show()
    }
}
