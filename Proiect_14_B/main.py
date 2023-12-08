
import tkinter as tk
from tkinter import ttk
import requests

class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Z")

        # Variabila pentru a stoca subiectul de știri
        self.topic_var = tk.StringVar()

        # Crearea interfeței grafice
        self.create_gui()

    def create_gui(self):
        # Eticheta pentru subiectul de știri
        topic_label = ttk.Label(self.root, text="Introduceți subiectul de știri:")
        topic_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        # Câmp de introducere pentru subiectul de știri
        topic_entry = ttk.Entry(self.root, textvariable=self.topic_var)
        topic_entry.grid(row=0, column=1, padx=5, pady=10, sticky=tk.W)

        # Buton pentru a obține știrile
        get_news_button = ttk.Button(self.root, text="Obține știrile", command=self.get_news)
        get_news_button.grid(row=0, column=2, padx=5, pady=10, sticky=tk.W)

        # Câmp pentru afișarea știrilor
        self.news_text = tk.Text(self.root, wrap=tk.WORD, width=80, height=20)
        self.news_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W)

    def get_news(self):
        # Obține subiectul de știri introdus de utilizator
        topic = self.topic_var.get()

        # Setează cheia API de la News API
        api_key = '3ef695980afe4eb685bf37daef1d574d'

        # Faceți cererea către News API pentru a obține știrile
        url = f'https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}'
        response = requests.get(url)

        # Verifică dacă răspunsul este OK (codul 200)
        if response.status_code == 200:
            # Șterge conținutul anterior al câmpului de text
            self.news_text.delete(1.0, tk.END)

            # Obține știrile din răspunsul API și le afișează în câmpul de text
            news_data = response.json()
            articles = news_data.get('articles', [])

            for article in articles:
                print(article)
                title = article.get('title', '')
                description = article.get('description', '')
                source = article.get('source', {}).get('name', '')

                # Afișează titlul, descrierea și sursa în câmpul de text
                self.news_text.insert(tk.END, f"{title}\n{description}\nSource: {source}\n\n")

        else:
            # Afișează un mesaj de eroare dacă cererea a eșuat
            self.news_text.delete(1.0, tk.END)
            self.news_text.insert(tk.END, "Nu s-au putut obține știrile. Verificați conexiunea la internet sau încercați din nou.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NewsApp(root)
    root.mainloop()
