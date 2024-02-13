import streamlit as st
st.image("logo.svg")
st.title("Streamlit Title")
st.header("Streamlit Heading")
st.subheader("Streamlit Sub-heading")
st.info("Information details of user")
st.warning("warning:Come on time!")
st.write("Employee name")
st.write(range(50))
st.error("Wrong password")
st.success("Congrats you have got A grade")
#demonstrate different levels of Markdown headings, from # for the largest heading to ### for the smallest
st.markdown("Coding")
st.markdown("# Coding")
st.markdown("## Coding")
st.markdown("### Coding")
#displays the "parrot" emoji using Markdown syntax.
st.markdown(":parrot:")
#similar to st.write() but is often used for plain text
st.text("I am text")
st.caption("Caption is here")
#renders a mathematical expression using LaTeX
st.latex(r''' a+b x^2 +c ''')