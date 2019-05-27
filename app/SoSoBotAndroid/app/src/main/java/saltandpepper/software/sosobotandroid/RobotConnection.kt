package saltandpepper.software.sosobotandroid

import com.github.kittinunf.fuel.core.FuelManager
import com.github.kittinunf.fuel.httpGet

class RobotConnection(ipAddress: String) {

    init {
        FuelManager.instance.basePath = "http://$ipAddress"
    }

    fun move(direction: Direction, power: Byte = 100) {
        request("/$direction/on/$power")
    }

    fun stop(direction: Direction) {
        request("/$direction/off/0.0")
    }

    private fun request(path: String) {
        // TODO handle exception
        path.httpGet().responseString {
                result ->
        }
    }
}