import streamlit as st

def hello_world():
    return "Olá Mundo. Meu Dash já está online e funcionando."

def main():
    st.write(hello_world())

if __name__ == "__main__":
    main()