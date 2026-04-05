import streamlit as st
import pandas as pd

# កំណត់ការរៀបចំទំព័រ
st.set_page_config(page_title="JMI Portal", page_icon="🏥", layout="wide")

# ប្លុក CSS ដែលមានសុវត្ថិភាព (គ្មានអក្សរ f នៅខាងមុខ ដើម្បីកុំឱ្យរាយប៉ាយ)
style_block = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Kantumruy+Pro:wght@400;700&display=swap');
    html, body, [class*="css"], .stMarkdown { font-family: 'Kantumruy Pro', sans-serif; }
    .stApp { background-color: #f8f9fa; }
    .cert-paper { 
        background: white; border: 10px solid #001f3f; padding: 30px; 
        text-align: center; max-width: 750px; margin: auto; 
        border-radius: 10px; box-shadow: 0 15px 40px rgba(0,0,0,0.2); 
    }
    .student-name { color: #D4AF37; font-size: 45px; font-weight: bold; margin: 20px 0; }
</style>
"""
st.markdown(style_block, unsafe_allow_html=True)

st.title("🏥 JMI Strategic Command Portal")

# ប្រព័ន្ធ Password
pwd = st.sidebar.text_input("Director's Key", type="password")

if pwd == "JMI2026":
    st.sidebar.success("Welcome, Dr. CHAN Sokhoeurn")
    menu = st.sidebar.radio("MENU", ["📊 Dashboard", "📜 Certification"])
    
    if menu == "📊 Dashboard":
        st.write("### ប្រព័ន្ធគ្រប់គ្រងសិស្ស")
        df = pd.DataFrame([{"ឈ្មោះ": "Sokhoeurn Sovannachak", "កម្រិត": "K-G3", "ស្ថានភាព": "Active"}])
        st.table(df)
        
    elif menu == "📜 Certification":
        st.header("Certificate Generator")
        if st.button("🌟 GENERATE"):
            st.balloons()
            st.markdown("""
            <div class="cert-paper">
                <h1 style="color:#001f3f;">CERTIFICATE</h1>
                <p>This is to certify that</p>
                <div class="student-name">Sokhoeurn Sovannachak</div>
                <p>has mastered the Medical Foundation Pathway.</p>
                <hr>
                <p><b>Dr. Chan Sokhoeurn</b><br>Academic Director</p>
            </div>
            """, unsafe_allow_html=True)
else:
    st.info("🔒 សូមបញ្ចូល Password 'JMI2026' ដើម្បីចាប់ផ្ដើម។")
