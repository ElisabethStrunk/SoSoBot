package saltandpepper.software.sosobotandroid

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.MotionEvent
import android.view.View
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

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
            MotionEvent.ACTION_DOWN -> robotConnection.move(direction)
            MotionEvent.ACTION_UP -> robotConnection.stop(direction)
        }
        false
    }
}
