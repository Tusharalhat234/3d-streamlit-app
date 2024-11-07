import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Set up the Streamlit page
st.title("3D Interactive Scatter Plot")
st.write("Explore a 3D Scatter Plot with adjustable parameters!")

# User inputs for controlling the 3D plot
num_points = st.slider("Number of Points", min_value=10, max_value=500, value=100)
color_option = st.selectbox("Color Scheme", ["Viridis", "Plasma", "Cividis", "Inferno", "Magma"])

# Generate random 3D data based on user input
x = np.random.randn(num_points)
y = np.random.randn(num_points)
z = np.random.randn(num_points)
size = np.random.rand(num_points) * 20  # Random point sizes

# Create a 3D scatter plot with Plotly
fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=size,
        color=z,  # Color by z-axis values
        colorscale=color_option,  # Apply selected color scheme
        opacity=0.8
    )
)])

# Set plot layout
fig.update_layout(
    scene=dict(
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        zaxis_title="Z Axis"
    ),
    margin=dict(l=0, r=0, b=0, t=0)
)

# Display the 3D plot in Streamlit
st.plotly_chart(fig)

# Optional user interaction (Exporting data)
if st.button("Export Data"):
    # Convert data to CSV format
    import pandas as pd
    df = pd.DataFrame({'x': x, 'y': y, 'z': z, 'size': size})
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download 3D Data",
        data=csv,
        file_name="3d_data.csv",
        mime="text/csv"
    )

st.write("Adjust the parameters to see the 3D plot update in real-time!")
