import streamlit as st
from aztec_code_generator import AztecCode
from io import BytesIO

# App Configuration
st.set_page_config(page_title="30%-Etikett Generator", page_icon="🎫")

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
        st.image(byte_im, caption=f"{final_string}")

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
