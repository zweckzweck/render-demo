import streamlit as st
# import matplotlib.pyplot as plt
st.image("https://untld.in/cdn/shop/files/Untitled_1000_x_1000_px.png?v=1661777427&width=500",width=200)
#st.title("utdsd.in")
st.title("Untitled Clothing")

st.sidebar.header("About us")
# abs=st.sidebar.button("About us")
# if abs:
#     st.sidebar.text("""
#     1.123 State Street Cal
#     2.United States of America""")
#
# Python code
import streamlit as st

# Initialize session state for managing visibility of text in sidebar
if 'show_text_sidebar' not in st.session_state:
    st.session_state.show_text_sidebar = False

# Function to toggle the state of text visibility
def toggle_sidebar_text():
    st.session_state.show_text_sidebar = not st.session_state.show_text_sidebar

# Create a button in the sidebar that toggles text visibility
st.sidebar.button("ESTB.", on_click=toggle_sidebar_text)

# Display text in the sidebar based on the session state
if st.session_state.show_text_sidebar:
    st.sidebar.write("""
    433 State Street 
    Orange County , California
    USA""")

# Optional main area feedback
# st.write("Welcome Untitled Clothing")
st.title("Pants")
col1,col2,col3=st.columns(3)

with col1:
    st.write("Bootcut Denim")
    st.image("https://untld.in/cdn/shop/files/UNTLDOCTOBER20252.0-39.jpg?v=1762376888&width=360",width=200)
    st.button("$9.99",key="btn1")
with col2:
    st.write("Denim Loose Fit")
    st.image("https://untld.in/cdn/shop/files/UNTLDOCTOBER20252.0-145.jpg?v=1762458211&width=360",width= 200)
    st.button("$9.99",key="btn2")
with col3:
    st.write("Denim Cargo")
    st.image("https://untld.in/cdn/shop/files/UNTLDJULY2025-112.jpg?v=1752154152&width=360",width=200)
    st.button("$10.99", key="btn3")

st.title("Shirt")

col1,col2,col3=st.columns(3)

with col1:
    st.write("Archive Shirt (Stripe)")
    st.image("https://untld.in/cdn/shop/files/UNTLDOCTOBER20252.0-220.jpg?v=1762378515&width=360",width=200)
    st.button("$9.99",key="btn4")

with col2:
    st.write("Knock Out Shirt Blue")
    st.image("https://untld.in/cdn/shop/files/UNTLDOCTOBER20252.0-287.jpg?v=1762379405&width=360",width= 200)
    st.button("$9.99",key="btn5")
with col3:
    st.write("Archive Shirt (Checks)")
    st.image("https://untld.in/cdn/shop/files/UNTLDOCTOBER20252.0-246.jpg?v=1762378805&width=360",width=200)
    st.button("$10.99", key="btn6")

st.title("Jackets")

col1,col2,col3=st.columns(3)

with col1:
    st.write("Croc Jacket (Black)")
    st.image("https://untld.in/cdn/shop/files/UNTLD_OCTOBER_2025_-241.jpg?v=1759836171&width=360",width=200)
    st.button("$9.99",key="btn7")

with col2:
    st.write("Drive Jacket (Burgundy)")
    st.image("https://untld.in/cdn/shop/files/UNTLDSEPTEMBER2025-151.jpg?v=1758198365&width=360",width= 200)
    st.button("$9.99",key="btn8")
with col3:
    st.write("Leather Jacket (Brown)")
    st.image("https://untld.in/cdn/shop/files/UNTLD_OCTOBER_2025_-87.jpg?v=1759836659&width=360",width=200)
    st.button("$10.99", key="btn9")

# x=[1,2,3,4]
# y=[5,5,6,7]
# X=plt.bar(x,y)
# st.pyplot(X)

st.html(
    "<p>Since 1950</p>"
)

