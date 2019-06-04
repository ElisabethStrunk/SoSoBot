import 'dart:io';

class MotorCommunication {

  String ipAddress;

  HttpClient client = new HttpClient();

  MotorCommunication(this.ipAddress);

  void forward(bool on) {
    request(ServerPaths.forwardPath, on);
  }

  void backward(bool on) {
    request(ServerPaths.backwardPath, on);
  }

  void left(bool on) {
    request(ServerPaths.leftPath, on);
  }

  void right(bool on) {
    request(ServerPaths.rightPath, on);
  }

  Uri buildUri(String path, bool on) {
    return Uri.parse("http://" + ipAddress + path + "/" + (on ? "on" : "off"));
  }

  void request(String path, bool on) {
    client.getUrl(buildUri(path, on)).then((request) {
      print(request);
      return request.close();
    }).then((response) {
      print(response);
      // TODO handle response
    });
  }
}

class ServerPaths {
  static const String forwardPath = "/forward";
  static const String backwardPath = "/backward";
  static const String leftPath = "/left";
  static const String rightPath = "/right";
}