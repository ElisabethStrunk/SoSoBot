package saltandpepper.software.sosobotandroid

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View

class MainActivity : AppCompatActivity() {

    private val robotConnection = RobotConnection("192.168.101.62")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun onForwardButtonPressed(view: View) {
        robotConnection.forward(true)
    }

    fun onBackwardButtonPressed(view: View) {
        robotConnection.backward(true)
    }

    fun onLeftButtonPressed(view: View) {
        robotConnection.left(true)
    }

    fun onRightButtonPressed(view: View) {
        robotConnection.right(true)
    }
}
