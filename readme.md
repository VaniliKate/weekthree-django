# Awards Clone

## Description
This is a web application developed using Django framework. This app allows users to register and share their projects of choice. Once a user has posted the project to be reviewed, the app is reviewed in three categories Content,Usability and Design.

## Technologies
The project is created with:
* HTML:5 for giving the structure of the webpage.
* CSS:3 for styling the webpage.
* Bootstrap for more styling of the webpage.
* Python Django for the functionality.

## Installation
* Clone the repository directly to your pc
    https://github.com/VaniliKate/weekthree-django.git
* To be able to run this project on your PC you need to have python already installed Python version 3.6 and above. Incase you dont have it use this commands to install
    $ sudo add-apt-repository ppa:jonathonf/python-3.6
    $ sudo apt-get update
    $ sudo apt-get install python3.6
* Install Python command tool called PIP which comes preinstalled in linux and mac. For linux use this to install pip
    $ sudo apt-get install python3-pip 
* For mac 0S use this command to install pip
    sudo easy_install pip
Open your editor and run the cloned repository and install the modules below to run effectivey.

* To install all requirements and extentions needed to run the app install requirements using

    pip install -r requirements.txt
* To run the class test use the following commands in the terminal
    python3.6 manage.py test
* Now your ready to run the modules type the fillowing commands to run the app locally.
    ./start.sh or python3.6 manage.py server

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