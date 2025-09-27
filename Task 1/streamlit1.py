import streamlit as st
import streamlit.components.v1 as components

path_html = "Lab1_task1_net5kings.html"
with open(path_html, 'r', encoding='utf-8') as f:
    html_content = f.read()
    #width/heignht
components.html(html_content, width=900, height=1000) 

    