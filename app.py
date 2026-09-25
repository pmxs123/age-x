import streamlit as st

# 页面标题
st.title("哥斯拉酒吧")
st.subheader("入场资格核验")

# 输入框
wa = st.text_input("请输入你的姓名：")
asb = st.number_input("请输入你的年龄：", min_value=0, max_value=120, value=None)
vp = st.number_input("你的VIP等级是多少？：", min_value=0, max_value=999, value=0)

# 判断逻辑
if st.button("提交核验"):
    if asb is None:
        st.warning("请填写年龄！")
    elif asb >= 18:
        st.success(f"{wa}，已成年允许进入")
        if vp > 50:
            st.info("你的vip已达到50级，享有专属服务😘")
        else:
            st.info("你是普通用户，没有专属服务")
    else:
        st.error(f"{wa}，你是未成年不能进入")
