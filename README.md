
# AirBnB Clone

AirBnB is a complete web application, integrating database stoarage, a backend API and front end interface

This is part 1 of our AirBnb Clone Project.
The purpose of this project is to make a command intrepreter that manages AirBnB Objects


# Concepts Learned
    How to create a Python package
    How to create a command interpreter in Python using the cmd module
    What is Unit testing and how to implement it in a large project
    How to serialize and deserialize a Class
    How to write and read a JSON file
    How to manage datetime
    What is an UUID
    What is *args and how to use it
    What is **kwargs and how to use it
    How to handle named arguments in a function

# Synopsis
  The Commandline Interpreter can be started by executing the command ./console.py. The console can create, destroy, and     update objects. Type help within the console to get a list of command options and its function.

 ## Example
    abrham@ubuntu:~$ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit

    Undocumented commands:
    ======================
    all  destroy  show  update

    (hbnb) help quit
    Quit command to exit the program
    (hbnb) quit
    abrham@ubuntu:~$
    
## File Structure
      Airbnb_Clone\
                   models\
                          __init__.py
                          engine\
                                  __init__.py
                                  file_storage.py
                          base_model.py
                          user.py
                          place.py
                          city.py
                          review.py
                          state.py
                          amenity.py
                          
                   tests\
                          __init__.py
                          test_models\
                                      __init.py
                                      test_engine\
                                                  __init__.py
                                                  test_file_storage
                                      test_base_model.py
                                      test_city.py
                                      test_place.py
                                      test_review.py
                                      test_user.py
                                      test_amenity.py
                   README.md
  
# AUTHORS
Abrham Gebregiorgis & Stephanie
