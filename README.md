# Child Care Tracker
Internal codename: cricket


### Required modules
* asgiref==3.3.4
* cachetools==4.2.1
* certifi==2020.12.5
* chardet==4.0.0
* click==7.1.2
* Django==3.1.7
* django-background-tasks==1.2.5
* django-compat==1.0.15
* django-crispy-forms==1.11.2
* django-phone-field==1.8.1
* django-widget-tweaks==1.4.8
* google-api-core==1.26.3
* google-auth==1.29.0
* google-cloud==0.34.0
* google-cloud-texttospeech==2.3.0
* googleapis-common-protos==1.53.0
* grpcio==1.37.0
* gTTS==2.2.2
* idna==2.10
* packaging==20.9
* proto-plus==1.18.1
* protobuf==3.15.8
* pyasn1==0.4.8
* pyasn1-modules==0.2.8
* pycairo==1.20.0
* pygame==2.0.1
* pyparsing==2.4.7
* python-dotenv==0.17.0
* pytz==2021.1
* PyYAML==5.4.1
* requests==2.25.1  
* rsa==4.7.2
* six==1.15.0
* sqlparse==0.4.1
* typing-extensions==3.7.4.3
* urllib3==1.26.4


### Project Milestones

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
- ~~[] Design and/or print case for wall mountable~~
- [x] Create speech to text module for easier inputting of data
- [x] TSS to read out tasks when they come due.
- [x] Validate speech to text for accuracy. I’ll have everyone in my household try it
- [x] Redo dateTime fields as seperate date and time for tasks and supplies
- [x] Build out secondary device (it will just be web-based client, so it just needs to be built and configured)
- [x] Final testing and troubleshooting of full deployment
