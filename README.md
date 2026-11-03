# Netflix Movie Recommendation System

A content-based recommender that suggests similar Netflix titles from a selected title.

**Live demo:** https://netflix-recommender-apurva.streamlit.app/

## Overview
The system compares titles using their director, cast, genres and description. A user selects a title and receives the 10 most similar titles with similarity scores.

## Approach
1. Combine director, cast, genres and description into a single text field.
2. Convert the text to numerical vectors with TF-IDF.
3. Rank all other titles by cosine similarity to the selected title.

## Data Quality
The dataset contains multiple entries with identical titles, which caused inconsistent lookups. A case-insensitive title-to-index mapping with duplicate keys removed now resolves each title to a single record.

## Sample Output
Input: *The Crown*

| Recommended title | Similarity |
|---|---|
| Downton Abbey | 16.02% |
| London Spy | 11.10% |
| Flowers | 10.88% |
| Lovesick | 10.79% |
| The Frankenstein Chronicles | 10.39% |

## Limitations
- Recommendations rely on content metadata only. There is no user viewing data, so results are not personalised.
- Similarity scores are low overall, and titles with sparse descriptions produce weaker matches.
- The model has not yet been evaluated with a quantitative metric.

## Planned Improvements
- Add an evaluation method, such as genre overlap between the input and its recommendations.
- Apply dimensionality reduction and clustering to group similar titles.

## Tech Stack
Python, Pandas, Scikit-learn, Streamlit

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Repository Contents
- `app.py`: Streamlit application
- `Netflix_Movie_Recommendation_System.ipynb`: development and testing notebook
- `netflix_titles.csv`: dataset
