import streamlit as st
from aztec_code_generator import AztecCode
from io import BytesIO

# App Configuration
st.set_page_config(page_title="30%-Code Generator", page_icon="🎫", layout="centered")

# Mobile / responsive improvements: make images and buttons scale nicely
st.markdown(
        """
        <style>
        /* Ensure generated images scale to the screen */
        img { max-width: 100% !important; height: auto !important; }

        /* Larger touch targets for buttons */
        .stButton>button, .stDownloadButton>button {
            padding: 12px 18px !important;
            font-size: 1rem !important;
            border-radius: 8px !important;
        }

        /* Make input larger and easier to tap on small screens */
        @media (max-width: 480px) {
            input[type="text"] {
                font-size: 1.1rem !important;
                padding: 10px 12px !important;
            }
            .stDownloadButton, .stButton {
                width: 100% !important;
            }
            .css-1d391kg, .main, .block-container { padding-left: 10px !important; padding-right: 10px !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
)

st.title("30%-Code Erstellen")
st.write("EAN des zu reduzierenden Artikels eingeben um ein 30%-Code zu erstellen.")

# User Input
user_input = st.text_input("", placeholder="EAN")

if user_input:
    # 1. Logic: Prepend 22701 and Append 03000
    prefix = "22701"
    suffix = "03000"
    final_string = f"{prefix}{user_input}{suffix}"
    


    try:
        # 2. Generate the Aztec Code
        # This library creates an AztecCode object
        aztec = AztecCode(final_string)
        
        # 3. Convert the code into an image (PIL object)
        # size=10 makes the modules (dots) larger for better scanning
        img = aztec.image(module_size=10)
        
        # 4. Prepare for Streamlit and Download
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Display the result
        # Use an explicit width (CSS will enforce max-width for smaller screens)
        st.image(byte_im, caption=f"{final_string}", width=360)

        # Download Button
        st.download_button(
            label="Code herunterladen",
            data=byte_im,
            file_name=f"aztec_{user_input}.png",
            mime="image/png"
        )
        
    except Exception as e:
        st.error(f"Ein Fehler ist aufgetreten: {e}")
else:
    st.warning("Bitte EAN eingeben.")
