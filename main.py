from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <!-- my form -->
        
        <form method="post">
            <label> Rotate by: 
                <input name="rot" type="text" value="0"/>
            </label>

            <label> 
                <textarea name="text">{0}</textarea> 
            </label>
            
            <label>
                <input type="submit"/>
            </label>      
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    return '<h1>' + form.format(rotate_string(text,rot)) + '<h1>'


app.run()

