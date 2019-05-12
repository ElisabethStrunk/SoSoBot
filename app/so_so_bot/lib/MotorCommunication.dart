import 'dart:io';

class MotorCommunication {

  String ipAddress;
  String path = "/motor";

  HttpClient client = new HttpClient();

  MotorCommunication(this.ipAddress);

  void startMotor(MotorSite motorSite) {
    var uri = buildUri(motorSite, true);
    request(uri);
  }

  void stopMotor(MotorSite motorSite) {
    var uri = buildUri(motorSite, false);
    request(uri);
  }

  Uri buildUri(MotorSite motorSite, bool on) {
    return Uri.parse(ipAddress + path + "/" + motorSite.toString() + "?on=" + (on ? "1" : "0"));
  }

  void request(Uri uri) {
    client.putUrl(uri).then((request) {
      request.close();
    });
  }
}

class MotorSite {
  static MotorSite left = MotorSite("left");
  static MotorSite right = MotorSite("right");
  static MotorSite both = MotorSite("both");

  String representation;

  MotorSite(this.representation);

  @override
  String toString() {
    return representation;
  }
}