import seaborn as sns
import streamlit as st

st.title('Dataset')
st.selectbox('Selwct Dataset', sns.get_dataset_names())

df = sns.load_dataset(db)

df