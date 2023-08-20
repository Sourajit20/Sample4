import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Get the mean, standard deviation, and number of samples from the user
    mean = st.slider("Mean", 0, 100, 50)
    std = st.slider("Standard deviation", 0, 10, 5)
    n_samples = st.slider("Number of samples", 10, 1000, 100)

    # Generate the normal distribution
    data = np.random.normal(mean, std, n_samples)

    # Plot the histogram of the data
    fig, ax = plt.subplots()
    ax.hist(data)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of normal distribution")
    st.pyplot(fig)

    # Download as CSV
    if st.button("Download Data as CSV"):
        df = pd.DataFrame(data, columns=["Value"])
        csv = df.to_csv(index=False)
        st.download_button("Download CSV", data=csv, file_name="generated_data.csv")

if _name_ == "_main_":
    main()
