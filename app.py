import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import itertools

sun_data = pd.read_csv('data/sun_data.csv')
color_values = [np.arange(1, 26, 2).tolist(), np.arange(2, 26, 2).tolist()]
color_values = list(itertools.chain(*color_values))

fig = go.Figure(go.Sunburst(
	ids=sun_data['ids'],
    labels=sun_data['labels'] + '<br>' + sun_data['key_mode'].astype(str),
    parents=sun_data['parents'], 
	text=sun_data['songs'],
	hoverinfo='label+text', 
    marker=dict(
        colors=color_values,  # Numerical array for coloring
        colorscale='Turbo'      # Choose a predefined colorscale
    )
))

fig.update_layout(margin = dict(t=0, l=0, r=0, b=0), 
                  font=dict(
        family="Arial, sans-serif",
        size=16
       
    ))
st.plotly_chart(fig, use_container_width=True)
