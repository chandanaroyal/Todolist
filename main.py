import streamlit as st

st.set_page_config(page_title="To-Do App", layout="centered")

# --------- STYLE (WHITE CARD UI) ----------
st.markdown("""
<style>
body {
    background-color: #f4f4f4;
}

.main {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 15px;
    border: 2px solid black;
    max-width: 600px;
    margin: auto;
}

h1, h2, h3, p {
    color: black;
    text-align: center;
}

.stTextInput input {
    background-color: #ffffff;
    color: black;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 10px;
}

.stButton>button {
    background-color: #2f5eff;
    color: white;
    border-radius: 8px;
    font-weight: bold;
    height: 40px;
}

.task-box {
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# --------- TITLE ----------
st.markdown("<h1>To Do List</h1>", unsafe_allow_html=True)

# --------- SESSION ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --------- INPUT (ALIGNED) ----------
col1, col2 = st.columns([6,2], vertical_alignment="bottom")

with col1:
    new_task = st.text_input("", placeholder="Enter new task...", label_visibility="collapsed")

with col2:
    add_clicked = st.button("Add", use_container_width=True)

if add_clicked and new_task:
    st.session_state.tasks.append({"task": new_task, "done": False})

st.markdown("<h3>Task List</h3>", unsafe_allow_html=True)

# --------- TASK LIST (UPDATED UI) ----------
for i, item in enumerate(st.session_state.tasks):

    col1, col2, col3, col4 = st.columns([1,6,1,1])

    with col1:
        item["done"] = st.checkbox("", value=item["done"], key=f"check_{i}")

    # 🔥 Task box (like search bar)
    with col2:
        task_style = f"""
        <div style="
            background-color: #ffffff;
            border: 1px solid #ccc;
            border-radius: 12px;
            padding: 12px;
            font-size: 18px;
            {'text-decoration: line-through; color: gray;' if item['done'] else ''}
            {item['task']}
        </div>
        """
        st.markdown(task_style, unsafe_allow_html=True)

    with col3:
        if st.button("Edit", key=f"edit_{i}"):
            new_val = st.text_input("Edit task", value=item["task"], key=f"editbox_{i}")
            if new_val:
                item["task"] = new_val

    with col4:
        if st.button("Delete", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()
# --------- STATS ----------
completed = sum(1 for t in st.session_state.tasks if t["done"])
total = len(st.session_state.tasks)

st.markdown("---")
st.markdown(f"<p>Completed: {completed} | Uncompleted: {total-completed}</p>", unsafe_allow_html=True)

# --------- CLEAR ALL ----------
if st.button("Clear All"):
    st.session_state.tasks = []
    st.rerun()
