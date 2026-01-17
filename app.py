import streamlit as st
from aztec_code_generator import AztecCode
from io import BytesIO

# -------------------------------------------------
# Page config (CI compliant)
# -------------------------------------------------
st.set_page_config(
    page_title="30%-Code Generator",
    page_icon=None,
    layout="centered"
)

# -------------------------------------------------
# REWE CI – Fonts & Styling
# -------------------------------------------------
st.markdown(
    """
    <style>
    /* REWE Mato – Webfont */
    @font-face {
        font-family: 'REWE Mato';
        src: url('fonts/REWEMatoWebW01/REWEMatoWebW01-Light.woff2') format('woff2');
        font-weight: 300;
        font-style: normal;
    }

    @font-face {
        font-family: 'REWE Mato';
        src: url('fonts/REWEMatoWebW01/REWEMatoWebW01-Regular.woff2') format('woff2');
        font-weight: 400;
        font-style: normal;
    }

    @font-face {
        font-family: 'REWE Mato';
        src: url('fonts/REWEMatoWebW01/REWEMatoWebW01-Medium.woff2') format('woff2');
        font-weight: 500;
        font-style: normal;
    }

    @font-face {
        font-family: 'REWE Mato';
        src: url('fonts/REWEMatoWebW01/REWEMatoWebW01-Bold.woff2') format('woff2');
        font-weight: 700;
        font-style: normal;
    }

    :root {
        --rewe-red: #CC071E;
        --rewe-black: #000000;
        --rewe-white: #FFFFFF;
    }

    html, body, [class*="css"] {
        font-family: 'REWE Mato', Arial, Helvetica, sans-serif;
        color: var(--rewe-black);
        background-color: var(--rewe-white);
    }

    h1 {
        font-weight: 700;
        font-size: 2.2rem;
        margin-bottom: 0.5rem;
    }

    /* Buttons */
    div.stButton > button {
        background-color: var(--rewe-red);
        color: var(--rewe-white);
        border: none;
        border-radius: 0;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        width: 100%;
    }

    div.stButton > button:hover {
        background-color: #A80618;
        color: var(--rewe-white);
    }

    /* Inputs */
    input {
        border-radius: 0 !important;
        border: 1px solid var(--rewe-black) !important;
        font-family: 'REWE Mato', Arial, Helvetica, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# App content
# -------------------------------------------------
st.title("30%-Code Generator")

st.markdown(
    "Generierung eines Aztec-Codes gemäß REWE CI."
)

code_input = st.text_input(
    "Code-Inhalt",
    placeholder="Code eingeben"
)

if st.button("Code generieren"):
    if not code_input:
        st.error("Bitte einen gültigen Code eingeben.")
    else:
        aztec = AztecCode(code_input)
        img = aztec.get_matrix()

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        st.image(buffer)
        st.success("Code erfolgreich generiert.")
