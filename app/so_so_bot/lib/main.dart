import 'package:flutter/material.dart';
import 'package:so_so_bot/dialogs.dart';
import 'MotorCommunication.dart';

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

  void onTapDownLeft(TapDownDetails details) {
    motorCommunication.left(true);
  }

  void onTapUpLeft() {
    motorCommunication.left(false);
  }

  void onTapDownRight(TapDownDetails details) {
    motorCommunication.right(true);
  }
  
  void onTapUpRight() {
    motorCommunication.right(false);
  }

  void onTapDownForward(TapDownDetails details) {
    motorCommunication.forward(true);
  }

  void onTapUpForward() {
    motorCommunication.forward(false);
  }

  void onTapDownBackward(TapDownDetails details) {
    motorCommunication.backward(true);
  }

  void onTapUpBackward() {
    motorCommunication.backward(false);
  }

  void onTapCanceled() {
    onTapUpLeft();
    onTapUpRight();
    onTapUpBackward();
    onTapUpForward();
  }
  
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
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
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
            GestureDetector(
              onTapDown: onTapDownForward,
              onTapCancel: onTapCanceled,
              child: RaisedButton(
                child: Icon(Icons.keyboard_arrow_up),
                onPressed: onTapUpForward,
              ),
            ),
            Row(
              // Row is a widget that displays its children in a horizontal array.
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: <Widget>[
                GestureDetector(
                  onTapDown: onTapDownLeft,
                  onTapCancel: onTapCanceled,
                  child: RaisedButton(
                    child: Icon(Icons.keyboard_arrow_left),
                    onPressed: onTapUpLeft,
                  ),
                ),
                GestureDetector(
                  onTapDown: onTapDownRight,
                  onTapCancel: onTapCanceled,
                  child: RaisedButton(
                    child: Icon(Icons.keyboard_arrow_right),
                    onPressed: onTapUpRight,
                  ),
                ),
              ],
            ),
            GestureDetector(
              onTapDown: onTapDownBackward,
              onTapCancel: onTapCanceled,
              child: RaisedButton(
                child: Icon(Icons.keyboard_arrow_down),
                onPressed: onTapUpBackward,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
