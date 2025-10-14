import streamlit as st
import plotly.graph_objects as go
import pandas as pd

sun_data = pd.read_csv('data/sun_data.csv')

fig = go.Figure(go.Sunburst(
	ids=sun_data['ids'],
    labels=sun_data['labels'] + '<br>' + sun_data['key_mode'].astype(str),
    parents=sun_data['parents'], 
	text=sun_data['songs'],
	hoverinfo='label+text'
))

fig.update_layout(margin = dict(t=0, l=0, r=0, b=0), 
                  font=dict(
        family="Arial, sans-serif",
        size=16
       
    ))
st.plotly_chart(fig, use_container_width=True)
