import streamlit as st

st.set_page_config(
    page_title="Stock Portfolio Tracker",
    page_icon="📈"
)

st.title("📈 Stock Portfolio Tracker")
st.write("Calculate the total value of your stock portfolio.")

st.header("Enter your stocks")

stock1 = st.text_input("Stock 1 name", "Apple")
shares1 = st.number_input("Number of shares", min_value=0.0, value=0.0)
price1 = st.number_input("Price per share", min_value=0.0, value=0.0)

stock2 = st.text_input("Stock 2 name", "Microsoft")
shares2 = st.number_input("Number of shares", min_value=0.0, value=0.0)
price2 = st.number_input("Price per share", min_value=0.0, value=0.0)

if st.button("Calculate Portfolio Value"):
    value1 = shares1 * price1
    value2 = shares2 * price2

    total = value1 + value2

    st.success(f"Total Portfolio Value: ₹{total:,.2f}")
