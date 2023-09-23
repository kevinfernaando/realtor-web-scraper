import streamlit as st
from function import *

st.title("Realtor Web Scraper")
location = st.text_input("Location (City, State)", placeholder="e.g: Manhattan, NY")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("##### Price")
with col2:
    min_price = st.number_input("Min. Price")
with col3:
    max_price = st.number_input("Max. Price")


col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("##### Property Type")
with col2:
    property_type = st.multiselect(
        "Property Type",
        ("House", "Condo", "Townhome", "Multi Family", "Mobile", "Farm", "Land"),
    )


col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("##### Bedrooms")
with col2:
    min_bed = st.selectbox("Min. Bedrooms", ("No Min", "Studio", 1, 2, 3, 4, 5))
with col3:
    max_bed = st.selectbox("Max. Bedrooms", ("No Max", "Studio", 1, 2, 3, 4, 5))


col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("##### Bathrooms")
with col2:
    min_bath = st.selectbox("Min. Bathrooms", ("No Min", 1, 2, 3, 4, 5))
with col3:
    max_bath = st.selectbox("Max. Bathrooms", ("No Max", 1, 2, 3, 4, 5))


col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("##### Keyword")
with col2:
    keyword = st.text_input("Keyword", placeholder="Seperate with comma")


btn = st.button("Scrape Data")
if btn:
    if min_price <= 0.0:
        min_price = None

    if max_price <= 0.0:
        max_price = None

    # type-single-family-home,condo,townhome,multi-family-home,mfd-mobile-home,farms-ranches
    property_dict = {
        "House": "single-family-home",
        "Condo": "condo",
        "Townhome": "townhome",
        "Multi Family": "multi-family-home",
        "Mobile": "mfd-mobile-home",
        "Farm": "farms-ranches",
        "Land": "land",
    }
    if len(property_type) == 0:
        property_type = None
    else:
        property_type = [property_dict[type] for type in property_type]
        property_type = ",".join(property_type)

    if min_bed == "No Min":
        min_bed = None

    if max_bed == "No Max":
        max_bed = None

    if min_bath == "No Min":
        min_bath = None

    if max_bath == "No Max":
        max_bath = None

    if keyword == "":
        keyword = None
    else:
        final_keyword = []
        words = keyword.split(",")
        for word in words:
            word = "-".join(word.split())
            final_keyword.append(word)
        keyword = ",".join(final_keyword)

    params_string = [
        "location",
        "min_price",
        "max_price",
        "property_type",
        "min_bed",
        "max_bed",
        "min_bath",
        "max_bath",
        "keyword",
    ]

    print(location)
    print(min_price)
    print(max_price)
    print(property_type)
    print(min_bed)
    print(max_bed)
    print(min_bath)
    print(max_bath)
    print(keyword)

    params = {key: eval(key) for key in params_string}
    print(generate_url(**params))
    df = scrape_data(params)

    st.dataframe(df)

    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode("utf-8")

    csv = convert_df(df)

    st.download_button(
        label="Download Data",
        data=csv,
        file_name=f"{location} Data.csv",
        mime="text/csv",
    )
