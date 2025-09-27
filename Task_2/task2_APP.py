import streamlit as st
import os
import graph
#from . import Class_GameOfThronesGraph

#title
st.title("Task2: infographic of relationships between characters in the Game of Thrones")
#tabs for Game of thrones
tab1, tab2, tab3 = st.tabs(["Game of Thrones Houses", "Members of Houses", "Lab1. Task2"])

with tab1:
    st.header("Game of Thrones Houses")
    for house in graph.Class_GameOfThronesGraph.GameOfThronesHouses:
        st.write(f'{house}: Strength {house.getStrength()}')
        #dynaties strength graph 
    st.pyplot(graph.fig)
    
with tab2:
    st.header("Members of Houses")
    for house in graph.Class_GameOfThronesGraph.GameOfThronesHouses:
            st.write(f'{house}!')
            for person in house:
                st.markdown(f'* {person} ')
                #house stengths
            st.write(f"We have {house.getStrength()} family members!!!")
            st.write("\n")
            
with tab3:
    st.header("Lab1. Task2")
    import streamlit.components.v1 as components
    #need this for streamlit cloud
    path_html = os.path.join(os.path.dirname(__file__), "Lab1_Taks2_GameOfThrones.html")

    with open(path_html, 'r', encoding='utf-8') as f:
        html_content = f.read()

    #width/heignht
    components.html(html_content,height=900,scrolling=True)

    