# CineMetrics 🎬

> A data analysis tool that consumes the TMDB API to generate a behavioral profile based on the user's TV show preferences.

![Project Status](https://img.shields.io/badge/Status-In_Development-yellow)
## 🎯 Objective
Recommendation algorithms are often "black boxes." **CineMetrics** aims to build a transparent analyzer that:
1. Takes a user's watched list and personal ratings (0-10) as input.
2. Enriches this data with global genres and metadata via an external API (TMDB).
3. Generates a "User DNA" report (e.g., 60% Drama, 20% Sci-Fi) to suggest new content with mathematical precision.

## 🛠 Tech Stack

* **Language:** Python
* **API Consumption:** `requests` library (connecting to TheMovieDB API)
* **Storage:** MySQL (storing user history and genre weights)
* **Data Processing:** JSON Parsing and Weighted Logic

## 🧠 How It Works ( The Algorithm)
The system operates in 3 logical stages:

1.  **Data Collection (Input):** The user provides the TV show name and their personal rating.
2.  **Enrichment (API Request):** The system fetches the show's ID from TMDB and extracts metadata (Genres, Cast, Global Rating).
3.  **Processing (Weighting Algorithm):**
    * If *Personal Rating* > *Global Rating*, the weight of that show's genres increases in the user's profile.
    * The system calculates the frequency of watched genres vs. user satisfaction.

## 📌 Roadmap
- [x] Implement basic API connection (TV Show Search)
- [ ] Create Database Schema (Users & Genres Tables)
- [ ] Develop the weighting algorithm logic
- [ ] Create data visualization (Preference Charts)

---
*This project is part of my Computer Science portfolio.*

## 🗄️ Modeling DB

```mermaid
erDiagram
    SERIES {
        int id PK "TMDB's ID"
        text name "Series Name"
        text overview "Synopsis"
        float vote_average "Average Rating"
    }
