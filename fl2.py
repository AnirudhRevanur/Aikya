from flask import Flask, render_template, request, redirect
import json


app = Flask(__name__)


p = [{"p":"kkk"}]

@app.route('/', methods=['GET','POST'])
def hello():
    ngos = [{'name':'NGO 1', 'details':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt, esse.'},
            {'name':'NGO 2', 'details':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt, esse.'}
            ]
    return render_template('base.html',ngos=ngos)
def input_page():
    # post = [{'p':'klk'}]
    global p
    if request.method == 'POST':
        title = request.form["title"]
        print('--------------')
        print(title)
        print('----------------')

        p = p.append({'title':title})
        return redirect('/')
    else:
        print('====================')
        print(p)
        print('============================')
        p = [{'p':'kkk'}]
        print('00000000000000000000000000000000')
        return render_template('base.html',post=p)


if __name__ == '__main__':
    app.run(debug=True)