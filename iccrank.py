import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

# Function to generate random ICC rankings
def generate_rankings():
    teams = ["India", "Australia", "England", "New Zealand", "South Africa", "Pakistan", "West Indies", "Sri Lanka", "Bangladesh"]
    rankings = np.random.randint(1, 10, size=len(teams))
    ranking_data = {"Team": teams, "Ranking": rankings}
    return pd.DataFrame(ranking_data)

def main():
    st.title("ICC Ranking System")
# Company logo
    st.sidebar.image("icc.jpg", use_column_width=True)
    # Generate random ICC rankings
    df = generate_rankings()

    st.subheader("Current ICC Rankings")
    st.write(df)

    

if __name__ == "__main__":
    main()
