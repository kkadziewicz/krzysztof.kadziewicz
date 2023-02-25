import requests
import tkinter as tk

# Zdefiniuj klucz API do NewsAPI.org
api_key = "3d797c82c9b04851b1d74bf763bf5a7e"

# Definiuj URL do API z parametrem języka polskiego
url = f"https://newsapi.org/v2/top-headlines?country=pl&language=pl&apiKey={api_key}"

# Funkcja, która pobiera i wyświetla newsy po naciśnięciu przycisku
def get_news():
    # Wywołaj API i zapisz wynik w zmiennej response
    response = requests.get(url)

    # Sprawdź, czy zapytanie zakończyło się powodzeniem
    if response.status_code == 200:
        # Wyczyść poprzednie wyniki
        news_list.delete(0, tk.END)

        # Wyświetl tytuł i link każdego artykułu
        for article in response.json()['articles']:
            news_title = article['title']
            news_url = article['url']
            news_list.insert(tk.END, f"{news_title} ({news_url})")
    else:
        news_list.insert(tk.END, "Wystąpił problem z pobieraniem newsów.")

# Stwórz okno główne
root = tk.Tk()
root.title("Aktualności")

# Stwórz przycisk do pobierania newsów
get_news_button = tk.Button(root, text="Pobierz newsy", command=get_news)
get_news_button.pack(pady=10)

# Stwórz listę do wyświetlania newsów
news_list = tk.Listbox(root, width=80)
news_list.pack()

# Uruchom pętlę zdarzeń interfejsu graficznego
root.mainloop()
