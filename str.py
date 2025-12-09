import streamlit as st

st.set_page_config(page_title="Simple To-Do List")

# Title
st.title("Simple To-Do List")

# Session state to store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input for a new task
new_task = st.text_input("Add a new task:")

if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append(new_task.strip())
        st.experimental_rerun()

# Display tasks
st.subheader("Your Tasks")
if len(st.session_state.tasks) == 0:
    st.write("No tasks yet… lucky you.")
else:
    for i, task in enumerate(st.session_state.tasks):
        cols = st.columns([6, 1])
        cols[0].write(f"- {task}")
        if cols[1].button("❌", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
