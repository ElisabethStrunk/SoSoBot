package saltandpepper.software.sosobotandroid

import com.github.kittinunf.fuel.core.FuelManager
import com.github.kittinunf.fuel.httpGet

class RobotConnection(ipAddress: String) {

    private val onPath = "/on/100.0"
    private val offPath = "/off/0.0"

    init {
        FuelManager.instance.basePath = "http://$ipAddress"
    }

    fun move(direction: Direction, power: Byte = 100) {
        // TODO update request for power parameter
        request("/$direction", true)
    }

    fun stop(direction: Direction) {
        request("/$direction", false)
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