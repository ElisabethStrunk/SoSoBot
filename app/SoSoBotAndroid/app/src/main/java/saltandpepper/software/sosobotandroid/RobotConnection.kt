package saltandpepper.software.sosobotandroid

import com.github.kittinunf.fuel.core.FuelManager
import com.github.kittinunf.fuel.httpGet
import java.lang.Exception

class RobotConnection(ipAddress: String) {

    private val mVelocityFull = 1.0f
    private val mVelocityStop = 0.0f

    init {
        FuelManager.instance.basePath = "http://$ipAddress"
    }

    /**
     * @param velocity A value between `0.0` (stop) and `1.0` (full speed). Defaults to `1.0`.
     */
    fun move(direction: Direction, velocity: Float = mVelocityFull, onError: ((message: String) -> Unit)? = null) {
        request("move/$direction/$velocity", onError)
    }

    fun stop(direction: Direction, onError: ((message: String) -> Unit)? = null) {
        move(direction, mVelocityStop, onError)
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