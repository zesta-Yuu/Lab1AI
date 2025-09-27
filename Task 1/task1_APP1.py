import streamlit as st
import streamlit.components.v1 as components
import os
#path_html = "Lab1_task1_net5kings.html"


#need this for streamlit cloud
path_html = os.path.join(os.path.dirname(__file__), "Lab1_task1_net5kings.html")

with open(path_html, 'r', encoding='utf-8') as f:
    html_content = f.read()

#width/heignht
components.html(html_content, width=900, height=1000) 

    