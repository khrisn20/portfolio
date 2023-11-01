import streamlit as st  

#Page Configuration
st.set_page_config(page_title="My Portfolio", layout="wide")
project_image_1 = "images\merge_conflict.JPG"

#Header Section
with st.container():
    st.subheader("Hi, I am Christian")
    st.title("A Software Developer based in Tampa, FL")
    st.write("I have 4 years of IT experience with the military in which I have been tasked with roles in different areas of competency.")
    st.write("[Git Hub >](https://github.com/khrisn20)")

#Summary Section
with st.container():
    st.write("---")
    with st.container():
        st.header("Summary")
        st.write("##")
        st.write(
            """
            In this Portfolio I will display the projects I work on during my job search for a Software Development role.
            Some of the projects I will be working on are:
            - A web scraper that scrapes car price data from online car marketplaces.
            - A Python script that consumes and API with Car Data.
            - A data cleaning pipeline in Jupyter notebooks that cleans the data gathered in the previous two projects.
            - A data science/machine learning pipeline that preprocesses and trains a machine learning model.
            - A web app that allows users to make predictions on Car Depreciation based on predictions made by the model in the previous project.
            - After presenting this projects I will move on to present three Java projects(IMS, Scheduler, Rest API) I made when I was learning how to code.
            """
        )

#Projects Section
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(project_image_1)

    with text_column:
        st.subheader("Web Scraper")
        st.write(
            """
            In this project I will be ncjhdh djakbhbdbvhdvbhv.
            cnbdjan bvjuie vbjuieb cbjdswi bvcdwisv jbndwbv ncjdkvbn cjdkwsbvjid vbndjvbdv nbjd bnvjd bjd.
            vbdjskvbnjfdvnbj ncjdswnvjd jvnjdwsnv nvjdwnv nvfjdw nvjdkln  nvfjdwnk.
            """
        )
        st.markdown("[See Repo](https://github.com/khrisn20)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(project_image_1)

    with text_column:
        st.subheader("Web Scraper")
        st.write(
            """
            In this project I will be ncjhdh djakbhbdbvhdvbhv.
            cnbdjan bvjuie vbjuieb cbjdswi bvcdwisv jbndwbv ncjdkvbn cjdkwsbvjid vbndjvbdv nbjd bnvjd bjd.
            vbdjskvbnjfdvnbj ncjdswnvjd jvnjdwsnv nvjdwnv nvfjdw nvjdkln  nvfjdwnk.
            """
        )
        st.markdown("[See Repo](https://github.com/khrisn20)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(project_image_1)

    with text_column:
        st.subheader("Web Scraper")
        st.write(
            """
            In this project I will be ncjhdh djakbhbdbvhdvbhv.
            cnbdjan bvjuie vbjuieb cbjdswi bvcdwisv jbndwbv ncjdkvbn cjdkwsbvjid vbndjvbdv nbjd bnvjd bjd.
            vbdjskvbnjfdvnbj ncjdswnvjd jvnjdwsnv nvjdwnv nvfjdw nvjdkln  nvfjdwnk.
            """
        )
        st.markdown("[See Repo](https://github.com/khrisn20)")
