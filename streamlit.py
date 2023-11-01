import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

# df = pd.read_csv('')
df = sns.load_dataset('titanic')
pr = df.profile_report()

st_profile_report(pr) # to display data EDA report on dashboard.
st.title('My first app')

