import streamlit as st
from CatFriendlyHouseEnvClass import *
from agents import TableDrivenAgent

if 'house' not in st.session_state:
    st.session_state.house = CatFriendlyHouseEnvironment()
    st.session_state.cat_agent = TableDrivenAgent()
    st.session_state.house.add_thing(st.session_state.cat_agent, start_performance=10)
    st.session_state.steps = 0

def run_step():
    if not st.session_state.house.is_done() and st.session_state.steps < 4:
        st.session_state.house.step()
        st.session_state.steps += 1
    else:
        st.session_state.is_done = True


st.title("Cat Friendly House Simulation")
st.subheader(f"Step {st.session_state.steps}")

cat = st.session_state.cat_agent
house = st.session_state.house

#bold = **text**
st.markdown(f"**Agent Status:** {cat.show_state()}")
st.progress(cat.performance / 25, text=f"Performance: {cat.performance:.2f}") 

room_info = []
for loc in LOCATIONS:
    items = house.status.get(loc, [])
    item_str = f"Item: **{items[0].__class__.__name__}**" if items else "Empty"
    room_info.append(f"Room **{loc}**: {item_str}")

st.markdown("---")
st.markdown("### House State")
st.markdown("\n".join(room_info))

# Simulation Control
if not st.session_state.house.is_done() and st.session_state.steps < 4:
    st.button("Run Next Step", on_click=run_step)
elif st.session_state.steps >= 4:
    st.success("Simulation Complete")
else:
    st.error("Simulation Ended")