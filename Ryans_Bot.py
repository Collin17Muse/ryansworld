import streamlit as st
import random
import datetime
import matplotlib.pyplot as plt
import numpy as np

# Mock knowledge base of financial articles
mock_articles = [
    {
        "title": "Understanding Inflation",
        "content": "Inflation is the rate at which the general level of prices for goods and services is rising, and subsequently, purchasing power is falling. Central banks attempt to limit inflation, and avoid deflation, in order to keep the economy running smoothly. Common measures include CPI and PPI."
    },
    {
        "title": "What is Compound Interest?",
        "content": "Compound interest is interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods. It accelerates wealth growth over time, especially with regular contributions."
    },
    {
        "title": "How Stock Markets Work",
        "content": "Stock markets provide a platform for investors to buy and sell shares in public companies. They are essential to the economy, allowing companies to raise capital and giving investors the opportunity to earn returns. Examples include NYSE and NASDAQ."
    },
    {
        "title": "Introduction to Cryptocurrency",
        "content": "Cryptocurrency is a digital or virtual currency secured by cryptography, making it nearly impossible to counterfeit. Most cryptocurrencies are decentralized networks based on blockchain technology. Bitcoin, Ethereum, and Litecoin are popular examples."
    },
    {
        "title": "Budgeting and Financial Planning",
        "content": "Budgeting involves creating a plan to manage your income and expenses. Effective financial planning helps ensure you can meet short-term obligations while saving for long-term goals. Key steps include tracking spending, setting savings goals, and reviewing debt levels."
    },
    {
        "title": "Understanding Credit Scores",
        "content": "A credit score is a number that represents your creditworthiness. It's based on your credit history, including the number of accounts, total levels of debt, repayment history, and other factors. Higher scores typically lead to better borrowing terms."
    }
]

# Expanded FAQ database
faqs = {
    "what is inflation": "Inflation is the rate at which prices increase, reducing purchasing power.",
    "how does compound interest work": "Compound interest adds interest to the principal and previously earned interest.",
    "what is cryptocurrency": "Cryptocurrency is a secure digital currency built on blockchain.",
    "how does the stock market work": "The stock market allows trading of company shares and supports capital raising.",
    "what is a budget": "A budget is a financial plan to manage income and expenses.",
    "how is credit score calculated": "Credit scores consider payment history, amounts owed, length of credit history, and credit types."
}

# Search knowledge base
def search_articles(query):
    results = []
    for article in mock_articles:
        if query.lower() in article["title"].lower() or query.lower() in article["content"].lower():
            results.append(article)
    return results if results else random.sample(mock_articles, 1)

# Answer FAQ
def answer_faq(query):
    query = query.lower().strip()
    for q in faqs:
        if q in query:
            return faqs[q]
    return None

# Streamlit setup
st.set_page_config(page_title="Financial Chatbot", layout="wide")
st.title("💬 Ryan's Financial Knowledge Bot")

st.markdown("Ask anything about personal finance, markets, or money concepts. Ryan will guide you like a helpful advisor!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("👤 You:", key="input")

if user_input:
    st.session_state.chat_history.append({"role": "user", "message": user_input})
    faq_answer = answer_faq(user_input)

    if faq_answer:
        response = f"🧠 Ryan: {faq_answer}"
    else:
        matched_articles = search_articles(user_input)
        response = "\n".join([f"📘 {a['title']}\n{a['content']}" for a in matched_articles])
        response = f"🧠 Ryan: I found something that might help!\n{response}"

    st.session_state.chat_history.append({"role": "bot", "message": response})

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['message']}")
    else:
        st.markdown(chat["message"])

# Inflation chart
def show_inflation_chart():
    st.subheader("📈 Simulated Inflation Rate Over Time")
    years = np.arange(2010, 2024)
    inflation_rate = np.random.uniform(1.0, 6.0, len(years))

    fig, ax = plt.subplots()
    ax.plot(years, inflation_rate, marker='o')
    ax.set_title("Simulated Inflation Trend")
    ax.set_xlabel("Year")
    ax.set_ylabel("Inflation Rate (%)")
    st.pyplot(fig)

# Compound interest chart
def show_compound_interest_chart(principal, rate, years):
    st.subheader("📊 Compound Interest Growth Simulation")
    t = np.arange(0, years + 1)
    amounts = principal * (1 + rate / 100) ** t

    fig, ax = plt.subplots()
    ax.plot(t, amounts, marker='o')
    ax.set_title("Growth of Investment with Compound Interest")
    ax.set_xlabel("Years")
    ax.set_ylabel("Value ($)")
    st.pyplot(fig)

# Visual toggles
if st.checkbox("📉 Show Simulated Inflation Chart"):
    show_inflation_chart()

if st.checkbox("💹 Run Compound Interest Simulation"):
    principal = st.slider("Initial Principal ($)", 1000, 10000, 5000, step=500)
    rate = st.slider("Annual Interest Rate (%)", 1, 15, 5)
    years = st.slider("Number of Years", 1, 30, 10)
    show_compound_interest_chart(principal, rate, years)

# Sidebar
with st.sidebar:
    st.header("🧰 Chatbot Features")
    st.markdown("- Smart FAQ responses")
    st.markdown("- Financial article search")
    st.markdown("- Simulated charts")
    st.markdown("- Friendly human-like responses")
    st.write("🕒 Current Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
