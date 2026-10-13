import streamlit as st

st.title("🎨 Dynamic Color Inspector")
st.write("Pick a color and explore its digital properties!")

color = st.color_picker("Pick a color for your next app theme:", "#00f0ff")
st.write("The current HEX code of your chosen color is:", color)

st.markdown(
    f"""
    <div style="background-color: {color}; padding: 30px; border-radius: 10px; text-align: center; color: white; font-weight: bold;">
        This is how your selected color looks in real-time!
    </div>
    """,
    unsafe_allow_html=True
)
