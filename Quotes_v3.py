import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Daily Inspiration",
    layout="centered"
)

# ---------------- SESSION STATE INIT ----------------
if "saved_quotes" not in st.session_state:
    st.session_state.saved_quotes = []

if "current_quote" not in st.session_state:
    st.session_state.current_quote = None

# ---------------- MOBILE BUTTON STYLING ----------------
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        height: 50px;
        font-size: 18px;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center;'>🌟 Daily Inspiration</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:grey;'>Tap below for a fresh quote</p>",
    unsafe_allow_html=True
)

# ---------------- TABS ----------------
tab1, tab2 = st.tabs(["✨ Inspire", "❤️ Saved Quotes"])

# ================= TAB 1: INSPIRE =================
with tab1:

    if st.button("✨ Inspire Me"):
        with st.spinner("Finding something inspiring for you..."):
            response = requests.get("https://zenquotes.io/api/random")
            data = response.json()

            st.session_state.current_quote = {
                "quote": data[0]["q"],
                "author": data[0]["a"]
            }

    # Show quote if it exists
    if st.session_state.current_quote is not None:
        quote = st.session_state.current_quote["quote"]
        author = st.session_state.current_quote["author"]

        st.markdown(
            f"""
            <div style="
                background-color:#f9f9f9;
                padding:20px;
                border-radius:12px;
                box-shadow:0px 4px 10px rgba(0,0,0,0.1);
                text-align:center;
            ">
                <p style="font-size:20px; font-style:italic;">
                    “{quote}”
                </p>
                <p style="margin-top:10px; font-weight:bold;">
                    — {author}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("❤️ Save this quote"):
            st.session_state.saved_quotes.append(
                st.session_state.current_quote
            )
            st.success("Quote saved!")

# ================= TAB 2: SAVED QUOTES =================
with tab2:

    st.subheader("❤️ Your Saved Quotes")

    if len(st.session_state.saved_quotes) == 0:
        st.write("No saved quotes yet.")
    else:
        for item in st.session_state.saved_quotes:
            st.markdown(
                f"""
                <div style="
                    background-color:#ffffff;
                    padding:15px;
                    border-radius:10px;
                    margin-bottom:10px;
                    border-left:4px solid #ff4b4b;
                ">
                    <p style="font-style:italic;">
                        “{item['quote']}”
                    </p>
                    <p style="font-weight:bold;">
                        — {item['author']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
