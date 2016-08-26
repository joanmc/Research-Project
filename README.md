# COMP47360: RESEARCH PRACTICUM
# TEAM 4: OCCUPANTS
# BARRY KIDNEY, JOAN MCCARTHY, DAVID O'KEEFFE & ELLEN RUSHE

SERVER: http://csi420-01-vm4.ucd.ie/

LOGIN CREDENTIALS: 
    - Username: occupants
    - Password: Research2016!

# Repository Contents
    Database: All python files to construct the database
    Modelling Notebooks: All iPython notebooks detainling all stages of the modelling process
    Project File: Web Application - This is the final product that has been deployed on the server
    Signal Strength_RaspberryPi: iPython notebooks detailing additional work undertaken in researching the relation between RSSI and the number of people in a room
    Survey: iPython notebooks detailing analysis undertaken on the repsonses received from the survey that was conducted
    Working_Prototype_Presentation2: Early application prototype presented at Presentation 2 'Current Working Prototype'

# User Instructions
When the user accesses the homepage summary graphs of space utilisation, frequency and occupancy rates are presented to them. Users are also presented with a map of the location of the Computer Science building within UCD. Users also have the option to participate in our survey to help develop the system.  

Users can access the results tab to view historical occupancy results estimated by three Logistic Regression models. Users can select the required room and date to view these results. A graph provides a visualisation of the results and panels alongside the graph provide more detailed results from the models. 

Lecturers and administrative staff have the option to sign up on the navigation bar. Once a new user has received a confirmation email approving their registration the user will then be able to login and to view current data within the database and to upload new data - ground truth, wifi logs, new rooms, timetables and modules. 

# Developer Instructios
The  application backend is written in [Python 3.5](https://docs.python.org/3.4/). [MySQL](https://www.mysql.com/) is used to provide storage of data. The [Django](https://www.djangoproject.com/) framework for web application development. [WSGI](https://wsgi.readthedocs.org/en/latest/) for providing the communications interface between the web app and Python backend. [Apache2](https://httpd.apache.org/) to host the webpages and web app.

The web application frontend is written in [HTML5](https://www.w3.org/TR/html5/) and [Javascript](http://www.ecma-international.org/publications/standards/Ecma-262.htm). [ChartJS](http://www.chartjs.org/) is used to provide visualisations of results.