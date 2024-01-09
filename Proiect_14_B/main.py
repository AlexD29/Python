import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import datetime, timedelta, timezone
import requests
import langid
import os


def extract_date(date_string):
    formats_to_try = [
        '%Y-%m-%dT%H:%M:%S%z',
        '%Y-%m-%dT%H:%M:%SZ',
        '%Y-%m-%d %H:%M:%S %z',
        '%Y-%m-%dT%H:%M:%SZ',
        '%Y-%m-%dT%H:%M:%S.%fZ',
        '%Y-%m-%d %H:%M:%S',
    ]

    for fmt in formats_to_try:
        try:
            date_time_obj = datetime.strptime(date_string, fmt)
            date_time_obj = date_time_obj.replace(tzinfo=timezone.utc)
            return date_time_obj
        except ValueError:
            pass

    # If none of the formats match, raise an error
    raise ValueError(f"Could not parse date: {date_string}")


def format_date(input_date):
    try:
        date_time_obj = datetime.strptime(input_date, '%Y-%m-%d %H:%M:%S%z')
        formatted_date = date_time_obj.strftime('%d.%m.%Y %H:%M')
        return formatted_date

    except ValueError as e:
        print(f"Error formatting date: {e}")
        return None


def is_english(text):
    lang, _ = langid.classify(text)
    return lang == 'en'


