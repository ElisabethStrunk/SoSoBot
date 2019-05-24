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
        val shouldMove = when (motionEvent.actionMasked) {
            MotionEvent.ACTION_DOWN -> true
            else -> false
        }

        when (view) {
            leftButton -> robotConnection.left(shouldMove)
            upButton -> robotConnection.forward(shouldMove)
            rightButton -> robotConnection.right(shouldMove)
            downButton -> robotConnection.backward(shouldMove)
        }
        true
    }
}
