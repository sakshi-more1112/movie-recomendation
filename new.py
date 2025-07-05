import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import messagebox

# === Load Data ===
try:
    df = pd.read_csv("movie_dataset1.csv", low_memory=False)
except FileNotFoundError:
    messagebox.showerror("Error", "'movie_dataset1.csv' file not found.")
    exit()

# === Preprocess ===
df['combined_features'] = df[['genres', 'keywords', 'tagline', 'cast', 'director']].fillna('').agg(' '.join, axis=1)
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations(title):
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    idx = indices.get(title)
    if idx is None:
        return ["❌ Movie not found. Try another title."]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

# === GUI Setup ===
window = tk.Tk()
window.title("🎬 Movie Recommender")
window.geometry("600x500")
window.configure(bg="#f6f8ff")  # light lavender/blue

# === Styling ===
FONT_HEADER = ("Helvetica", 16, "bold")
FONT_NORMAL = ("Helvetica", 12)
BTN_COLOR = "#aec6cf"  # pastel blue
ENTRY_BG = "#ffffff"
TEXT_BG = "#fdfdff"
TEXT_FG = "#333333"

# === Header ===
header = tk.Label(window, text="🎥 Movie Recommendation System", font=FONT_HEADER, bg="#f6f8ff", fg="#2c3e50")
header.pack(pady=20)

# === Input Frame ===
input_frame = tk.Frame(window, bg="#f6f8ff")
input_frame.pack(pady=10)

entry_label = tk.Label(input_frame, text="Enter Movie Title:", font=FONT_NORMAL, bg="#f6f8ff")
entry_label.grid(row=0, column=0, padx=5)

entry = tk.Entry(input_frame, width=40, font=FONT_NORMAL, bg=ENTRY_BG)
entry.grid(row=0, column=1, padx=5)

# === Button ===
def show_recommendations():
    movie_title = entry.get().strip()
    if not movie_title:
        messagebox.showwarning("Input Error", "Please enter a movie title.")
        return

    recommendations = get_recommendations(movie_title)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"🎬 Top 5 movies similar to '{movie_title}':\n\n")
    for i, movie in enumerate(recommendations, 1):
        result_text.insert(tk.END, f"{i}. {movie}\n")

button = tk.Button(window, text="🎯 Get Recommendations", command=show_recommendations,
                   font=FONT_NORMAL, bg=BTN_COLOR, activebackground="#b7d9e8",
                   relief="raised", padx=10, pady=5)
button.pack(pady=15)

# === Output ===
result_text = tk.Text(window, height=10, width=70, font=FONT_NORMAL, bg=TEXT_BG,
                      fg=TEXT_FG, bd=2, relief="groove", wrap=tk.WORD)
result_text.pack(pady=10)

# === Footer ===
footer = tk.Label(window, text="Made with 💙 using Python & Scikit-Learn", font=("Helvetica", 10),
                  bg="#f6f8ff", fg="#888888")
footer.pack(pady=10)

# === Run App ===
window.mainloop()
