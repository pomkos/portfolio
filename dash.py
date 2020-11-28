import streamlit as st
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
<script src="https://cdn.jsdelivr.net/npm/darkmode-js@1.5.7/lib/darkmode-js.min.js"></script>
<script>
  function addDarkmodeWidget() {
    new Darkmode().showWidget();
  }
  window.addEventListener('load', addDarkmodeWidget);
</script>
"""

st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with st.beta_expander("Welcome to Pete's Perfect Little Projects", expanded=True):
    select_options = ['Covid dash','Protein calculator','Venmo calculator']
    explore = st.radio('',select_options,index=2)

    
if explore == "venmo calculator".capitalize():
    from apps import tip_script
    tip_script.app()

elif explore == "protein calculator".capitalize():
    from apps import brotein
    brotein.app()
    
elif explore == "covid dash".capitalize():
    from apps import covid
    covid.app()