import streamlit as st

st.set_page_config(
    page_title = "Trading App",
    page_icon = "chart_with_upwards_trend:",
    layout = "wide"
)

st.title("Trading Guide App :bar_chart:")

st.header("We provide the greatest platform for you to collect all information prior to investing in stocks.")

st.image("app.webp")

st.markdown("## We provide the following services: ")

st.markdown("#### :one: Stock Information")
st.write("Through this page, you can see all the information about stocks.")

st.markdown("#### :two: Stock Prediction")
st.write("You can explore predicted closing prices for the next 30 days based on historical stock data and advanced forecasting models. Use thiss tool to gain valuablt insights into market trends and make informed investment decisions.")

st.markdown("#### :three: CAPM Return")
st.write("Discover how the Capital Asset Prcing Model calculates the expected return of different stocks asses based on its risk and market performance.")

st.markdown("#### :four: CAPM Beta")
st.write("Calculates Beta and Expected Return for individual Stocks.")