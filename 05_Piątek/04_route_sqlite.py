from flask import Flask

from funkcje_dodatkowe.baza_danych import generate_token, create_user_record
from funkcje_dodatkowe.send_email_smarthost import mail_report
from datetime import datetime

app = Flask("moja_apka")

@app.route("/") # dekorator
def main_page():
    return "<H1> Welcome</H1>"

@app.route("/data")
def get_data():
    html = """
    <h2> Podaj nam dane </h2> <hr>
    Tu chcę Twój adres email: ...... <hr>
    """ + str(generate_token())
    return html

@app.route("/user/<value>")
def username(value):
    html = f"""
    <H1>Welcome new user</H1>
    Wysyłam ci maila na adres: {value}
    """
    new_token = generate_token()
    mail_body = f"treść naszego maila - {datetime.today()} - {new_token}"
    if value.count("@") == 1:
        ret, ret_value = mail_report(value,"python-course@jurkiewicz.tech", mail_body)
        if ret == False:
            print(ret_value)
        if ret == True:
            create_user_record(value, new_token)
    return html

app.run()