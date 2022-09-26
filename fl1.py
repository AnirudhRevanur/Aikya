from flask import Flask, render_template, request, redirect
import json


app = Flask(__name__)

def write_json(new_data, filename='donor.json'):
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
# def hello():
#     with open('donor.json') as json_file:
#         data  = json.load(json_file)

#     ngos = [{'name':'NGO 1', 'details':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt, esse.'},
#             {'name':'NGO 2', 'details':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt, esse.'}
#             ]
#     return render_template('base.html',post=data)
def input_page():
    # post = [{'p':'klk'}]
    global p
    if request.method == 'POST':
        title = request.form["title"]
        title1 = {'title':title}
        write_json(title1)
        print('--------------')
        print(title)
        print('----------------')

        return redirect('/')
    else:
        with open('donor.json') as json_file:
            data  = json.load(json_file)
        return render_template('base.html',post=data)


if __name__ == '__main__':
    app.run(debug=True)