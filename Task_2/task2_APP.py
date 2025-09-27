import streamlit as st
from . import graph
from . import Class_GameOfThronesGraph

#st.set_page_config(layout="wide") -> increases page width
#title
st.title("Task2: infographic of relationships between characters in the Game of Thrones")
#tabs for Game of thrones
tab1, tab2, tab3 = st.tabs(["Game of Thrones Houses", "Members of Houses", "Lab1. Task2"])

with tab1:
    st.header("Game of Thrones Houses")
    for house in Class_GameOfThronesGraph.GameOfThronesHouses:
        st.write(f'{house}: Strength {house.getStrength()}')
        #dynaties strength graph 
    st.pyplot(graph.fig)
    
with tab2:
    st.header("Members of Houses")
    for house in Class_GameOfThronesGraph.GameOfThronesHouses:
            st.write(f'{house}!')
            for person in house:
                st.markdown(f'* {person} ')
                #house stengths
            st.write(f"We have {house.getStrength()} family members!!!")
            st.write("\n")
            
with tab3:
    st.header("Lab1. Task2")
    import streamlit.components.v1 as components
    path_html = "Lab1_Taks2_GameOfThrones.html"
    with open(path_html, 'r', encoding='utf-8') as f:
        html_content = f.read()
    components.html(html_content, height= 1010, scrolling=True) 

    