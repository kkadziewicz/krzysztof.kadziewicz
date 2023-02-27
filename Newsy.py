import requests
import tkinter as tk
import webbrowser

# Zdefiniuj klucz API do newsapi
API_KEY = '3d797c82c9b04851b1d74bf763bf5a7e'

# Utwórz okno programu
root = tk.Tk()
root.title('Najnowsze wiadomości')

# Utwórz etykietę z tytułem programu
title_label = tk.Label(root, text='Najnowsze newsy', font=('Arial', 18))
title_label.pack(pady=10)

# Utwórz pole tekstowe do wyświetlania newsów
news_text = tk.Text(root, width=80, height=20, font=('Arial', 12))
news_text.pack(padx=10, pady=10)

# Wykonaj zapytanie do API, aby pobrać najnowsze newsy
response = requests.get('https://newsapi.org/v2/top-headlines?country=pl&apiKey=' + API_KEY)

# Sprawdź, czy żądanie zakończyło się sukcesem
if response.status_code == 200:
    # Przetwórz odpowiedź z serwera i wyświetl tytuły newsów
    news = response.json()
    for article in news['articles']:
        title = article['title']
        url = article['url']
        news_text.insert(tk.END, title + '\n')
        news_text.insert(tk.END, url + '\n\n')
        news_text.tag_add('link', f"{news_text.index(tk.INSERT)}-{len(url)}c", news_text.index(tk.INSERT))
        news_text.tag_config('link', foreground='blue', underline=True)
        news_text.tag_bind('link', '<Button-1>', lambda event, url=url: webbrowser.open_new(url))
else:
    # Wyświetl komunikat o błędzie
    news_text.insert(tk.END, 'Błąd pobierania newsów\n\n')

# Utwórz przycisk do zamykania programu
close_button = tk.Button(root, text='Zamknij', command=root.destroy)
close_button.pack(pady=10)

# Uruchom pętlę główną programu
root.mainloop()
