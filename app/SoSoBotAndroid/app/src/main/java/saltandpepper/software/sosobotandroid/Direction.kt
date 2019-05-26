package saltandpepper.software.sosobotandroid

enum class Direction {
    FORWARD, BACKWARD, LEFT, RIGHT;

    override fun toString(): String{
        return when (this) {
            FORWARD -> "forward"
            BACKWARD -> "backward"
            LEFT -> "left"
            RIGHT -> "right"
        }
    }
}