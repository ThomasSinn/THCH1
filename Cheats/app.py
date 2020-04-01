#Python 3.7 controller 
#uberch'eats project

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static/scripts', template_folder='static/pages')

#Home Page
@app.route('/', methods=["GET", "POST"])
def landingPage():
    if request.method == "POST":
        searchtext = request.form.get("search")

        return redirect(url_for('searchPage', searchtext=searchtext))
    else:
        return render_template('index.html')

@app.route('/search/<searchtext>', methods=["GET", "POST"])
def searchPage(searchtext):
    results = ["bruh", "mmmhmmm", "heyyy"]

    return render_template('searchpage.html', results=results)
"""
#should be the actual comparison of the gig economy pricing
@app.route('/store/<storeid>')
def compare():
    return render_template('store.html')
"""
if __name__ == "__main__":
    app.run()
