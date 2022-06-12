# Awards Clone

## Description
This is a web application developed using Django framework. This app allows users to register and share their projects of choice. Once a user has posted the project to be reviewed, the app is reviewed in three categories Content,Usability and Design.

## Technologies
The project is created with:
* HTML:5 for giving the structure of the webpage.
* CSS:3 for styling the webpage.
* Bootstrap for more styling of the webpage.
* Python Django for the functionality.

## Setup/Installation Requirements
* A PC mainly with an Operating system.
* Python3.6 or later is installed in your PC.
* Postgresql installed
* clone the repository into your local machine **(https://github.com/VaniliKate/weekthree-django.git)**
* navigate to the cloned folder by `cd weekthree-django`
* Create a virtual environment
* run `source virtual/bin/activate`
* install Django `pip install django=1.11`
* pip install `requirements.txt`
* run `python3.6 manage.py runserver `
* The application should work
* for the test run `python manage.py test award`

### Behaviour Driven Development
* The program should return all projects on the directories page<br>
Given:All projects<br>
When: Url is changed to directory page<br>
Then: All projects are displayed<br>

* Admin site should be displayed when "admin/" url is chosen<br>
Given: An admin url<br>
When: User enters admin url in browser<br>
Then: Admin Login is displayed<br>

* User authentication occurs when Admin tries to Login<br>
Given:Admin page is accessed<br>
When: User tries to login<br>
Then: User details are authenticated to confirm if user is an admin<br>

* User session should end when logout url is chosen<br>
Given:Logout option is given<br>
When: User chooses logout option<br>
Then: User session is ended<br>