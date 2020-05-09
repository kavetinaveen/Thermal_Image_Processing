import streamlit as st
import flir_image_extractor
import plotly.express as px

st.title("Extract Temperature in Celsius")
demo = st.sidebar.selectbox('Select Demo', ['Demo 1', 'Demo 2', 'Demo 3'])
fir = flir_image_extractor.FlirImageExtractor()

if demo == 'Demo 1':
	fir.process_image('examples/ax8.jpg')
elif demo == 'Demo 2':
	fir.process_image('examples/flir_example.jpg')
elif demo == 'Demo 3':
	fir.process_image('examples/zenmuse_xtr.jpg')

fig = px.imshow(fir.get_thermal_np())
fig.update_layout(width=800,height=600)
st.plotly_chart(fig)
st.markdown('**Note:** Hover mouse on picture, `z` is Temperature in Celsius')
