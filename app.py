import streamlit as st

st.set_page_config(
    page_title="Stock Portfolio Tracker",
    page_icon="📈",
    layout="centered"
)

# Manually defined stock prices in USD
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

st.title("📈 Stock Portfolio Tracker")
st.write("Calculate the total value of your stock investments.")

st.subheader("Enter Your Stock Quantities")

quantities = {}

for stock, price in stock_prices.items():
    quantities[stock] = st.number_input(
        f"{stock} — Price: ${price}",
        min_value=0,
        step=1,
        value=0
    )

if st.button("Calculate Portfolio", type="primary"):
    total = 0
    results = []

    for stock, quantity in quantities.items():
        price = stock_prices[stock]
        investment = price * quantity
        total += investment

        if quantity > 0:
            results.append({
                "Stock": stock,
                "Quantity": quantity,
                "Price ($)": price,
                "Investment ($)": investment
            })

    if results:
        st.subheader("Portfolio Results")
        st.dataframe(results, use_container_width=True)

        st.success(f"Total Investment: ${total:,.2f}")

        # Create a downloadable report
        report = "STOCK PORTFOLIO REPORT\n\n"

        for item in results:
            report += (
                f"{item['Stock']}: "
                f"{item['Quantity']} shares x "
                f"${item['Price ($)']} = "
                f"${item['Investment ($)']:,.2f}\n"
            )

        report += f"\nTotal Investment: ${total:,.2f}"

        st.download_button(
            "Download Portfolio Report",
            data=report,
            file_name="portfolio_result.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please enter a quantity for at least one stock.")
