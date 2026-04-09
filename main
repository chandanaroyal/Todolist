import streamlit as st

st.set_page_config(page_title="To-Do App", layout="centered")

st.title("📱 To-Do List")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add task input
new_task = st.text_input("Add a new task")

if st.button("➕ Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})

st.divider()

# Display tasks
for i, item in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([1, 5, 1])

    # Checkbox
    with col1:
        item["done"] = st.checkbox("", value=item["done"], key=f"check_{i}")

    # Task text
    with col2:
        if item["done"]:
            st.markdown(f"~~{item['task']}~~")
        else:
            st.write(item["task"])

    # Delete button
    with col3:
        if st.button("❌", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

# Clear all button
st.divider()
if st.button("🗑 Clear All"):
    st.session_state.tasks = []
