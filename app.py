import streamlit as st
# from streamlit_modal import Modal
# from streamlit_extras.buy_me_a_coffee import button
st.html(
    '''
    <style>
    .stMainBlockContainer{
                background-color:#32322F;
        }
    .stMain{
        background-color:#2C2B28;
    }
    .stAppHeader{
        background-color:#29253E;
    }
    h1{
    color:Gray;
    }
    hr {
        border-color: green;
    }
    p,li{
        color:;
    }
    h3,h2{
        color:#D97757;
    }
    </style>
    '''
)

Home=st.Page(
    page="Pages/Welcome.py",
    title="Home",
    icon="🏠"
)
baymax=st.Page(
    page="Pages/Baymax.py",
    title="Baymax A.I.",
    icon="🤖"
)
Symptom_Checker=st.Page(
    page="Pages/Symptom Checker.py",
    title="Symptom checker",
    icon="⁉️"
)
History=st.Page(
    page="Pages/History.py",
    title="History",
    icon="🕒"
)
About=st.Page(
    page="Pages/About.py",
    title="About",
    icon="🧠"
)
Socials=st.Page(
    page="Pages/Socials.py",
    title="Socials",
    icon="🌐"
)
# modal = Modal(key="my_modal", title="Care for a Sip!!☕")

# # Button to trigger the modal
# if st.sidebar.button("Buy me a coffee",icon="☕",):
#     modal.open()

# # Modal content
# if modal.is_open():
#     with modal.container():
#         st.image("https://iili.io/20Mw9lj.jpg",width=450)
st.sidebar.link_button("Buy me a coffee","https://buymeacoffee.com/sandesh13fr",icon="☕",)
pages=st.navigation([Home,baymax,Symptom_Checker,History,About,Socials])
pages.run()