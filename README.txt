Max Chalfin : SI 106 FINAL PROJECT README

You may submit this .txt file edited, or a .PDF if you want to format it more.

Project_Option: "iTunes Playlist"

Files (by name) that are included in my submission include:
    - Final_Project.py 
    - playlist_file.json


Python modules that must be pip installed in order to run the code include importing requests,the json module, and the IPython modules that come with Python 3.  Therefore, in order to run the code, Python 3 is required.

- In order to run the code, run python Final_Project.py
- When run, there will be a prompt asking you to enter an artist(music). You'll definitely get good data if you enter the artist 'coldplay', but you can try anything.
- Follow the instructions provided as you progress through the code, in terms of the options of your response.
- If you happen to restart the code, but you want your playlist from when you previously ran the code, enter playlist and the songs tht were previously added will appear along with the new additions.
    

REQUIREMENTS LIST 
- Data from at least one REST APIs (Lines 28-31)
- Define at least 2 classes (Lines 6-19 & 22-44)
  - Each class must have
    - A constructor
    - An __str__ method
    - At least one additional method
    - At least 3 instance variables that might be set in each instance
  - You must create at least 1 instance of each class you define
  - You must use each instance of the classes you create:
    - Your code must invoke the string method and the additional method for each
- Code creates a .json file that is clearly structured for output
    - Through Pretty Print, the code becomes easily readable by a human being
    - **Only updates the playlist_file.json file after user types 'exit'
   

- Borrowed code from question 8 on Problem Set 9, in order to incorperate the request module and the IPython module to output images --> in this case print out the cover art
- Borrowed code from https://docs.python.org/2/library/json.html# to figure out how to create the playlist file that is updated after each time it's called

As a result of my code running, it will create a JSON file that holds all the information about each song added to the playlist.  Furthermore, it will contain a list of dictionaries that includes: the song title, artist, link to the cover art, along with the link to the 30 second snipped of the song.  In other words, when running the code, the user will have the opportunity to input an artist in which will fetch songs from itunes using the itunes API and will prompt the user to either add that song to a playlist(yes/no) or back(ask for another artist, exit, or print the playlist).  
