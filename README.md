# Random_password_generator
This is a basic project of python programming language. Here we will get to know about the basic of Flask env. and some basic concept of List, for loop and html request.
---------------------------------------------------------------------------------
# About Project - 
As the name suggests this is the introductry of Python Flask project.
I have implemented basic concepts of Http request, Random library, list, for loop and starting with Flask.
In this project we are focused on the logic part not at the User Interface(user interface is importat - later i will improve the UI part too.)
# Let's get started - 
Install any Python IDE, I am using VS code here.
Open the terminal go the location where project is located.
"cd C:\Users\Sxxx5\Desktop\Projects\Password_generator>"
installing virtualenv
# pip install virtualenv
creating python virtual env named as venv
# virtualenv venv
Activating Virtual env.
# for windows - venv\Scripts\activate
Installing Flask
# pip install Flask

# Files
creating a python file named as **app.py**

Refer to files attached.

create a folder named **static** for storing css and javascript.

create a folder named **templates** for storing html files

Refer to files attached.

# logic 

        Input1 = int(first_input)
        Input2 = int(second_input)
        Input3 = int(third_input)

        special_character1 = []
        for i in range(32,48):
            special_character1.append(chr(i))
        
        special_character2 = []
        for i in range(58,65):
            special_character2.append(chr(i))
        
        alpha_upper = []
        for i in range(65,91):
            alpha_upper.append(chr(i))

        alpha_lower = []
        for i in range(97,123):
            alpha_lower.append(chr(i))
        
        numb =[]
        for i in range(48, 58):
            numb.append(chr(i))

        special_character = special_character1 + special_character2
        alpha = alpha_upper + alpha_lower

        rand_alpha_list = []
        for i in range(0,Input1):
            rand_alpha_list.append(random.choice(alpha))
        
        rand_special_list = []
        for i in range(0,Input2):
            rand_special_list.append(random.choice(special_character))
        
        rand_num_list = []
        for i in range(0,Input3):
            rand_num_list.append(random.choice(numb))
        
        dummy_password = rand_num_list+rand_alpha_list+rand_special_list
        random.shuffle(dummy_password)
        dummy_password = ''.join(dummy_password)

# see the below output.

![Capture1](https://user-images.githubusercontent.com/26331296/175374925-f3f31714-0e77-49fd-bfb4-86688fea188e.PNG)

![Capture3](https://user-images.githubusercontent.com/26331296/175375190-4427943e-f4ee-4773-b79c-05f5501f2d96.PNG)

![Capture4](https://user-images.githubusercontent.com/26331296/175375216-a79385f2-6f5b-4750-86bb-19f86d08bbf5.PNG)

![Capture2](https://user-images.githubusercontent.com/26331296/175375239-a96ac79a-6dd0-4164-807e-64dcdd617f1f.PNG)


