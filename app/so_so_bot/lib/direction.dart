class Direction extends Object {
  static const Direction FORWARD = Direction._("forward");
  static const Direction BACKWARD = Direction._("backward");
  static const Direction LEFT = Direction._("left");
  static const Direction RIGHT = Direction._("right");

  final String value;

  const Direction._(this.value);

  @override
  String toString() {
    return value;
  }
}