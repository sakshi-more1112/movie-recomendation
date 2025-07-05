# 🎬 Movie Recommendation System

A simple yet effective **Content-Based Movie Recommendation System** built using **Python**, **Scikit-learn**, and **Tkinter GUI**. It suggests movies similar to the one entered by the user based on genre, cast, keywords, and more.

---

## 💡 Features

- 🔍 Recommends top 5 movies similar to any given title
- 🎨 User-friendly GUI built with Tkinter
- 🧠 Uses TF-IDF vectorization and Cosine Similarity
- ✅ Clean and modern design
- 📂 Works offline with local movie dataset

---

## 📁 Dataset

The system uses a custom dataset `movie_dataset1.csv` containing the following fields:

- `title`
- `genres`
- `keywords`
- `tagline`
- `cast`
- `director`

All of these features are combined to generate similarity scores for recommendations.

---

## 🚀 How It Works

1. Preprocess movie metadata by combining genres, keywords, cast, etc.
2. Convert text features into numerical vectors using **TF-IDF**.
3. Compute similarity scores between all movies using **Cosine Similarity**.
4. Suggest the **top 5 most similar movies** for any input title.

---

## 🖥️ GUI Preview

> ⚠️ Add a screenshot here of your running app for better visual appeal.

---

## 🛠️ How to Run

### Requirements
- Python 3.x
- pandas
- scikit-learn
- tkinter (comes preinstalled with Python)

### Installation

```bash
pip install pandas scikit-learn
