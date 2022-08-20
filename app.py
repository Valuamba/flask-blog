from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + " - " + str(id)

#http://localhost:5000/user-details?name=sergei&id=20
# https://
# www.google.com
# /search
# ?
# q=codeforces&
# sxsrf=ALiCzsZEA1c-3OP3JCpVP_mZ_vcNeYcf4g%3A1660979498342&
# source=hp&
# ei=KokAY6P8EcWExc8P-M2usAU&iflsig=AJiK0e8AAAAAYwCXOvLyTXHppey12F9Ci0l72jYlAQvO&ved=0ahUKEwijuebn7tT5AhVFQvEDHfimC1YQ4dUDCAY&
# uact=5&
# oq=codeforces&
# gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBQgAEIAEMgUIABCABD
# sclient=gws-wiz
@app.route('/user-details')
def user(name, id):
    name = request.args.get('name')
    id = request.args.get('id')
    return "User page: " + name + " - " + str(id)


# Check if the main file to run
if __name__ == "__main__":
    app.run(debug=True)
