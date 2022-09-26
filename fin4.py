from sys import _current_frames
from flask import Flask, render_template, request, redirect
from serpapi import GoogleSearch
import trycourier as tc
import json


app = Flask(__name__)


name = ''
email = ''

def write_json(new_data, filename='don1.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        # print(file_data)
        # print(type(file_data))


@app.route('/', methods=['GET','POST'])
def home():
    global email
    global name
    name=''
    email=''
    return render_template('home1.html')



@app.route('/sign_in', methods=['GET','POST'])
def signin_page():
    global name
    global email
    if request.method == 'POST':
        match = 0
        curr_password = request.form["password"]
        curr_email = request.form["email"]
        with open('don1.json') as json_file:
            data  = json.load(json_file)

        with open('ngoj.json') as json_file:
            data_ngo  = json.load(json_file)

        for i in data:
            if i["email"] == curr_email and i["password"] == curr_password:
                match = 1
                # name=curr_name
                email=curr_email
                return redirect('/')

        for i in data_ngo:
            if i["email"] == curr_email and i["password"] == curr_password:
                match = 1
                return redirect('/')
            else:
                return redirect('/sign_in')
        
    else:
        with open('don1.json') as json_file:
            data  = json.load(json_file)
        return render_template('signup.html',post=data)

@app.route('/sign_ngo', methods=['GET','POST'])
def signin_ngo():
    if request.method == 'POST':
        match = 0
        curr_password = request.form["password"]
        curr_email = request.form["email"]
        with open('ngoj.json') as json_file:
            data  = json.load(json_file)

        for i in data:
            if i["email"] == curr_email and i["password"] == curr_password:
                match = 1
                return redirect('/')
            else:
                return redirect('/sign_ngo')
        
    else:
        with open('donor.json') as json_file:
            data  = json.load(json_file)
        return render_template('signup2.html',post=data)


@app.route('/sign_up', methods=['GET','POST'])
def signup_page():
    global name
    global email
    if request.method == 'POST':
        match = 0
        curr_name = request.form["name"]
        # name=curr_name
        curr_usrname = request.form["username"]
        curr_phno = request.form["phno"]
        curr_add = request.form["add"]
        curr_password = request.form["password"]
        curr_email = request.form["email"]
        # email=curr_email
        new_user = {'name':curr_name, "username":curr_usrname, "phno":curr_phno, "add":curr_add, "password":curr_password, "email":curr_email}
        write_json(new_user)
        with open('don1.json') as json_file:
            data  = json.load(json_file)

        return redirect('/')

        # for i in data:
        #     if i["email"] == curr_email and i["password"] == curr_password:
        #         match = 1
        #         return redirect('/')
        #     else:
        #         return redirect('/sign_in')
        
    else:
        with open('donor.json') as json_file:
            data  = json.load(json_file)
        return render_template('user.html',post=data)


@app.route('/sign_upngo', methods=['GET','POST'])
def signup_ngo():
    if request.method == 'POST':
        match = 0
        curr_name = request.form["name"]
        curr_phno = request.form["phno"]
        curr_add = request.form["add"]
        curr_password = request.form["password"]
        curr_email = request.form["email"]

        params = {
        "api_key": "17c5b1871ac410368c258a7985181f724a0c2da4737664bab80710da79dc7421",
        "engine": "google_maps",
        "type": "search",
        "google_domain": "google.com",
        "q": curr_name,
        "hl": "en",
        }

        search = GoogleSearch(params)
        results = search.get_dict()



        new_user = {'name':curr_name, "phno":curr_phno, "add":curr_add, "password":curr_password, "email":curr_email, "loc":results["search_metadata"]["google_maps_url"]}
        write_json(new_user,'ngoj.json')
        with open('ngoj.json') as json_file:
            data  = json.load(json_file)

        return redirect('/sign_upngo')

        # for i in data:
        #     if i["email"] == curr_email and i["password"] == curr_password:
        #         match = 1
        #         return redirect('/')
        #     else:
        #         return redirect('/sign_in')
        
    else:
        with open('ngoj.json') as json_file:
            data  = json.load(json_file)
        return render_template('ngo.html')


@app.route('/ngo_list', methods=['GET','POST'])
def ngolist():
    global email
    if request.method == 'POST':
        client = tc.Courier(auth_token="pk_prod_ATMP66V9TF4A2BM0DRSXV7TWWP8J")
        curr_details = request.form["details"]
        resp = client.send_message(
            message={
              "to": {
                "email": "adithyag020@gmail.com"
              },
              "content": {
                "title": "Donation Alert!",
                "body": "{{joke}}"
              },
              "data":{
                "joke": "You are recieving " + curr_details
                
              }
            }
          )

        # curr_details = request.form["details"]  

        new_user = {"details":curr_details}
        write_json(new_user,'details.json')
        with open('details.json') as json_file:
            data  = json.load(json_file)      

        return redirect('/ngo_list')
    else:
        with open('ngoj.json') as json_file:
            data  = json.load(json_file)    
        return render_template('charity_form.html', ngos=data)


@app.route('/giving', methods=['GET','POST'])
def giving():
    return render_template('giving.html')


if __name__ == '__main__':
    app.run(debug=True)