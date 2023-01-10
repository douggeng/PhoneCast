# PhoneCast

A weather push notification updater

## Description

This application uses an api from "Open Weather". With this, my
program grabs the correct city api and converts the measurements
from kelvin/ms to farhenheit/mph. Once all conversions are made, the app sends a push notification to my phone with temperature, windspeeds, humidity, and sky vision. I scheduled the notifications
twice a day at specific times.

## Getting Started

### Video Demo
[![Video](https://img.youtube.com/vi/sg_qU68eMgs/10.jpg)](https://www.youtube.com/watch?v=sg_qU68eMgs)



### Libraries

* Schedule
* Requests
* Time

### Instructions

* Register on https://openweathermap.org/ and grab the weather api key.
* Register on https://www.mynotifier.app/ and grab the notification api key.
* Download myNotifer on iphone appstore
* Enter keys into secret_api_key.
* Change the city string to your city.
* Now change times at top to your desired time and run the program:
```
python main.py
```


## What I learned

* Working with multiple APIs.
* Utilized the Schedule library for automation.
* Created variables from response json library.


## What I want to improve/add

* Adding a UI which allows you to start the application and change times.
* Making a personal iphone app to push the notifications.
