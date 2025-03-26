import streamlit as st

def main():
    st.title("Simple Calculator")
    st.write("Enter a mathematical expression and get the result.")
    
    expression = st.text_input("Enter expression (e.g., 5 + 3 * 2):", "")
    
    if st.button("Calculate"):
        try:
            result = eval(expression)  # Be cautious with eval
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
