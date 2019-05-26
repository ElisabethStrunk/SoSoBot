package saltandpepper.software.sosobotandroid

import com.github.kittinunf.fuel.core.FuelManager
import com.github.kittinunf.fuel.httpGet

class RobotConnection(ipAddress: String) {

    enum class Direction {
        FORWARD, BACKWARD, LEFT, RIGHT;

        fun asPath(): String = "/" + toString()

        override fun toString(): String{
            return when (this) {
                FORWARD -> "forward"
                BACKWARD -> "backward"
                LEFT -> "left"
                RIGHT -> "right"
            }
        }
    }

    private val onPath = "/on/100.0"
    private val offPath = "/off/0.0"

    init {
        FuelManager.instance.basePath = "http://$ipAddress"
    }

    fun move(direction: Direction) {
        request(direction.asPath(), true)
    }

    fun stop(direction: Direction) {
        request(direction.asPath(), false)
    }

    private fun pathForBool(isOn: Boolean): String = if (isOn) onPath else offPath

    private fun request(path: String, isOn: Boolean) {
        val requestPath = path + pathForBool(isOn)
        // TODO handle exception
        requestPath.httpGet().responseString {
                result ->
        }
    }
}