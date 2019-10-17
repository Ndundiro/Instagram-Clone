## Instagram-Clone

## Author
Ndundiro Kamau 

## Decription
Instagram-Clone is a platform  where users can share their images for other people.The image can be liked and commented on.Users can follow other users and also get followed by other users.

## Screenshot
<img src="https://github.com/Ndundiro/Instagram-Clone/blob/master/instascreenshot.png" width="1000">

## Live Link 
[lick here](https://insta159.herokuapp.com/) view the live site.

## SetUp/Installations
1. Download the zip file of the project or Clone the repository using the following command:
git clone ```https://github.com/Ndundiro/Instagram-Clone```

Navigate to the project directory
```cd INSTA-AP```

2. Virtual Environment
Install virtualenv  using pip:  
```python3.6 -m venv virtual```  
Proceed to activate the virtual environment   
```source virtual/bin/activate```

3. Install packages/dependancies  
Install the packages in the requirements.txt file:  
```pip install -r requirements.txt```

4. Create a database
Create a new postgress database,Type the following command  
psql  
Run the following command,it creates a new database named gallery1  
```#create database insta```

5. Create Database migrations
run the following command:    
 ```python3 manage.py makemigrations insta```
followed by:    
 ```python3 manage.py migrate```

6. Run the app
To run the application:  
```python3 manage.py runserver``` 

Open  the link http://127.0.0.1:8000/  in a browser.

7. To run tests:  
```python3 manage.py test```

For more Information,Read the following documents:

* [DjangoDocumentation](https://docs.djangoproject.com/en/1.11/)
* [PythonDocumentation](https://docs.python.org/3.6/)

User Story
Sign in to the application to start using.
Upload a pictures to the application.
Search for different users using their usernames.
See your profile with all your pictures.
Follow other users and see their pictures on my timeline.


## Bugs
There are no known bugs yet

## Technologies Used
* Python3.6
* Django 2.20
* PostgreSQL
* HTML5
* CSS3
* Heroku

### Dependencies
* Postgresql

## Support and Contact Details
For any comments,suggestions,feedback or inquiries, contact me via email: ndundirokamau@gmail.com

## License
[MIT License](https://github.com/Ndundiro/Instagram-Clone/blob/master/LICENSE)

Copyright © 2019 Ndundiro Kamau
