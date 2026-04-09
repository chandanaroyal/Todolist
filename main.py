import streamlit as st

st.set_page_config(page_title="To-Do App", layout="centered")

# White background styling
st.markdown(
    """
    <style>
    .main {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📝 To-Do List")

# Initialize tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "filter" not in st.session_state:
    st.session_state.filter = "ALL"

# Add task
new_task = st.text_input("Enter new task...")

if st.button("➕ ADD"):
    if new_task:
        st.session_state.tasks.append({
            "task": new_task,
            "done": False
        })

st.divider()

# Display tasks
for i, item in enumerate(st.session_state.tasks):
    if st.session_state.filter == "ACTIVE" and item["done"]:
        continue
    if st.session_state.filter == "COMPLETED" and not item["done"]:
        continue

    col1, col2, col3, col4 = st.columns([1, 5, 1, 1])

    # Checkbox
    with col1:
        item["done"] = st.checkbox("", value=item["done"], key=f"check_{i}")

    # Task text
    with col2:
        if item["done"]:
            st.markdown(f"~~{item['task']}~~")
        else:
            st.write(item["task"])

    # Edit button
    with col3:
        if st.button("✏️", key=f"edit_{i}"):
            new_val = st.text_input("Edit task", value=item["task"], key=f"editbox_{i}")
            if new_val:
                item["task"] = new_val

    # Delete button
    with col4:
        if st.button("❌", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

st.divider()

# Filters
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("ALL"):
        st.session_state.filter = "ALL"

with col2:
    if st.button("ACTIVE"):
        st.session_state.filter = "ACTIVE"

with col3:
    if st.button("COMPLETED"):
        st.session_state.filter = "COMPLETED"

# Stats
total = len(st.session_state.tasks)
completed = sum(1 for t in st.session_state.tasks if t["done"])
active = total - completed

st.write(f"{completed}/{total} completed • {active} active")
