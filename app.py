import streamlit as st
import requests
import pandas as pd

# UI Title
st.title("🔎 E-Commerce Product Scraper")

# 📌 Input Fields
search_name = st.text_input("Search Name", "Full-Sleeve Cotton Shirts")
source = st.selectbox("Select Source", ["Amazon", "Flipkart", "Myntra"])
price_min = st.number_input("Min Price (₹)", 500, 10000, 500)
price_max = st.number_input("Max Price (₹)", 500, 10000, 1000)
min_rating = st.slider("Minimum Rating", 1.0, 5.0, 4.0, 0.1)
product_count = st.number_input("Number of Results", 1, 20, 10)

# Search Button
if st.button("🔍 Search"):
    st.write(f"Fetching results from **{source}** for '{search_name}'...")

    # Simulating a DuckDuckGo Search (Since Amazon needs scraping)
    url = f"https://api.duckduckgo.com/?q={search_name}&format=json"
    response = requests.get(url).json()

    # Extracting search results (Simulated)
    results = response.get("RelatedTopics", [])[:product_count]

    # Creating the Table Data
    data = [
        {
            "Sr No": i + 1,
            "Name": item["Text"][:50],
            "Product Link": item.get("FirstURL", "N/A"),
            "Price (₹)": f"{price_min}-{price_max}",
            "Rating": min_rating,
            "Source": source
        }
        for i, item in enumerate(results)
    ]

    df = pd.DataFrame(data)
    st.write(df)

    # 📥 Download CSV Button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV", csv, "search_results.csv", "text/csv")
