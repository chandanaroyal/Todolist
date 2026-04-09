import streamlit as st

st.set_page_config(page_title="To-Do App", layout="centered")

# --------- CUSTOM STYLE (MATCH IMAGE) ----------
st.markdown("""
<style>
body {
    background-color: #f5f5f5;
}
.main {
    background-color: #ffffff;
    padding: 20px;
    border: 2px solid black;
}

button {
    border: 2px solid black !important;
    background-color: #e8e4d9 !important;
    color: black !important;
    font-weight: bold !important;
}

.task-box {
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 5px;
}

.completed {
    text-decoration: line-through;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# --------- TITLE ----------
st.markdown("## 📝 To-Do List")

# --------- SESSION ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "filter" not in st.session_state:
    st.session_state.filter = "ALL"

# --------- INPUT ----------
col1, col2 = st.columns([4,1])

with col1:
    new_task = st.text_input("Enter new task...", label_visibility="collapsed")

with col2:
    if st.button("+ ADD"):
        if new_task:
            st.session_state.tasks.append({"task": new_task, "done": False})

st.markdown("---")

# --------- TASK LIST ----------
for i, item in enumerate(st.session_state.tasks):

    if st.session_state.filter == "ACTIVE" and item["done"]:
        continue
    if st.session_state.filter == "COMPLETED" and not item["done"]:
        continue

    col1, col2, col3, col4 = st.columns([1,6,1,1])

    # Checkbox
    with col1:
        item["done"] = st.checkbox("", value=item["done"], key=f"check_{i}")

    # Task text
    with col2:
        if item["done"]:
            st.markdown(f"<div class='completed'>{item['task']}</div>", unsafe_allow_html=True)
        else:
            st.write(item["task"])

    # Edit
    with col3:
        if st.button("✏️", key=f"edit_{i}"):
            new_val = st.text_input("Edit task", value=item["task"], key=f"editbox_{i}")
            if new_val:
                item["task"] = new_val

    # Delete
    with col4:
        if st.button("❌", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

st.markdown("---")

# --------- FILTER BUTTONS ----------
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

# --------- STATUS ----------
total = len(st.session_state.tasks)
completed = sum(1 for t in st.session_state.tasks if t["done"])
active = total - completed

st.markdown(f"**{completed}/{total} COMPLETED • {active} ACTIVE**")
