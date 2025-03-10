import streamlit as st


def main():
    x = st.slider("Select a value")
    st.write(x, "squared is", x * x)


if __name__ == "__main__":
    main()
