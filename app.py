import streamlit as st
import pandas as pd
import altair as alt
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="DSA 210: Climate & Music",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 1. LOAD DATA ---
current_dir = os.path.dirname(os.path.abspath(__file__))
music_file = os.path.join(current_dir, "Song_Data_With_Genres.xlsx")
climate_file = os.path.join(current_dir, "Global_Climate_Data_Formatted.xlsx")

@st.cache_data
def load_data():
    try:
        df_music = pd.read_excel(music_file)
        df_climate = pd.read_excel(climate_file)
        df_music.columns = df_music.columns.str.strip()
        df_climate.columns = df_climate.columns.str.strip()
        # Merge logic
        merged = pd.merge(df_music, df_climate, on='Country', how='inner')
        return merged
    except Exception as e:
        return None

df = load_data()

if df is None:
    st.error("❌ Error loading data. Please check file paths.")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.title("🎧 Filter Controls")
top_n = st.sidebar.slider("Number of Top Moods to Display:", 5, 20, 8)

# Filter Data based on selection
top_moods = df['Mood'].value_counts().head(top_n).index.tolist()
filtered_df = df[df['Mood'].isin(top_moods)]

# --- MAIN PAGE CONTENT ---

# 1. HEADER & MOTIVATION (From README)
st.title("🌍 Global Music Trends: The Climate Connection")
st.markdown("### DSA 210 Term Project | Fall 2025-2026")

with st.expander("📖 Project Motivation & Methodology", expanded=True):
    st.markdown("""
    **Does the weather affect the music we listen to?**
    
    We see climate's effect on culture in clothing and food, but what about subjective concepts like music?
    This project investigates if a country's climate has a measurable effect on its **Shazam Top 30** charts.
    
    * **Music Data:** Shazam Top 30 songs from 68 countries (Oct 21-27, 2025).
    * **Climate Data:** Avg Temp & Rainfall (World Bank & CRU).
    * **Method:** Pearson Correlation Tests & Machine Learning (Decision Tree, K-Means).
    """)

# Use Tabs to structure the story
tab1, tab2, tab3 = st.tabs(["📊 Correlation Analysis", "🤖 Machine Learning Insights", "📝 Conclusions"])

# --- TAB 1: HYPOTHESIS TESTING ---
with tab1:
    st.header("Hypothesis Testing")
    st.write("We performed Pearson Correlation Tests to validate three specific hypotheses.")

    # --- HYPOTHESIS 1: WINTER MELANCHOLY ---
    st.subheader("1. The 'Winter Melancholy' & 'Sunny Disposition'")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Interactive Temp Chart
        chart_temp = alt.Chart(filtered_df).mark_circle(size=60).encode(
            x=alt.X('Average_Temp_Celsius', title='Avg Temperature (°C)', scale=alt.Scale(zero=False)),
            y=alt.Y('Mood', title='Mood', sort='-x'),
            color=alt.Color('Mood', legend=None),
            tooltip=['Title', 'Artist', 'Country', 'Average_Temp_Celsius', 'Mood']
        ).properties(height=400, title="Temperature vs. Music Mood").interactive()
        
        st.altair_chart(chart_temp, use_container_width=True)
    
    with col2:
        st.info("✅ **Hypothesis Supported**")
        st.markdown("""
        **Findings:**
        * **Dark Moods:** Strong negative correlation ($r = -0.57$). As temp drops, 'Dark' music popularity rises.
        * **Dance Moods:** Positive correlation ($r = 0.41$). Warmer countries prefer high-energy dance music.
        """)

    st.divider()

    # --- HYPOTHESIS 2: RAINY DAY VIBE ---
    st.subheader("2. The 'Rainy Day Vibe'")
    
    col3, col4 = st.columns([2, 1])
    
    with col3:
        # Interactive Rain Chart
        chart_rain = alt.Chart(filtered_df).mark_circle(size=60).encode(
            x=alt.X('Rainfall_mm_per_year', title='Rainfall (mm/year)'),
            y=alt.Y('Mood', title='Mood', sort='-x'),
            color=alt.Color('Mood', legend=None),
            tooltip=['Title', 'Artist', 'Country', 'Rainfall_mm_per_year', 'Mood']
        ).properties(height=400, title="Rainfall vs. Music Mood").interactive()
        
        st.altair_chart(chart_rain, use_container_width=True)
        
    with col4:
        st.warning("⚠️ **Hypothesis Not Supported**")
        st.markdown("""
        **Findings:**
        * We hypothesized that rain leads to 'Chill' music.
        * **Result:** Failed to reject Null Hypothesis.
        * **Stats:** $r = 0.21$, $P = 0.096$ (Not statistically significant).
        """)

# --- TAB 2: MACHINE LEARNING ---
with tab2:
    st.header("Beyond Correlation: Machine Learning Results")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("🌲 Decision Tree Classifier")
        st.write("**Goal:** Predict Genre based on Temp & Rainfall.")
        st.metric(label="Model Accuracy", value="40%", delta="Better than random (12.5%)")
        st.markdown("""
        * **Insight:** Rainfall was a more important predictor than Temperature.
        * **Issue:** High class imbalance. The model predicted 'Pop' (the majority class) very well but struggled with niche genres.
        """)
        
    with col_b:
        st.subheader("🔗 K-Means Clustering")
        st.write("**Goal:** Group countries into 'Climate-Music Zones'.")
        st.markdown("""
        * **Result:** Found 3 distinct climate groups (Cold, Moderate, Hot).
        * **Discovery:** **'Pop Universality'**. Pop music was the dominant genre in *all* three clusters, suggesting mainstream music transcends climate barriers.
        """)

# --- TAB 3: CONCLUSIONS ---
with tab3:
    st.header("Final Thoughts & Future Work")
    
    st.markdown("""
    ### 📝 Summary
    While we found a strong correlation between **Cold Weather and Dark Music** ($r=-0.57$), other factors like **Rainfall** were less predictive than expected. The ubiquity of Pop music (Pop Universality) often overpowers subtle climate preferences.
    
    ### 🔮 Limitations & Future Work
    * **Class Imbalance:** 29% of the dataset was Pop. Future work should use **SMOTE** to balance the data.
    * **Time Series:** This was a snapshot of **October 2025**. To see true seasonality (e.g., "Summer Hits"), we need data over 12 months.
    * **Economics:** We need to control for GDP, as economic factors might influence music market maturity more than weather.
    """)