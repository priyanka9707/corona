from flask import Flask, render_template
from flask import Flask, flash, redirect, render_template, \
     request, url_for
app = Flask(__name__)
@app.route("/")
def hello():

    return render_template('index.html')

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is

@app.route("/about")
def harry():
    name = "rohan das"
    return render_template('about.html', name2= name)

@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')

app.run(debug=True)