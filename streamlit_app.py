############## Constistuent.Online #################
####### Code-free analysis for curious folk. ######

### An application for ...

## streamlit run "C:\Users\Jack\Documents\Python_projects\streamlit_apps\matrix_maker\streamlit_app.py"

### --------------------------------------- IMPORTS 

import pandas as pd
import streamlit as st

pd.set_option('display.max_columns', None)

### 
headers = {
    "content-type": "application/json"
}

css = 'body, html, p, h1, .st-emotion-cache-1104ytp h1, [class*="css"] {font-family: "Inter", sans-serif;}'
st.markdown( f'<style>{css}</style>' , unsafe_allow_html= True)

### ---------------------------------------- FUNCTIONS 

def matrix_maker(df, x_col, y_col, sum_col):
    
    df_matrix = pd.DataFrame()
    
    xs = df[x_col].unique()
    ys = df[y_col].unique()
    
    for x in xs:
        for y in ys:            
            v = df.loc[(df[x_col] == x) & (df[y_col] == y), sum_col].sum()
            df_matrix.loc[x, y] = v
            
    return df_matrix
            

### _________________________________________ RUN

st.markdown("**Open Investigation Tools** | [constituent.online](%s)" % 'http://www.constituent.online')
    
st.title('Matrix Maker')
st.write('Convert a long dataframe into a matrix.')


### 


uploaded_file = st.file_uploader("Upload file here &#x2935;", type={"csv"})
if uploaded_file:
    
    #file_name = uploaded_file.name
    
    df = pd.read_csv(uploaded_file)
    
    columns = list(df.columns)
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        x_col = st.selectbox('X column:', columns, index = 0)
    with col2:
        y_col = st.selectbox('Y column:', columns, index = 1)
    with col3:
        sum_col = st.selectbox('Sum column:', columns, index = len(columns) - 1)
        st.markdown('<p class="small-font">This should be a column with numbers only.</p>', unsafe_allow_html=True)

    st.write('')
    st.write('')
    
    df_matrix = matrix_maker(df, x_col, y_col, sum_col)

    st.dataframe(df_matrix, width = 800)
    
    st.markdown('<p class="small-font">Note: if there is more than 1 value returned, the sum total of those values is what will be returned</p>', unsafe_allow_html=True)
    st.markdown("""<style>.small-font {font-size:10px !important; padding: 0; margin: 0; line-height: 6px;}</style>""", unsafe_allow_html=True)
