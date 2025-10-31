# Climate-Music_Corelation_DSA210_Elif_Ozkaya
DSA210 Term Project / Fall 2025-2026 

# DSA 210 Project Proposal: Analysis of Music Charts and Climate

## Motivation

I have always been fascinated with the effects of climate on culture. We can see this in clothing and food, which are directly affected by the types of crops grown in a climate and the needs of people living in different heat conditions.

I want to explore this topic with a more subjective concept which is music.

Additionally, I really like top 10, 40 or 100 lists. My favorite radio programs during my childhood were always chart countdowns, which makes me even more interested in this data.

This project combines both interests. My goal is to see if a country's climate has a measurable effect on its 'Top 200' music charts. For example, do hotter countries prefer more pop music, or do colder countries prefer more metal?

---

## Data to be Used

### Music Popularity per Country

* Source: Shazam official website (https://www.shazam.com/charts/top-200)
* Data: Top 200 songs for 70 countries in the week of 21-27 October 2025.
* Status: Collection Complete. I have 70 separate CSV files.
* Features: chart_position, artist_name, song_name, country_name.

### Audio Features & Genre

* The Shazam CSVs do not include the genre, tempo, energy, or mood of the songs and I need these to 
* Collection steps:
    1.  I will find a large, public "Audio Features" dataset from Kaggle or another relaible source.
    2.  This dataset will provide the audio features I need for many songs.
    3.  I will use Pandas in Python to merge this dataset with my main Shazam data and check for any shortcomings.
    4.  I will repeat the steps for large shortcomings. If the shortcoming is small I may fill the data manually.

### Climate of Countries

* I need to add climate data for each of the 70 countries.
* Collection steps
    1.  I will find a simple, public dataset from Kaggle or other reliable data source.
    2.  I will collect climate type, avarage temprature and potentially other relavant data.
    3.  I will use Pandas in Python to merge this climate data with my main music dataset.


## Analysis Plan
* I will create visualizations to find patterns:
    1. A scatterplot to see if avg_annual_temperature (x-axis) and mood (y-axis) are correlated.
    2. A scatterplot to check avg_annual_temperature vs. energy.
    3. A bar chart showing the most popular genre per climate type
      
2.  Hypothesis Test: I will run a formal test to see if the average mood of songs in "Tropical" countries is statistically different from the average mood in "Temperate" countries.

### Machine Learning (ML)

*  Regression Model: I will try to build a regression model to predict a country's avg_mood_score based on its avg_annual_temperature.
*  Classification Model: I will try to build a model to predict if a country is in which climate_zone based *only* on the audio features of its top songs (like average energy, tempo, and danceability).

