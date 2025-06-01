import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Trading Guide App",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

# Main title of the app
st.title("Trading Guide App :bar_chart:")

# Catchy header introducing your platform
st.header(
    "Empowering Smarter Investments: Your One-Stop Platform for Informed Stock Trading Decisions"
)

# App banner image (ensure 'app.webp' is present in your directory)
st.image("app.webp")

# Section for platform services
st.markdown("## Explore Our Comprehensive Services:")

# 1. Stock Information
st.markdown("#### :one: **Stock Insights & Data**")
st.write(
    "Get up-to-date, detailed information on stocks—including fundamentals, market trends, and recent performance. "
    "Easily access key data to help you research and evaluate investment opportunities."
)

# 2. Stock Prediction
st.markdown("#### :two: **Stock Price Forecasting**")
st.write(
    "Utilize cutting-edge forecasting models to predict the next 30 days’ closing prices based on historical data. "
    "Visualize future trends and leverage predictive analytics to enhance your investment strategy."
)

# 3. CAPM Return
st.markdown("#### :three: **CAPM Expected Return Calculator**")
st.write(
    "Understand potential returns with the Capital Asset Pricing Model. Our tool estimates the expected return for any stock "
    "by evaluating its risk (Beta) and overall market performance, helping you make risk-aware choices."
)

# 4. CAPM Beta
st.markdown("#### :four: **Stock Beta Analysis**")
st.write(
    "Analyze the volatility and risk profile of individual stocks with our Beta calculator. "
    "Assess how your chosen stock might react to market movements and optimize your portfolio accordingly."
)

# (Optional) Add a call-to-action for user engagement
st.markdown("---")
st.success("Ready to start? Select a service from the sidebar to begin your trading journey!")