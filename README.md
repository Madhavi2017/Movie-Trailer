# Movie-Trailer
The Movie Trailer Website project consists of server-side code to store a list of movies titles, along with its respective box art imagery and movie trailer website. The data is served as a web page allowing visitors to watch the trailers
## Getting started
These instructions will help you to run the project on your local computer. See deployment for notes on how to deploy the project on a live system.
### Installation and Execution
Install python on your computer from https://www.python.org/downloads/
To confirm that your installation was successful, open IDLE (python GUI), a program installed by Python that makes it easy to edit and run Python code. After the successful installation of python on your system, check with the basic commands like,
```
>>> print "Maggie"	# prints the string							
Maggie  
```
Python itself comes with an editor that you can access from the IDLE File > New File menu option.
Write the code in that file, save it as [filename].py and then (in that same file editor window) press F5 to execute the code you created in the IDLE Shell window.

#### Using command prompt
command line python in windows, save your file with .py extension. Now open command prompt and and change the current directory to python existing directory using the command
```
>cd C:\Python27
```
try this
```
C:\Python27>python
```
if you get the python version and message then your python is succesfully installed and python path is added to your system
```
C:\Python27>python
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
If you get this message, then python isn't on your path
'python' is not recognized as an internal or external command, operable program or batch file.
Putting Python In Your Path
```
My Computer > Properties > Advanced System Settings > Environment Variables > system variables -> Path
```
This needs to include: C:\Python26; (or equivalent). If you put it at the front, it will be the first place looked. You can also add it at the end.Then restart your prompt, and try typing 'python'. If it all worked, you should get a ">>>" prompt.

### Procedure
open a new file and save with .py extension such that it represents a python file. And follow the instructions as given below:
Create a class named Movie remember class name should start with a capital letter
```
class Movie (): 	# to store the movie name title story and trailer
```
Create an instance for Movie class that includes name story trailer and poster, which allocates memory for the Movie class. The __init__ function is called a constructor, or initializer, and is automatically called when you create a new instance of a class. Within that function, the newly created object is assigned to the parameter self.
```
def   __init__ (self, arg1, arg2,  ..): 
```
In __init__ method self refers to the newly created object, in other class methods, it refers to the instance whose method was called.
```
def   __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
        	self.title = movie_title			# instance  or object  is created
        	self.story = movie_storyline
       	  	self.poster_image_url = poster_image
        	self.trailer_youtube_url = trailer_youtube
```
After the creation of instances here we need to pass the values to class, and that can be done as given below, and follow the proper syntax in order to eliminate errors. Tab and spaces plays a major role in python if not placed properly it throws an error like expected indented block
```
got = Movie ("Game of Thrones",
                      "A Game of Thrones is the first novel"
                      " in A Song of Ice and Fire,"
                      "a series of fantasy novels by American"
                      " author George R. R. Martin. It was"
                      " first published on August 1, 1996.",
                      "http://www.hollywoodreporter.com/sites/default"
                      "/files/2011/03/got_-_official_poster.jpg",
                      "https://www.youtube.com/watch?v=Stw6INIS570")
```
Here I have passed the values and created instance got now in order to print the storyline of got used the command and the corresponding output in the python shell will be
```
print (got.storyline)
>>>
A Game of Thrones is the first novel in A Song of Ice and Fire, a series of fantasy novels by American author George R. R. Martin. It was first published on August 1, 1996.
>>>
```
Similarly, for title we get the title of our movie in shell
In order to play the trailer and show the poster of our movie we have to define a method like show trailer and show poster
```
def showtrailer (self):
	webbrowser.open (self.trailer_youtube_url)
```
web browser is not present in python standard library hence we have to import web browser at the beginning of our program like
```
import webbrowser

got.showtrailer ( )	#we are calling the show trailer function hence it plays the trailer 
```
Hence, we have defined all the functions for our movie similarly we can repeat that for other movies as well just by creating instances and passing the required information, here I have created an object for flash similarly we can repeat it for others
We have to create multiple instances of that Python Class to represent our favourite movies flash, now, baby’s, suits, ratatouille. And group all the instances together in a list.
```
# list of movies (grouping all the instances together)
movies = [got, flash, suits, now, ratatouille, baby]
```
To generate a website that displays these movies, I have provided with a starter code repository that contains a Python module called fresh_tomatoes.py. we have to import the fresh_tomatoes module in our python code. The fresh_tomatoes.py module has a function called open_movies_page that takes in one argument, which is a list of movies, and creates an HTML file which will display all of our favourite movies.
```
# open movies list and takes in the list of movies
fresh_tomatoes.open_movies_page(movies)
```
I have created the class Movie and created instances for that in the same file, in order to make it clear, create a list of these movie objects and save it another file entertainment_center.py and by calling the constructor media.Movie()  we can instantiate movie objects, and this list of movies is given as input to open_movies_page() function to build the HTML file and display our website
### Run the program
once we finish writing the code save the file and run the module as go to run and click run module-F5 and finally it displays our movie trailer website or we can run in command prompt as mentioned in the installation process like
```
C:\Python27>cd C:\Python27\project1
C:\Python27\project1>entertainment.py
```
This opens our project output window(Movie trailer website).This tells about the sucessful execution of our project



