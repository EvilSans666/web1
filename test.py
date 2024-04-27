import streamlit as st
import seaborn as sns
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.datasets import load_diabetes
import pandas as pd


st.title('Diabetes')
tmp = load_diabetes(as_frame=True)
df = tmp['data']

df


