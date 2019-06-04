# SoSoBot

SoSo HH internship project: 
Project for pupil and student interns at SoSo HH (SALT AND PEPPER Software GmbH & Co. KG, Hamburg).
Awesome joint venture of the SoSo HH hardware, embedded and mobile dev teams.

A little car-like robot; controlled by a Raspberry Pi; manually controllable by mobile app via HTTP.

## API

We follow [REST](https://stackoverflow.com/questions/671118/what-exactly-is-restful-programming) ([Quick Tips](https://restapitutorial.com/lessons/restquicktips.html)).
The following paths are defined for the HTTP `GET` method:

- Movement
	- `http://yourBaseUri/move/<direction: string = {left|forward|right|backward}>/<velocity: float = {0.0 ... 1.0}>`
- Horn
	- `http://yourBaseUri/horn/<which: string = {1|2}>`
- Led
	- `http://yourBaseUri/led/<side: string = {left|right}>/<status: string = {on|off}/<frequency: int = {0 ... 10}>`

## Mobile App

There are currently two versions; an Android implementation ([app/SoSoBotAndroid](app/SoSoBotAndroid)) and a Flutter implementation ([app/so_so_bot](app/so_so_bot)).

While implementing the Flutter app we realized that it may be too complicated for beginners to learn mobile development.
In favor of the graphical layout designer and the openness of the Android platform regarding development we switched to Android.