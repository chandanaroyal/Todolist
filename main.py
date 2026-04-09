import streamlit as st

st.set_page_config(page_title="To-Do App", layout="centered")

# --------- MODE SWITCH ----------
if "mode" not in st.session_state:
    st.session_state.mode = "dark"

toggle = st.toggle("🌙 Dark Mode", value=True)

if toggle:
    st.session_state.mode = "dark"
else:
    st.session_state.mode = "light"

# --------- STYLES ----------
if st.session_state.mode == "dark":
    bg_color = "#0b1220"
    card_color = "#1e1e1e"
    text_color = "white"
    border_color = "#2f5eff"
    button_color = "#2f5eff"
else:
    bg_color = "#f4f4f4"
    card_color = "#ffffff"
    text_color = "black"
    border_color = "#000000"
    button_color = "#4CAF50"

st.markdown(f"""
<style>
body {{
    background-color: {bg_color};
}}

.main {{
    background-color: {card_color};
    padding: 25px;
    border-radius: 15px;
    border: 3px solid {border_color};
}}

h1, h2, h3, p {{
    color: {text_color};
}}

.stTextInput input {{
    background-color: {"#2b2b2b" if st.session_state.mode=="dark" else "#ffffff"};
    color: {text_color};
    border-radius: 10px;
}}

.stButton>button {{
    background-color: {button_color};
    color: white;
    border-radius: 8px;
    font-weight: bold;
}}

.task-box {{
    border: 1px solid gray;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
}}
</style>
""", unsafe_allow_html=True)

# --------- TITLE ----------
st.markdown("<h1 style='text-align:center;'>To Do List</h1>", unsafe_allow_html=True)

# --------- SESSION ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --------- INPUT ----------
col1, col2 = st.columns([5,1])

with col1:
    new_task = st.text_input("", placeholder="Enter new task...", label_visibility="collapsed")

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    add_clicked = st.button("Add", use_container_width=True)

if add_clicked and new_task:
    st.session_state.tasks.append({"task": new_task, "done": False})

st.markdown("<h3 style='text-align:center;'>Task List</h3>", unsafe_allow_html=True)

# --------- TASK LIST ----------
for i, item in enumerate(st.session_state.tasks):
    col1, col2, col3, col4 = st.columns([1,5,1,1])

    with col1:
        item["done"] = st.checkbox("", value=item["done"], key=f"check_{i}")

    with col2:
        if item["done"]:
            st.markdown(f"<span style='color:gray; text-decoration: line-through;'>{item['task']}</span>", unsafe_allow_html=True)
        else:
            st.write(item["task"])

    with col3:
        if st.button("❌", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

    with col4:
        if st.button("✏️", key=f"edit_{i}"):
            new_val = st.text_input("Edit task", value=item["task"], key=f"editbox_{i}")
            if new_val:
                item["task"] = new_val

# --------- STATS ----------
completed = sum(1 for t in st.session_state.tasks if t["done"])
total = len(st.session_state.tasks)

st.markdown("---")
st.markdown(f"<p style='text-align:center;'>Completed: {completed} | Uncompleted: {total-completed}</p>", unsafe_allow_html=True)

# --------- CLEAR ----------
if st.button("🗑 Clear All"):
    st.session_state.tasks = []
    st.rerun()
