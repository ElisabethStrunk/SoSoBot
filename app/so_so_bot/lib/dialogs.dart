import 'package:flutter/material.dart';

class IpAddressDialog extends StatelessWidget {

  IpAddressDialog({this.onOkPressed, this.onCancel});

  final Function(String) onOkPressed;
  final VoidCallback onCancel;

  @override
  Widget build(BuildContext context) {
    return ipAddressDialog(context);
  }

  Widget ipAddressDialog(BuildContext context) {
    String enteredAddress;
    return SimpleDialog(
      title: Text("Enter the server IPv4 address"),
      children: <Widget>[
        SimpleDialogOption(
          child: TextField(onChanged: (value) => enteredAddress = value,),
        ),
        SimpleDialogOption(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: <Widget>[
              FlatButton(
                child: Text("Cancel"),
                onPressed: () => onCancel(),
              ),
              FlatButton(
                child: Text("OK"),
                onPressed: () => onOkPressed(enteredAddress),
              ),
            ],
          ),
        ),
      ],
    );
  }
}