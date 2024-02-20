import streamlit as st

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """

from PIL import Image

im = Image.open('/Users/agniksarkar/Automated_EDA/business-analytics-icon-data-analysis-illustration-sign-data-science-symbol-profit-graph-logo-vector.jpg')

st.set_page_config( page_title="Automated EDA App", page_icon = im ,layout="wide")
st.markdown(hide_default_format, unsafe_allow_html=True)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use("Agg")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Automatic EDA and Plot generator for Datasets")
st.markdown("This webapp is maintained by Agnik Sarkar")

def main():
    activies=['EDA', 'PLOTS']
    choices = st.sidebar.selectbox("Select Activities", activies)
    if choices=="EDA":
        st.subheader("Exploratory Data Analysis")
        data=st.file_uploader("Upload a dataset", type=["csv", "txt"])
        if data is not None:
            df=pd.read_csv(data)
            st.dataframe(df.head())
        if st.checkbox("Show Shape"):
            st.write(df.shape)
        if st.checkbox("Show Describe"):
            st.write(df.describe())
        if st.checkbox("Show Columns"):
            all_columns = df.columns.to_list()
            st.write(all_columns)
        if st.checkbox("Show Selected Column"):
            selected_columns  = st.multiselect("Select Columns", all_columns)
            new_df = df[selected_columns]
            st.dataframe(new_df)
        if st.checkbox("Show Value Counts"):
            st.write(df.iloc[:, -1].value_counts())
        if st.checkbox("Correlation Matrix"):
            plt.matshow(df.corr())
            st.pyplot()
        if st.checkbox("Correlation Matrix(Seaborn)"):
            st.write(sns.heatmap(df.corr(), annot=True))
            st.pyplot()
    elif choices == 'PLOTS':
        st.subheader("Data Visualization")
        data=st.file_uploader("Upload a dataset", type=["csv", "txt", "xlsx"])
        if data is not None:
            df=pd.read_csv(data)
            st.dataframe(df.head())
            if st.checkbox("Show Value Counts"):
                st.write(df.iloc[:, -1].value_counts().plot(kind="bar"))
                st.pyplot()
            all_columns = df.columns.to_list()
            type_of_plot = st.selectbox("Select plot type", ["area","bar","line","hist", "box","kde"])
            selected_columns = st.multiselect("Select columns to plot", all_columns)

            if st.button("Generate Plot"):
                st.success("Plot is Generated")
                if type_of_plot=='area':
                    new_extracted_df = df[selected_columns]
                    st.area_chart(new_extracted_df)
                if type_of_plot=='bar':
                    new_extracted_df = df[selected_columns]
                    st.bar_chart(new_extracted_df)
                if type_of_plot=='line':
                    new_extracted_df = df[selected_columns]
                    st.line_chart(new_extracted_df)
                else:
                    new_extracted_df_plot = df[selected_columns].plot(kind=type_of_plot)
                    st.write(new_extracted_df_plot)
                    st.pyplot()
# Main
if __name__=="__main__":
    main()