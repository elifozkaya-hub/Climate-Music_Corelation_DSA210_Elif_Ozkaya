# Climate-Music_Corelation_DSA210_Elif_Ozkaya
DSA210 Term Project / Fall 2025-2026 

# DSA 210 Project Proposal: Analysis of Music Charts and Climate

## Motivation

I have always been fascinated with the effects of climate on culture. We can see this in clothing and food, which are directly affected by the types of crops grown in a climate and the needs of people living in different heat conditions.

I want to explore this topic with a more subjective concept which is music.

Additionally, I really like top 10, 40 or 100 lists. My favorite radio programs during my childhood were always chart countdowns, which makes me even more interested in this data.

This project combines both interests. My goal is to see if a country's climate has a measurable effect on its 'Top 200' music charts. For example, do hotter countries prefer more pop music, or do colder countries prefer more metal?

---

## Overview

This project explores the relationship between a country's climate and its musical preferences. By analyzing the "Top 30" songs from 68 countries, I investigated whether environmental factors like temperature and rainfall have a statistically significant correlation with the Genre or Mood of music listeners prefer.

## Data to be Used

### Music Popularity per Country

* Source: Shazam official website (https://www.shazam.com/charts/top-200)
* Data: Top 30 songs for 68 countries in the week of 21-27 October 2025.
* Status: Collection Complete. I have 68 separate CSV files.
* Features: chart_position, artist_name, song_name, country_name.

### Audio Features & Genre

* Problems:
* 1. The Shazam CSVs do not include the genre, tempo, energy, or mood of the songs and I need these too.
* 2. I tried API's like Spotify, Shazam and Last.fm but none of the data they returned were usable, they returned NA for more than half of the requests and there was a request limit which i couldnt avoid as i have more than 1000 unique songs that needed to be sorted.

* Solution:
* 1. I used gemini to anotate my music ganre and mood features which I sampled and checked for acuracy and it is acurete.
* 2. The genre tags were selected to not be specific to the region they came from so turkish pop counts as pop to make analysis possible.
* Features: genre, mood for all songs from music popularity dataset


### Climate of Countries

I compiled the data for the 193 countries by aggregating information from three sources. 
1. Temperature & Rainfall 
Source: The World Bank Climate Change Knowledge Portal (CCKP) and the Climatic Research Unit (CRU) at the University of East Anglia.
Method: I filled a table with the data found from mentioned sources.

3. Climate Type (Köppen Classification)
Source: The Köppen-Geiger Climate Classification system.
Method: I matched each country to its dominant climate zone.




## Analysis Plan
* I will create visualizations to find patterns:
    1. A scatterplot to see if avg_annual_temperature (x-axis) and mood (y-axis) are correlated.
    2. A scatterplot to check avg_annual_temperature vs. energy.
    3. A bar chart showing the most popular genre per climate type
      
2.  Hypothesis Test: I will run a formal test to see if the average mood of songs in "Tropical" countries is statistically different from the average mood in "Temperate" countries.

### Machine Learning (ML)

*  Regression Model: I will try to build a regression model to predict a country's avg_mood_score based on its avg_annual_temperature.
*  Classification Model: I will try to build a model to predict if a country is in which climate_zone based *only* on the audio features of its top songs (like average energy, tempo, and danceability).

