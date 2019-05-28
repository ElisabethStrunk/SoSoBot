package saltandpepper.software.sosobotandroid

import com.github.kittinunf.fuel.core.FuelManager
import com.github.kittinunf.fuel.httpGet

class RobotConnection(ipAddress: String) {

    private val forwardPath = "/forward"
    private val backwardPath = "/backward"
    private val leftPath = "/left"
    private val rightPath = "/right"

    private val onPath = "/on/100.0"
    private val offPath = "/off/0.0"

    init {
        FuelManager.instance.basePath = "http://$ipAddress"
    }

    fun forward(isOn: Boolean) {
        request(forwardPath, isOn)
    }

    fun backward(isOn: Boolean) {
        request(backwardPath, isOn)
    }

    fun left(isOn: Boolean) {
        request(leftPath, isOn)
    }

    fun right(isOn: Boolean) {
        request(rightPath, isOn)
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