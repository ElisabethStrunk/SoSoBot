import 'package:flutter/material.dart';
import 'package:so_so_bot/dialogs.dart';
import 'MotorCommunication.dart';
import 'direction.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SoSoBot',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // The application is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'SoSoBot Controller'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  // TODO widget for IP address
  MotorCommunication motorCommunication = new MotorCommunication("192.168.101.62");
  
  void onPopupMenuSelected(int index) {
    if (index == 0) {
      showDialog(context: context, barrierDismissible: false, builder: (context) {
        return IpAddressDialog(
            onOkPressed: (ip) {
              motorCommunication.ipAddress = ip;
              Navigator.pop(context);
            },
            onCancel: () {
              Navigator.pop(context);
            });
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called.
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        actions: <Widget>[
          PopupMenuButton<int>(
            offset: Offset(0, 48),
            onSelected: onPopupMenuSelected,
            itemBuilder: (context) => <PopupMenuEntry<int>>[
              const PopupMenuItem<int>(
                value: 0,
                child: Text("Set IP adress"),
              ),
            ],
          )
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.only(left: 8, right:8),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.end,
          children: <Widget>[
            // Forward
            GestureDetector(
              onTapDown: (_) => motorCommunication.move(Direction.FORWARD),
              onTapCancel: () => motorCommunication.stop(Direction.FORWARD),
              child: RaisedButton(
                child: Icon(Icons.keyboard_arrow_up),
                onPressed: () => motorCommunication.stop(Direction.FORWARD),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: <Widget>[
                // Left
                GestureDetector(
                  onTapDown: (_) => motorCommunication.move(Direction.LEFT),
                  onTapCancel: () => motorCommunication.stop(Direction.LEFT),
                  child: RaisedButton(
                    child: Icon(Icons.keyboard_arrow_left),
                    onPressed: () => motorCommunication.stop(Direction.LEFT),
                  ),
                ),
                // Right
                GestureDetector(
                  onTapDown: (_) => motorCommunication.move(Direction.RIGHT),
                  onTapCancel: () => motorCommunication.stop(Direction.RIGHT),
                  child: RaisedButton(
                    child: Icon(Icons.keyboard_arrow_right),
                    onPressed: () => motorCommunication.stop(Direction.RIGHT),
                  ),
                ),
              ],
            ),
            // Backward
            GestureDetector(
              onTapDown: (_) => motorCommunication.move(Direction.BACKWARD),
              onTapCancel: () => motorCommunication.stop(Direction.BACKWARD),
              child: RaisedButton(
                child: Icon(Icons.keyboard_arrow_down),
                onPressed: () => motorCommunication.stop(Direction.BACKWARD),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
