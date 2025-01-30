# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:48:22 2025

@author: resva
"""

import numpy as np
from scipy.stats import norm
import streamlit as st


def black_scholes_price(S, X, T, r, sigma):
    """
    Calculate both call and put option prices using the Black-Scholes formula.

    Parameters:
        S (float): Current stock price
        X (float): Strike price
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate (as a decimal)
        sigma (float): Volatility of the stock (as a decimal)

    Returns:
        dict: Contains the call and put option prices
    """
    d1 = (np.log(S / X) + (r + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    # Calculate call and put prices
    call_price = S * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)
    put_price = X * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return {"call": call_price, "put": put_price}

"""

Now add GUI through streamlit library

"""

def main():
    st.title("Black-Scholes Option Pricing Model")
    st.write("Adjust the input parameters to see the call and put option prices.")

    # Input sliders and fields for Black-Scholes parameters
    S = st.number_input("Current Stock Price (S)", min_value=0.01, value=100.0, step=0.1)
    X = st.number_input("Strike Price (X)", min_value=0.01, value=100.0, step=0.1)
    T = st.slider("Time to Maturity (T, in years)", min_value=0.01, max_value=10.0, value=1.0, step=0.1)
    r = st.slider("Risk-Free Interest Rate (r)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
    sigma = st.slider("Volatility (σ)", min_value=0.0, max_value=1.0, value=0.2, step=0.01)

    # Calculate the option prices
    prices = black_scholes_price(S, X, T, r, sigma)

    # Display results
    st.write("### Option Prices")
    st.write(f"**Call Option Price:** {prices['call']:.2f}")
    st.write(f"**Put Option Price:** {prices['put']:.2f}")

if __name__ == "__main__":
    main()