def create_news_files(all_news_content):
    news_content_dir = "news_content"
    os.makedirs(news_content_dir, exist_ok=True)

    for index, content in enumerate(all_news_content):
        file_path = os.path.join(news_content_dir, f"news_{index + 1}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)


class NewsApp:
    def __init__(self, root):

        self.root = root
        self.root.title("Z")
        self.topic_var = tk.StringVar()
        self.placeholder_text = "Enter the topic"
        self.root.geometry("800x600")
        self.root.configure(background='white')
        self.image_label = None
        self.topic_entry = None
        self.get_news_button = None
        self.news_frame = None
        self.canvas = None
        self.selected_news = None
        self.card_row = 0
        self.card_column = 0

        self.create_gui()

        self.root.update_idletasks()
        self.root.geometry(f"+350+100")

    def create_gui(self):
        image_path = "images/z.jpg"
        image = Image.open(image_path)
        image = image.resize((180, 180))
        img = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(self.root, image=img, bg='lightgray')
        self.image_label.image = img
        self.image_label.grid(row=0, column=0, pady=(80, 20))

        self.topic_entry = ttk.Entry(self.root, textvariable=self.topic_var, font=('Helvetica', 20), width=30,
                                     style="Rounded.TEntry")
        self.topic_entry.grid(row=1, column=0, pady=(0, 20))
        self.topic_entry.insert(0, self.placeholder_text)
        self.topic_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.topic_entry.bind("<FocusOut>", self.on_entry_focus_out)

        self.topic_entry.bind("<Return>", lambda event: self.get_news())

        self.get_news_button = ttk.Button(self.root, text="Search", command=self.get_news, style="Big.TButton")
        self.get_news_button.grid(row=2, column=0, pady=(0, 0))

        style = ttk.Style()
        style.configure("Big.TButton", font=('Helvetica', 16), foreground="#4CAF50", background="#4CAF50",
                        padding=(10, 5), relief=tk.FLAT,
                        bd=0,
                        highlightthickness=0)

        self.get_news_button.bind("<Enter>", self.on_button_enter)
        self.get_news_button.bind("<Leave>", self.on_button_leave)

        self.root.columnconfigure(0, weight=1)

    def on_button_enter(self, event):
        current_style = event.widget.cget("style")

        if current_style == "Big.TButton":
            event.widget.configure(style="Hover.Big.TButton")
        else:
            event.widget.configure(style="Hover.Small.TButton")

        self.root.config(cursor="hand2")

    def on_button_leave(self, event):
        current_style = event.widget.cget("style")

        if current_style == "Hover.Big.TButton":
            event.widget.configure(style="Big.TButton")
        else:
            event.widget.configure(style="Small.TButton")

        self.root.config(cursor="")

    def on_mousewheel(self, event):
        # Determine the direction of the mouse wheel scroll
        if event.delta > 0:
            direction = "up"
        else:
            direction = "down"

        # Scroll the canvas accordingly
        if direction == "up":
            self.news_frame.yview_scroll(-1, "units")
        elif direction == "down":
            self.news_frame.yview_scroll(1, "units")

    def on_entry_focus_in(self, event):
        if self.topic_var.get() == self.placeholder_text:
            self.topic_var.set("")

    def on_entry_focus_out(self, event):
        if not self.topic_var.get():
            self.topic_var.set(self.placeholder_text)

    def update_gui_after_search(self):
        new_image_path = "images/z.jpg"
        new_image = Image.open(new_image_path)
        new_image = new_image.resize((50, 40))
        new_img = ImageTk.PhotoImage(new_image)

        self.image_label.configure(image=new_img)
        self.image_label.image = new_img

        self.topic_entry.configure(font=('Helvetica', 18), width=100)

        self.get_news_button.configure(style="Small.TButton")
        style = ttk.Style()
        style.configure("Small.TButton", font=('Helvetica', 12), foreground="#4CAF50", background="#4CAF50",
                        padding=(15, 4), relief=tk.FLAT,
                        bd=0,
                        highlightthickness=0)

        self.image_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
        self.topic_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")
        self.get_news_button.grid(row=0, column=2, padx=(0, 10), pady=(10, 10), sticky="ew")

        container_frame = ttk.Frame(self.root, style='Container.TFrame')
        container_frame.grid(row=1, column=0, columnspan=3,
                             sticky="nsew")
        style = ttk.Style()
        style.configure('Container.TFrame',
                        background='white')

        canvas = tk.Canvas(container_frame, bg='white')
        canvas.grid(row=0, column=0, sticky="nsew")

        container_frame.columnconfigure(0, weight=1)
        container_frame.rowconfigure(0, weight=1)

        self.news_frame = ttk.Frame(canvas, style='News.TFrame')
        canvas.create_window((0, 0), window=self.news_frame, anchor=tk.W, width=1520)
        style = ttk.Style()
        style.configure('News.TFrame', background='black')

        scroll_y = ttk.Scrollbar(container_frame, orient="vertical", command=canvas.yview)
        scroll_y.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scroll_y.set)

        canvas.bind("<MouseWheel>", self.on_mousewheel)

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.canvas = canvas

    def get_news(self):
        self.update_gui_after_search()

        for widget in self.news_frame.winfo_children():
            widget.destroy()

        topic = self.topic_var.get()

        if not topic:
            self.insert_card("Please enter a topic to search.")
            return

        api_keys = {
            'newsapi': '3ef695980afe4eb685bf37daef1d574d',
            'guardian': 'bdb1c135-cf0b-45f0-b098-db003ccd3b74',
            'mediastack': '251b56cf780d3d220c9f5a4cef7c2f16',
            'newsdata': 'pub_360972b3a808f11528343f275ac3c7f3744b3',
            'worldnewsapi': 'afb4f3873ef9488abe807c17e94dc09d',
            'gnewsapi': '0f69b52adff4d32d47f2b5ce1387d0d4',
        }

        language_param = '&language=en'
        sources = ['newsapi', 'guardian', 'mediastack', 'newsdata', 'worldnewsapi', 'gnewsapi']

        all_news = []

        for source in sources:
            api_key = api_keys.get(source)
            if api_key:
                if source == 'newsapi':
                    url = f'https://{source}.org/v2/everything?q={topic}&apiKey={api_key}{language_param}'
                elif source == 'guardian':
                    url = f'https://content.guardianapis.com/search?q={topic}&api-key={api_key}{language_param}'
                elif source == 'mediastack':
                    url = f'http://api.mediastack.com/v1/news?access_key={api_key}&keywords={topic}{language_param}'
                elif source == 'newsdata':
                    url = f'https://newsdata.io/api/1/news?apikey={api_key}&q={topic}{language_param}'
                elif source == 'worldnewsapi':
                    url = f'https://api.worldnewsapi.com/search-news?api-key={api_key}&text={topic}{language_param}'
                elif source == 'gnewsapi':
                    url = f'https://gnews.io/api/v4/search?q={topic}&token={api_key}&lang=en'

                response = requests.get(url)

                if response.status_code == 200:
                    news_data = response.json()

                    if source == 'newsapi':
                        articles = news_data.get('articles', [])
                        for article in articles:
                            published_at = extract_date(article.get('publishedAt', ''))
                            if published_at >= datetime.now(timezone.utc) - timedelta(days=10):
                                author = article.get('author', '')
                                content = article.get('content', '')
                                title = article.get('title', '')
                                source_name = article.get('source', {}).get('name', '')
                                description = article.get('description', '')
                                url_to_image = article.get('urlToImage', '')
                                web_url = article.get('url', '')
                                all_news.append({
                                    'source': "News API",
                                    'author': author,
                                    'content': content,
                                    'title': title,
                                    'extra_info': f"Source: {source_name}",
                                    'description': description,
                                    'image_url': url_to_image,
                                    'published_at': published_at,
                                    'web_url': web_url,
                                })

                    elif source == 'guardian':
                        results = news_data.get('response', {}).get('results', [])
                        for article in results:
                            published_at = extract_date(article.get('webPublicationDate', ''))
                            if published_at >= datetime.now(timezone.utc) - timedelta(days=10):
                                title = article.get('webTitle', '')
                                web_url = article.get('webUrl', '')
                                author = article.get('fields', {}).get('byline', '').replace('By ', '')
                                thumbnail = article.get('fields', {}).get('thumbnail', '')
                                all_news.append({
                                    'source': "The Guardian",
                                    'author': author,
                                    'content': '',
                                    'title': title,
                                    'extra_info': f"URL: {web_url}",
                                    'description': '',
                                    'image_url': thumbnail,
                                    'published_at': published_at,
                                    'web_url': web_url,
                                })

                    elif source == 'mediastack':
                        data = news_data.get('data', [])
                        for article in data:
                            published_at = extract_date(article.get('published_at', ''))
                            if published_at >= datetime.now(timezone.utc) - timedelta(days=10):
                                title = article.get('title', '')
                                if is_english(title):
                                    source_name = article.get('source', '')
                                    description = article.get('description', '')
                                    author = article.get('author', '')
                                    image_url = article.get('image', '')
                                    web_url = article.get('url', '')
                                    all_news.append({
                                        'source': "Media Stack",
                                        'author': author,
                                        'content': description,
                                        'title': title,
                                        'extra_info': f"Source: {source_name}",
                                        'description': description,
                                        'image_url': image_url,
                                        'published_at': published_at,
                                        'web_url': web_url,
                                    })

                    elif source == 'newsdata':
                        articles = news_data.get('results', [])
                        for article in articles:
                            published_at = extract_date(article.get('pubDate', ''))
                            if published_at >= datetime.now(timezone.utc) - timedelta(days=10):
                                title = article.get('title', '')
                                source_name = article.get('source', '')
                                description = article.get('description', '')
                                content = article.get('content', '')

                                creator = article.get('creator', [])
                                if creator is not None and isinstance(creator, list):
                                    creator = [c for c in creator if c is not None]

                                author = ', '.join(map(str, creator)) if creator else None
                                image_url = article.get('image', '')
                                web_url = article.get('url', '')

                                all_news.append({
                                    'source': "Newsdata.io",
                                    'author': author,
                                    'content': content,
                                    'title': title,
                                    'extra_info': f"Source: {source_name}",
                                    'description': description,
                                    'image_url': image_url,
                                    'published_at': published_at,
                                    'web_url': web_url,
                                })

                    elif source == 'worldnewsapi':
                        articles = news_data.get('news', [])
                        for article in articles:
                            published_at = extract_date(
                                article.get('publish_date', ''))
                            if published_at >= datetime.now(timezone.utc) - timedelta(days=10):
                                author = ', '.join(article.get('authors', []))
                                content = article.get('text', '')
                                title = article.get('title', '')
                                source_name = "World News API"
                                description = article.get('summary', '')
                                image_url = article.get('image', '')
                                web_url = article.get('url', '')
                                all_news.append({
                                    'source': source_name,
                                    'author': author,
                                    'content': content,
                                    'title': title,
                                    'extra_info': f"Source: {source_name}",
                                    'description': description,
                                    'image_url': image_url,
                                    'published_at': published_at,
                                    'web_url': web_url,
                                })

                    elif source == 'gnewsapi':
                        articles = news_data.get('articles', [])
                        for article in articles:
                            published_at = extract_date(article.get('publishedAt', ''))
                            if published_at >= datetime.now(timezone.utc) - timedelta(days=10):
                                title = article.get('title', '')
                                source_name = article.get('source', '')
                                description = article.get('description', '')
                                content = article.get('content', '')
                                author = article.get('author', '')
                                image_url = article.get('image', '')
                                web_url = article.get('url', '')

                                all_news.append({
                                    'source': "GNews API",
                                    'author': author,
                                    'content': content,
                                    'title': title,
                                    'extra_info': f"Source: {source_name}",
                                    'description': description,
                                    'image_url': image_url,
                                    'published_at': published_at,
                                    'web_url': web_url,
                                })

                else:
                    all_news.append({
                        'source': f"We couldn't get the news from source {source}. Check the internet connection and try again."
                    })

            else:
                all_news.append({
                    'source': f"API key is missing for source {source}."
                })

        sorted_news = sorted(all_news, key=lambda x: x.get('published_at'), reverse=True)

        for article in sorted_news:
            self.canvas.yview_moveto(0)
            self.insert_card(article)

        self.canvas.yview_moveto(0)

    def insert_card(self, article):
        news_section_frame = ttk.Frame(self.news_frame, style='News.TFrame', borderwidth=2, relief="groove",
                                       padding=(10, 10))
        style = ttk.Style()
        style.configure('News.TFrame', background='white')

        news_section_frame.grid(row=self.card_row, column=0, sticky="ew", padx=10, pady=10)

        self.news_frame.columnconfigure(0, weight=1)
        self.news_frame.rowconfigure(self.card_row, weight=1)

        self.card_row += 1

        self.card_column = 0

        ttk.Label(news_section_frame, text=article['source']).grid(row=0, column=0, sticky="w")
        title_label = ttk.Label(news_section_frame, text=article['title'], font=('Arial', 12, 'bold'))
        title_label.grid(row=1, column=0, sticky="w")

        ttk.Label(news_section_frame, text=article['extra_info']).grid(row=2, column=0, sticky="w")

        date_and_hour = format_date(article['published_at'].strftime('%Y-%m-%d %H:%M:%S%z'))
        ttk.Label(news_section_frame, text=date_and_hour).grid(row=3, column=0, sticky="w")

        read_button = ttk.Button(news_section_frame, text="Read", style="Green.TButton",
                                 command=lambda article=article: self.show_news_details(article,
                                                                                        self.root.winfo_width(),
                                                                                        self.root.winfo_height()))

        read_button.grid(row=4, column=0, sticky="w")

        self.news_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def show_news_details(self, article, root_width, root_height):
        detailed_news_window = tk.Toplevel(self.root)
        detailed_news_window.title(article['title'])

        detailed_news_window.geometry(f"{root_width}x{root_height}+{0}+{0}")

        ttk.Label(detailed_news_window, text=f"{article['title']}", font=('Arial', 14, 'bold')).grid(row=0, column=0,
                                                                                                     pady=(10, 10),
                                                                                                     padx=(5, 5),
                                                                                                     columnspan=3,
                                                                                                     sticky=tk.W)

        info_frame = ttk.Frame(detailed_news_window)
        info_frame.grid(row=1, column=0, padx=20, pady=20, sticky=tk.W)

        if article['image_url']:
            image = Image.open(requests.get(article['image_url'], stream=True).raw)
        else:
            image = Image.open('images/default_image.png')

        image = image.resize((320, 200))
        photo = ImageTk.PhotoImage(image)

        image_label = ttk.Label(detailed_news_window, image=photo)
        image_label.photo = photo
        image_label.grid(row=1, column=0, rowspan=3, columnspan=1, padx=(5, 5), sticky=tk.W)

        ttk.Label(detailed_news_window, text=f"{article['extra_info']}").grid(row=1, column=1, columnspan=3,
                                                                              sticky=tk.W)
        ttk.Label(detailed_news_window,
                  text=f"{format_date(article['published_at'].strftime('%Y-%m-%d %H:%M:%S%z'))}").grid(row=2, column=1,
                                                                                                       columnspan=3,
                                                                                                       sticky=tk.W)
        ttk.Label(detailed_news_window, text=f"Author: {article['author']}").grid(row=3, column=1, columnspan=3,
                                                                                  sticky=tk.W)

        content_frame = tk.Frame(detailed_news_window)
        content_frame.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W)

        if article['description'] == article['content']:
            ttk.Label(content_frame, text=article['content'], wraplength=1500, justify=tk.LEFT).grid(row=0, column=0,
                                                                                                     columnspan=3,
                                                                                                     sticky=tk.W)
        else:
            ttk.Label(content_frame, text=article['description'], wraplength=1000, justify=tk.LEFT).grid(row=0,
                                                                                                         column=0,
                                                                                                         columnspan=3,
                                                                                                         sticky=tk.W)
            ttk.Label(content_frame, text=article['content'], wraplength=1500, justify=tk.LEFT).grid(row=1, column=0,
                                                                                                     columnspan=3,
                                                                                                     sticky=tk.W)

        close_button = ttk.Button(detailed_news_window, text="Close", style="Green.TButton",
                                  command=detailed_news_window.destroy)
        close_button.grid(row=5, column=0, columnspan=4, sticky=tk.W)

    def show_all_news(self):
        for widget in self.news_frame.winfo_children():
            widget.destroy()

        self.selected_news = None

        self.get_news()


if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style(root)
    style.configure("Green.TButton", foreground="green", background="green")
    app = NewsApp(root)
    root.mainloop()
