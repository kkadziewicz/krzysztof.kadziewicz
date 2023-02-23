# https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg
import requests
import snakemd
import subprocess
import os  # https://docs.python.org/3/library/os.html
from secrets import token_urlsafe
from pathlib import Path
from datetime import date, timedelta

TEMP_DIR = "tmp"
NBP_URL = "https://api.nbp.pl/"
TODAY = date.today()
TODAY_ISO = TODAY.isoformat()

def init_dir():
    if not Path(TEMP_DIR).exists():
        os.mkdir(TEMP_DIR)


def generuj_dokument(code, start_date, end_date=TODAY_ISO):
    plik = f"{TEMP_DIR}/{token_urlsafe(8)}"
    url_address = f"https://api.nbp.pl/api/exchangerates/rates/A/{code}/{start_date}/{end_date}/"
    nowy_dokument = snakemd.new_doc(plik)
    try:
        nowy_dokument.output_page()
    except Exception as e:
        sg.Popup(e, title="ERROR")

def test_internetu():
    # https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
    try:
        nbp_test = requests.get(NBP_URL)
        status_nbp = nbp_test.status_code
    except Exception as e:
        sg.Popup(f"Error -> {e} | status_nbp ustawiam na -> -999", title="ERROR")
        status_nbp = -999

    if status_nbp == 200:
        sg.Popup(f"Łączność do {NBP_URL} - OK")
    elif status_nbp == -999:
        sg.Popup(f"Łączność do {NBP_URL} - sprawdź kabelek!!!!")
    else:
        sg.Popup(f"Łączność do {NBP_URL} - code: {status_nbp}")



# Start aplikacji
init_dir()

# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text(" --[Generowanie DOCX z wykresem walut------------------------------")],
    [sg.Text("Podaj kod Waluty (np. CHF)"), sg.Input("")],
    [sg.Text("_______________________________________________________________________")],
    [sg.Text("Ile dni wstecz wykres (max. 90)?"), sg.Input("")],
    [sg.Button("GENERUJ"),sg.Button("TEST INTERNETU"), sg.Button("KONIEC") ],
]
window = sg.Window("Tutuł naszego okienka aplikacji", app_layout)
# używamy pętli nieskończonej, która działa aż do słowa kluczowego `break`
# pamiętajmy o PEP-8, wcięciach i bloku kodu - https://www.python.org/dev/peps/pep-0008/#indentation
while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "KONIEC":
        print("Hard EXIT")
        break

    if event == "GENERUJ":
        waluta = values[0].upper()
        # https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta
        data_poczatkowa = TODAY - timedelta(int(values[1]))
        generuj_dokument(waluta, data_poczatkowa)

    if event == "TEST INTERNETU":
        test_internetu()

    # sprawdzamy wartości zwracane przez okno
    sg.popup(f"Event is: {event}, returned dict is: {values}")


# koniec programu
window.close()
print("End of application")