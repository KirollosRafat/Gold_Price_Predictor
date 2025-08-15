import numpy as np
import pickle as pk
import streamlit as st
import os

def main():
    st.title("Gold Price Prediction")

    # Take the data from the user
    SPX = st.text_input("Gold Ratio (SPX)")
    GLD = st.text_input("Gold Share")
    USO = st.text_input("USO")
    SLV = st.text_input("Silver Share")

    Price = None

    if st.button("Price Prediction"):
        try:
            # Convert inputs to float
            inputs = [float(SPX), float(GLD), float(USO), float(SLV)]
            Price = predictions(np.array([inputs], dtype=np.float32))
            st.success(f"Predicted Gold Price: {Price[0]:.2f}")
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

def predictions(data):
    file_path = os.path.join(os.path.dirname(__file__), 'traine_model.sav')
    trained_model = pk.load(open(file_path, 'rb'))
    price_outcome = trained_model.predict(data)
    return price_outcome

if __name__ == "__main__":
    main()
