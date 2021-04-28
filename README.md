# Child Care Tracker
Internal codename: cricket
Web app designed for a raspberry pi based tablet for aiding in the care of a child with special needs.

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Project Milestones](#project-milestones)


## General info
Taking care of a special needs is hard enough with without having to worry about remembering to everything that needs to be done. Cricket will keep track of daily tasks, appointments and supplies so you can focus on more important things.

## Screenshots
![Example screenshot](./img/screenshot.png)

## Technologies
Project is created with:
* Python 3.7
* SqLite3
* Apache2
* WSGI
* Raspberry Pi 4b 2gb 10"/7" monitors
* APScheduler==3.6.3
* asgiref==3.3.1
* cachetools==4.2.1
* certifi==2020.12.5
* chardet==4.0.0
* Django==3.1.7
* django-background-tasks==1.2.5
* django-compat==1.0.15
* django-crispy-forms==1.11.1
* django-phone-field==1.8.1
* django-widget-tweaks==1.4.8
* google-api-core==1.26.3
* google-auth==1.28.0
* google-cloud==0.34.0
* google-cloud-texttospeech==2.3.0
* googleapis-common-protos==1.53.0
* gTTS==2.2.2
* idna==2.10
* lazy-object-proxy==1.5.2
* playsound==1.2.2
* proto-plus==1.18.1
* protobuf==3.15.7
* python-dotenv==0.15.0
* pytz==2021.1
* requests==2.25.1
* rsa==4.7.2
* six==1.15.0
* SpeechRecognition==3.8.1
* sqlparse==0.4.1
* tzlocal==2.1
* urllib3==1.26.4
* wrapt==1.12.1
	
## Setup
To run this project, clone the project:

```
$ git clone
$ cd cricket
```

Generate a new secret key:

```
$ python -c "import secrets; print(secrets.token_urlsafe())"
```

If running the local dev server paste the new secret key into the cricket/cricket/settings.py file 

```python
SECRET_KEY = [New Key]
```

To keep the secret key private use dotenv package by creating a .env file in the project root that containes SECRET_KEY = [New Key] and leaving the settings.py unchanged.

Install python version 3.8 and required libraries into a virtual environment:

```
$ sudo python3.8
$ pip install venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Run the django development server:

```
$ python manage.py runserver
```

## Features
* Track daily recurring tasks
* Easily track what supplies need to be ordered
* Calendar to track future appointments
* Notifications are sent to your cell phone and spoken by the device

To-do list:
* Refactor views to make things asynchronous
* Ability to turn notifications on/off
* Camera to view child if your in a seperate room
* 2-way audio communication
* Speech to text for easier input
* Better javascript keyboard

## Status
Project is: _in progress_ 

[comment]: <> (_finished_, _no longer continue_ and why?)

## Project Milestones
As this project was started as my senior captsone project I've listed my timeline

#### Mon Feb 1, 2021
- [x] Sketch layout for webapp design and flow
- [x] Design schema for MySQL DB
- [x] Implement schema for MySQL DB
- [x] Setup raspberry pi and install Django, Apache, MySQL and any dependencies
- [x] Validate that Django is working and can communicate with MySQL

#### Mon Feb 15, 2021
- [x] Brush up on Django and JavaScript
- [x] Code home page as a navigation menu
- [x] Create the daily schedule to track breathing treatments, medications and feeds page
- [x] Create input form to add to the daily schedule
- [x] Validate that home page navigates to daily schedule and input form and that data can be added and deleted

#### Mon Mar 1, 2021
- [x] Create the meds and supplies tracker page
- [x] Create input form to add meds and supplies
- [x] Code the messaging system to send a reminder to designated users
- [x] Create page to manage designated users to alert
- [x] Validate that home page navigates to supply tracker and users, that data can be added and deleted for each

#### Mon Mar 22, 2021
- [x] Create monthly calendar to track appointments.
- [x] Create input form to add to calendar
- [x] Validate monthly calendar, input and deletion
- [x] Deploy everything up to this point to production webserver software (Apache) running on Raspberry Pi to ensure it works as intended


#### Mon Apr 5, 2021
- [x] Find js keyboard to use for input
- [x] Added js keyboard
- [x] Continue testing and troubleshooting production level deployment
- ~~Design and/or print case for wall mountable~~
- [x] Create speech to text module for easier inputting of data
- [x] TSS to read out tasks when they come due.
- [x] Validate speech to text for accuracy. I’ll have everyone in my household try it
- [x] Redo dateTime fields as seperate date and time for tasks and supplies
- [x] Build out secondary device (it will just be web-based client, so it just needs to be built and configured)
- [x] Final testing and troubleshooting of full deployment
