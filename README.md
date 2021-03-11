# Child Care Tracker
Internal codename: cricket

### Notes
Activate virtual environment with cct
Run dev server with runCCT

### Required modules
django
python-dotenv
django-phone-field
django-bootstrap-v5
django-bootstrap-modal-forms

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
- [] Create input form to add to the daily schedule
- [] Validate that home page navigates to daily schedule and input form and that data can be added and deleted

#### Mon Mar 1, 2021
- [x] Create the meds and supplies tracker page
- [] Create input form to add meds and supplies
- [] Code the messaging system to send a reminder to designated users
- [] Create page to manage designated users to alert
- [] Validate that home page navigates to supply tracker and users, that data can be added and deleted for each

#### Mon Mar 22, 2021
- [] Create monthly calendar to track appointments.
- [] Create input form to add to calendar
- [] Validate monthly calendar, input and deletion
- [] Deploy everything up to this point to production webserver software (Apache) running on Raspberry Pi to ensure it works as intended

#### Mon Apr 5, 2021
- [] Continue testing and troubleshooting production level deployment
- [] Design and/or print case for wall mountable
- [] Create speech to text module for easier inputting of data
- [] Validate speech to text for accuracy. I’ll have everyone in my household try it
- [] Build out secondary device (it will just be web-based client, so it just needs to be built and configured)
- [] Final testing and troubleshooting of full deployment
