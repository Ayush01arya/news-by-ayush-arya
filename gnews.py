import streamlit as st
from GoogleNews import GoogleNews
st.sidebar.markdown('<h1>Live News</h1>',unsafe_allow_html=True)
with st.sidebar.expander("About the Application"):
    st.write("Use This application you can get news around all over world .\nThis Application is devloped through python \n@kabir arya ")
st.sidebar.markdown('<h1>@kabir_arya001</h1>',unsafe_allow_html=True)
st.title("Live News")
country=st.text_input("Enter the Country or city Name ??")
if st.button('SEARCH'):
    go = GoogleNews(period='7d')
    go.setlang("hindi")
    go.search(country)

    result = go.result()
    for x in result:
        st.write("-"*40)
        st.markdown(
            f"<h5 style='text-align:justify;color:teal;'><b><u>Title---</u></b><br>{x['title']}</h5>",unsafe_allow_html=True)
        st.markdown(
            f"<h5 style='text-align:justify;color:black;'><b><u>Date and Time---</u></b><br>{x['date']}</h5>", unsafe_allow_html=True)
        st.markdown(
            f"<h5 style='text-align:justify;color:red;'><b><u>Description---</u></b><br>{x['desc']}</h5>", unsafe_allow_html=True)
        st.write(x['link'])
        # #st.markdown(f"'<h5 style='text-align:justify;color:black;'>{x['media']}</h5", unsafe_allow_html=True)

        #st.write(x['title'])
        #st.write(x['date'])
        #st.write(x['desc'])
        #imh=x['img']
        #st.image(imh)
        st.write(x['media'])
    st.markdown("'<h4 style='text-align:center;color:teal;'>This Project is made by Ayush Arya<br>@kabir_arya001</h4>",unsafe_allow_html=True)
