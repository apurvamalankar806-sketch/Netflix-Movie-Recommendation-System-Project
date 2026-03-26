# Netflix-Movie-Recommendation-System-Project

## Description
This project focuses on building a Netflix movie recommendation system that suggests similar movies based on textual content such as genre, cast, director, and description. The project was developed in multiple stages starting from a basic recommendation approach and later enhanced using similarity-based techniques.

## Objective
To understand how recommendation systems work.<br>
To build a content-based movie recommender.<br>
To improve recommendation accuracy through similarity computation.<br>
To handle real-world dataset issues such as duplicate titles.<br>

## Project Workflow
**Stage 1**: Basic Recommendation System<br>
Initially, a simple recommendation logic was implemented by selecting important columns like title, cast, genre, director, and description.
These features were combined to create a textual representation of each movie which was used to recommend similar content.

**Stage 2**: Handling Duplicate Titles<br>
During development, it was observed that the dataset contained multiple entries with identical movie titles.
To resolve this issue, the dataframe index was reset and a case-insensitive title-to-index mapping was created.
Duplicate title conflicts were removed using drop_duplicates() to ensure consistent recommendation retrieval.

**Stage 3**: Enhanced Recommendation using Cosine Similarity<br>
The recommendation system was further improved by applying TF-IDF Vectorization to convert textual data into numerical vectors.
Cosine similarity was then used to measure similarity between movies, allowing the system to recommend the most relevant titles along with similarity scores.

## Tools & Technologies Used
Python<br>
Pandas<br>
Scikit-learn<br>
Jupyter Notebook<br>

## Output
The system recommends top similar movies based on cosine similarity percentage.
Example:<br>
Input Movie: Narcos<br>
Recommended Movies:<br>
Downton Abbey  →  16.02 %<br>
London Spy  →  11.1 %<br>
Flowers  →  10.88 %<br>
Lovesick  →  10.79 %<br>
The Frankenstein Chronicles  →  10.39 %<br>
Higher similarity percentage indicates stronger content similarity.

## Conclusion
The project demonstrates the practical implementation of a content-based recommendation system using textual feature engineering and similarity metrics.
By progressively improving the system and resolving duplicate data issues, the final model provides more accurate and reliable movie recommendations.
