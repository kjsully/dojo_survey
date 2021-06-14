from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")



@app.route('/result', methods=['POST'])
def users():
    print('Got Post Info')
    print(request.form)

    return render_template(
        'success.html',
        name = request.form['name'],
        location = request.form['location'],
        language = request.form['language'],
        comments = request.form['comments']
        )




if __name__ == "__main__":
    app.run(debug=True)

