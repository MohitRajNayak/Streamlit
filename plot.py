import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
st.set_option('deprecation.showPyplotGlobalUse', False) # to disable warnings

df = pd.DataFrame(
    np.random.randn(100,3),
    columns=['col1','col2','col3']
)

st.header("Charts")

st.subheader("Line Chart")
st.line_chart(df)

st.subheader("Area Chart")
st.area_chart(df)

st.subheader("Bar Chart")
st.bar_chart(df)

st.subheader("Scatter plot")
plt.scatter(df['col1'],df['col2'])
plt.title("For Title")
plt.xlabel("For X-axis Label")
plt.ylabel("For Y-axis Label")
st.pyplot()

st.subheader("Scatter plot in altair pkg")
c = alt.Chart(df).mark_square().encode(
    x='col1',y='col2',size='col3',color='col3',tooltip=['col1','col2','col3']
)
st.altair_chart(c)

st.subheader("Scatter plot in altair pkg with container_width = True")
c = alt.Chart(df).mark_square().encode(
    x='col1',y='col2',size='col3',color='col3',tooltip=['col1','col2','col3']
)
st.altair_chart(c,use_container_width=True)

st.subheader("Flow Chart")
st.graphviz_chart("""
digraph{
                  speech -> input
                  input -> trigger
                  trigger -> speech
                  trigger -> concept
                  concept -> video
                  video -> gif

}
""")

st.subheader("Plotly chart")
df1 = px.data.gapminder()

fig = px.scatter(
    df1.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

st.plotly_chart(fig,theme="streamlit", use_container_width=True)

df = pd.DataFrame({
    "col1": np.random.randn(1000) / 50 + 37.76,
    "col2": np.random.randn(1000) / 50 + -122.4,
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),
})

st.subheader("Map plot")
st.map(df,
    latitude='col1',
    longitude='col2',
    size='col3',
    color='col4')

st.subheader("Display Media File")
st.image("data\marvel.jpg")
st.audio("data\song.wav")
st.video("https://www.youtube.com/watch?v=jq0lKFb-P8k&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5&index=4")