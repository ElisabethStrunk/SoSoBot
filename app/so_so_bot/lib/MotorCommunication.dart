import 'dart:io';
import 'direction.dart';

class MotorCommunication {

  String ipAddress;

  HttpClient client = new HttpClient();

  MotorCommunication(this.ipAddress);

  void move(Direction direction, {double velocity = 1.0}) {
    request(direction, velocity);
  }

  void stop(Direction direction) {
    request(direction, 0.0);
  }

  Uri buildUri(Direction direction, double velocity) {
    return Uri.parse("http://$ipAddress/move/$direction/$velocity");
  }

  void request(Direction direction, double velocity) { // todo on error lambda
    var uri = buildUri(direction, velocity);
    client.getUrl(uri).then((request) {
      print(request);
      return request.close();
    }).then((response) {
      print(response);
      // TODO handle response
    });
  }
}