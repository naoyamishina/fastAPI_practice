import streamlit as st

st.title("App title")

st.markdown("# 見出し1")
st.markdown("## 見出し2")
st.markdown("### 見出し3")

st.markdown("""
    # 見出し1
    ## 見出し2
    ### 見出し3
""")

st.code('''
    def hello():
        print("Hello, Streamlit!")
''')

st.write('st.write, World!')
"Demo, magic"
