package saltandpepper.software.sosobotandroid

import com.github.kittinunf.fuel.core.FuelManager
import com.github.kittinunf.fuel.httpGet
import java.lang.Exception

class RobotConnection(ipAddress: String) {

    init {
        FuelManager.instance.basePath = "http://$ipAddress"
    }

    fun move(direction: Direction, power: Byte = 100, onError: ((message: String) -> Unit)? = null) {
        request("/$direction/on/$power", onError)
    }

    fun stop(direction: Direction, onError: ((message: String) -> Unit)? = null) {
        request("/$direction/off/0.0", onError)
    }

    private fun request(path: String, onError: ((message: String) -> Unit)? = null) {
        try {
            path.httpGet().timeout(2000).responseString { result ->
                result.component2()?.also {
                    onError?.invoke("Status: ${it.response.statusCode} > ${it.localizedMessage}")
                }
            }
        } catch (exception: Exception) {
            onError?.invoke(exception.localizedMessage)
        }
    }
}