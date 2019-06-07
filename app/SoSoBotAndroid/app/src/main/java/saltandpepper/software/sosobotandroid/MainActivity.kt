package saltandpepper.software.sosobotandroid

import android.os.Bundle
import android.view.MotionEvent
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    /**
     * Provides a connection to the robot to move or stop it.
     */
    private val robotConnection = RobotConnection("192.168.101.62")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        rightButton.setOnTouchListener(onTouch)
        // TODO Register OnTouchListener for other buttons
    }

    private val onTouch: (View,  MotionEvent) -> Boolean = { view, motionEvent ->
        val direction = when (view) {
            // TODO Handle other buttons
            rightButton -> Direction.RIGHT
            else -> Direction.BACKWARD
        }

        when (motionEvent.actionMasked) {
            MotionEvent.ACTION_DOWN -> {
                Toast.makeText(this, "Pressed ${resources.getResourceEntryName(view.id)}", Toast.LENGTH_SHORT).show()
                // TODO Call the robot to start a movement in the desired direction
            }
            MotionEvent.ACTION_UP -> {
                Toast.makeText(this, "Released ${resources.getResourceEntryName(view.id)}", Toast.LENGTH_SHORT).show()
                // TODO Call the robot to stop the movement
            }
        }
        false
    }

    /**
     * Displays a toast message.
     */
    private fun onError(message: String) {
        Toast.makeText(this, message, Toast.LENGTH_LONG).show()
    }
}
