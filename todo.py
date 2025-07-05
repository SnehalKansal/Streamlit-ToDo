import streamlit as st
from datetime import datetime
st.set_page_config(page_title="Todo App", page_icon="✅", layout="centered")
if "todos" not in st.session_state:
    st.session_state.todos = []

st.markdown('<h1 class="main-header"> Simple Todo App</h1>', unsafe_allow_html=True)
st.markdown("### Built with Streamlit!")
st.markdown("## Add New Todo")
with st.form("add_todo"):
    new_todo = st.text_input(
        "What do you need to do?", placeholder="Enter your todo here..."
    )
    priority = st.selectbox("Priority:", ["Low", "Medium", "High"])
    submitted = st.form_submit_button("Add Todo")
    if submitted and new_todo.strip():
        todo_item = {
            "task": new_todo.strip(),
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "id": len(st.session_state.todos) + 1,
        }
        st.session_state.todos.append(todo_item)
        st.success(f" Added:{new_todo}")
st.markdown("## Your Todos")
if not st.session_state.todos:
    st.info("No todos yet! Add one above to get started.")

else:
    col1, col2=st.columns(2)
    with col1:
        show_completed = st.checkbox("Show completed todos", value=True)
    with col2:
        if st.button("Clear All Completed"):
            st.session_state.todos = [
                todo for todo in st.session_state.todos if not todo["completed"]
            ]
            st.rerun()
    for todo in st.session_state.todos:
        if not show_completed and todo["completed"]:
            continue
        todo_class = "todo-item completed" if todo["completed"] else "todo-item"
        with st.container():
            st.markdown(f'<div class="{todo_class}">', unsafe_allow_html=True)
            col1, col2, col3, col4=st.columns([3,1,1,1])
            with col1:
                if todo["completed"]:
                    st.markdown(f"~~{todo['created_At']}")
                else:
                    st.write(todo["task"])
                st.caption(f"Created: {todo['created_at']}")
            with col2:
                priority_colors = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}
                st.write(f"{priority_colors[todo['priority']]} {todo['priority']}")

            with col3:
                if st.button(
                    "✅" if not todo["completed"] else "🔄", key=f"toggle_{todo['id']}"
                ):
                    todo["completed"]=not todo["completed"]
                    st.rerun()

            with col4:
                if st.button("🗑️", key=f"delete_{todo['id']}"):
                    st.session_state.todos.remove(todo)
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
if st.session_state.todos:
    st.markdown("## 📊 Statistics")
    total_todos = len(st.session_state.todos)
    completed_todos = len(
        [todo for todo in st.session_state.todos if todo["completed"]]
    )
    pending_todos = total_todos - completed_todos
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Todos", total_todos)
    with col2:
        st.metric("Completed", completed_todos)
    with col3:
        st.metric("Pending", pending_todos)
    if total_todos > 0:
        progress = completed_todos / total_todos
        st.progress(progress)
        st.caption(f"Progress: {progress:.1%}")











































































