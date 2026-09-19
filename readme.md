# Overview

{This program is a grocery inventory program.}

{The goal of this program is to learn about Google Firestore and
brush up on my Python language skills.}

{Provide a description of the software that you wrote and how it integrates with a Cloud Database. Describe how to use your program.}

{This is designed to store the inventory in your home.  
It will also create a list of items you are out of.
The program connects to the Google Firstore database.
It then collects the information from the database and adds it to a dictionary
The dictionary is then accessed for the program to use it's functions.

The program can also add data to the database, edit data existing in the database and delete
data from the database.}


{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

{Using Google Firebase.  This is Google's cloud based nosql database.}

{One collection: inventory
Fields: 
expiration (string) --decided not to use this field for now, so it has been commented out of the code
location (string)
name (string)
quantity (int64)
upc (string)
}


# Development Environment

{Tools: Visual Studio
Language: Python
Third Party Tools: Firebase Admin
}

# Useful Websites

{Helpful websites:
- W3 Schools: (https://www.w3schools.com/python)
- Geeks for Geeks: (https://www.geeksforgeeks.org/python)
- https://firebase.google.com/docs/firestore
}

# Future Work

{List of things that you need to fix, improve, and add in the future.

- Add UI.
- Review code to see if there is a way to simplify or make it better.
- Update the program / database to provide a list when you are low, not out.
}