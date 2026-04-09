import streamlit as st

st.set_page_config(page_title="To-Do App", layout="centered")

# --------- DARK STYLE ----------
st.markdown("""
<style>
body {
    background-color: #e6d3a3;
}
.main {
    background-color: #1e1e1e;
    padding: 25px;
    border-radius: 15px;
    border: 3px solid #2f5eff;
}

h1, h2, h3, p {
    color: white;
}

button {
    border-radius: 8px !important;
    font-weight: bold !important;
}

.stButton>button {
    background-color: #2f5eff;
    color: white;
}

.delete-btn {
    color: red;
    font-weight: bold;
}

.task-box {
    border: 1px solid #555;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# --------- TITLE ----------
st.markdown("<h1 style='text-align:center;'>To Do List</h1>", unsafe_allow_html=True)

# --------- SESSION ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --------- INPUT ----------
col1, col2 = st.columns([4,1])

with col1:
    new_task = st.text_input("", placeholder="Enter task...")

with col2:
    if st.button("Add"):
        if new_task:
            st.session_state.tasks.append({"task": new_task, "done": False})

st.markdown("<h3 style='text-align:center;'>Task List</h3>", unsafe_allow_html=True)

# --------- TASK LIST ----------
for i, item in enumerate(st.session_state.tasks):
    col1, col2, col3, col4 = st.columns([1,5,1,1])

    # Checkbox
    with col1:
        item["done"] = st.checkbox("", value=item["done"], key=f"check_{i}")

    # Task text
    with col2:
        if item["done"]:
            st.markdown(f"<span style='color:gray; text-decoration: line-through;'>{item['task']}</span>", unsafe_allow_html=True)
        else:
            st.write(item["task"])

    # Delete
    with col3:
        if st.button("Delete", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

    # Edit
    with col4:
        if st.button("Edit", key=f"edit_{i}"):
            new_val = st.text_input("Edit task", value=item["task"], key=f"editbox_{i}")
            if new_val:
                item["task"] = new_val

# --------- STATS ----------
completed = sum(1 for t in st.session_state.tasks if t["done"])
total = len(st.session_state.tasks)
remaining = total - completed

st.markdown("---")
st.markdown(
    f"<p style='text-align:center;'>Completed: {completed} | Uncompleted: {remaining}</p>",
    unsafe_allow_html=True
)

# --------- CLEAR ALL ----------
if st.button("Clear All"):
    st.session_state.tasks = []
    st.rerun()
