import streamlit as st

st.title("年龄检测器")
age = st.number_input("请输入你的年龄", min_value=0, max_value=120, value=18)

if st.button("判断是否成年"):
    if age >= 18:
        st.success("✅ 你已经成年啦！")
    else:
        st.warning("❌ 你还未成年")
