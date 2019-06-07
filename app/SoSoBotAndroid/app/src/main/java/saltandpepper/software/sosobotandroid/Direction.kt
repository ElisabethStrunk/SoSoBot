package saltandpepper.software.sosobotandroid

enum class Direction {
    // TODO Add other directions
    BACKWARD, RIGHT;

    override fun toString(): String{
        return when (this) {
            RIGHT -> "right"
            else -> TODO("Add strings for other directions")
        }
    }
}