
from flask import Flask, render_template, request, url_for
#flask - fow WSGI class
#render_template - to render template
import random

 

app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/', methods = ['GET'])
def home():
    return render_template("home.html")

@app.route('/operation_result/', methods = ['POST'])
def operation_result():
    first_input = request.form['input1']
    second_input = request.form['input2']
    third_input = request.form['input3']

    try:
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

        return render_template('home.html',
                                Input1=Input1,
                                Input2=Input2,
                                Input3=Input3,
                                result = dummy_password,
                                password_generation = True)


    except:
        dummy_password = "compilation failed."
        return render_template('home.html',
                                Input1=Input1,
                                Input2=Input2,
                                Input3=Input3,
                                result = dummy_password,
                                password_generation = False)
    # return render_template("about.html")

@app.route("/about")
def about():
    return render_template("about.html")

 
# main driver function
if __name__ == '__main__':
    app.run(debug=True)
# run() method of Flask class runs the application
# on the local development server.