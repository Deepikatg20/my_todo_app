import streamlit as st
import modules.function

todos = modules.function.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    modules.function.write_todos(todos)


st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key =todo)
    if checkbox:
        todos.pop(index)
        modules.function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = "Enter a todo", placeholder="Add new todo..", on_change=add_todo, key="new_todo")


st.session_state
