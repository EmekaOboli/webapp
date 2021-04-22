import csv
from datetime import datetime

from flask import Flask
from flask import redirect
from flask import render_template
# from flask import url_for
from flask import request

app = Flask(__name__, template_folder="templates")


# Class Login( ):
#     def __init__(self, surname, name, age, occupation, username, email, tel_number):
#         self.surname=surname
#         self.name=name
#         self.age=age
#         self.occupation=occupation
#         self.username=username
#         self.email=email
#         self.tel_number=tel_number
#     def __rep__():


@app.route("/")
@app.route("/index.html")
def index():
    print(f"{datetime.now():%d-%m-%y %H:%M:%S}")
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    print(f"{datetime.now():%d-%m-%y %H:%M:%S}")
    return render_template(page_name)


# @app.route("/join community.html")
# def component():
#     print(f"{datetime.now():%d-%m-%y %H:%M:%S}")
#     return render_template('join community.html')


# @app.route("/contact.html")
# def contact():
#     print(f"{datetime.now():%d-%m-%y %H:%M:%S}")
#     return render_template('contact.html')
#

# @app.route("/download")
# def download():
#     print(f"{datetime.now():%d-%m-%y %H:%M:%S}")
#     return render_template('download.html')


# @app.route("/retainer plan.html")
# def pricing():
#     print(f"{datetime.now():%d-%m-%y %H:%M:%S}")
#     return render_template('retainer plan.html')
#
#
# # @app.route("/favicon")
# def pricing():
#     print(f"{datetime.now():%d-%m-%y %H:%M:%S}")
# return render_template("{{url_for('static', filename='favicon.ico')}}")


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    # return render_template('login.html', error=error)
    if request.method == 'POST':
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'try again'


# def write_to_file(data):
    # with open('../home/lawplug/database.txt', mode='a') as database:
        # name = data["name"]
        # email = data["email"]
        # subject = data["subject"]
        # retainer_plan = data["retainer plan"]
        # message = data["message"]
        # file = database.write(f'\n{name},{email},{retainer_plan},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        # retainer_plan = data["retainer plan"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['NAME', 'EMAIL', 'SUBJECT', 'MESSAGE'])
        csv_writer.writerow([name, email, subject, message])


@app.route("/thankyou.html")
def about():
    print(f"{datetime.now():%d-%m-%y %H:%M:%S}")
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run()
# (debug=True, use_reloader=True, port=80)
