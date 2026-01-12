import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

#Functions
def calculate_single_shannon(counts):
    """Calculates Shannon Index for a single array of counts"""
    total = np.sum(counts)
    proportions = counts / total
    
    # Filter for non-zero proportions to avoid log(0) error
    proportions_nonzero = proportions[proportions > 0]
    
    # Formula: -sum(p * ln(p))
    return -np.sum(proportions_nonzero * np.log(proportions_nonzero))

def calculate_single_simpson(counts):
    """Calculates Simpson Index (1-D) for a single array of counts"""
    total = np.sum(counts)
    proportions = counts / total
    
    # Formula: 1 - sum(p^2)
    return 1 - np.sum(proportions**2)

#Get Values---------------------------------------------------------------
def get_values(freshmen_processed, transfer_processed):
    print("Test Optional-------------------------------------------")
    freshmen_val_2020 = freshmen_processed['2020'].values
    freshmen_val_2021 = freshmen_processed['2021'].values
    
    transfer_val_2020 = transfer_processed['2020'].values
    transfer_val_2021 = transfer_processed['2021'].values
    
    #Simpson Index
    freshmen_s_2020 = calculate_single_simpson(freshmen_val_2020)
    freshmen_s_2021 = calculate_single_simpson(freshmen_val_2021)
    
    freshmen_s_change = freshmen_s_2021 - freshmen_s_2020
    print(f"Freshmen Simpson Index 2020 (1-D): {freshmen_s_2020:.5f}")
    print(f"Freshmen Simpson Index 2021 (1-D): {freshmen_s_2021:.5f}")
    print(f"Change in (1-D) for Freshmen: {freshmen_s_change:.5f}\n")
    
    transfer_s_2020 = calculate_single_simpson(transfer_val_2020)
    transfer_s_2021 = calculate_single_simpson(transfer_val_2021)
    
    transfer_s_change = transfer_s_2021 - transfer_s_2020
    print(f"Transfer Simpson Index 2020 (1-D): {transfer_s_2020:.5f}")
    print(f"Transfer Simpson Index 2021 (1-D): {transfer_s_2021:.5f}")
    print(f"Change in (1-D) for Transfers: {transfer_s_change:.5f}")
    
    print("-----------------------------------------------")
    
    #Shannon Index
    freshmen_h_2020 = calculate_single_shannon(freshmen_val_2020)
    freshmen_h_2021 = calculate_single_shannon(freshmen_val_2021)
    
    freshmen_h_change = freshmen_h_2021 - freshmen_h_2020
    print(f"Freshmen Shannon Index 2020 (H'): {freshmen_h_2020:.5f}")
    print(f"Freshmen Shannon Index 2021 (H'): {freshmen_h_2021:.5f}")
    print(f"Change in H' for Freshmen: {freshmen_h_change:.5f}\n")
    
    transfer_h_2020 = calculate_single_shannon(transfer_val_2020)
    transfer_h_2021 = calculate_single_shannon(transfer_val_2021)
    
    transfer_h_change = transfer_h_2021 - transfer_h_2020
    print(f"Transfer Shannon Index 2020 (H'): {transfer_h_2020:.5f}")
    print(f"Transfer Shannon Index 2021 (H'): {transfer_h_2021:.5f}")
    print(f"Change in H' for Transfers: {transfer_h_change:.5f}\n")
    
    print("Test Blind----------------------------------------------")
    #Simpson
    freshmen_val_2023 = freshmen_processed['2023'].values
    transfer_val_2023 = transfer_processed['2023'].values
    
    freshmen_s_2023 = calculate_single_simpson(freshmen_val_2023)
    
    freshmen_s_change = freshmen_s_2023 - freshmen_s_2020
    print(f"Freshmen Simpson Index 2020 (1-D): {freshmen_s_2020:.5f}")
    print(f"Freshmen Simpson Index 2023 (1-D): {freshmen_s_2023:.5f}")
    print(f"Change in (1-D) for Freshmen: {freshmen_s_change:.5f}\n")
    
    transfer_s_2023 = calculate_single_simpson(transfer_val_2023)
    
    transfer_s_change = transfer_s_2023 - transfer_s_2020
    print(f"Transfer Simpson Index 2020 (1-D): {transfer_s_2020:.5f}")
    print(f"Transfer Simpson Index 2023 (1-D): {transfer_s_2023:.5f}")
    print(f"Change in (1-D) for Transfers: {transfer_s_change:.5f}")
    
    print("-----------------------------------------------")
    
    #Shannon Index
    
    freshmen_h_2023 = calculate_single_shannon(freshmen_val_2023)
    
    freshmen_h_change = freshmen_h_2023 - freshmen_h_2020
    print(f"Freshmen Shannon Index 2020 (H'): {freshmen_h_2020:.5f}")
    print(f"Freshmen Shannon Index 2023 (H'): {freshmen_h_2023:.5f}")
    print(f"Change in H' for Freshmen: {freshmen_h_change:.5f}\n")
    
    
    transfer_h_2023 = calculate_single_shannon(transfer_val_2023)
    
    transfer_h_change = transfer_h_2023 - transfer_h_2020
    print(f"Transfer Shannon Index 2020 (H'): {transfer_h_2020:.5f}")
    print(f"Transfer Shannon Index 2023 (H'): {transfer_h_2023:.5f}")
    print(f"Change in H' for Transfers: {transfer_h_change:.5f}\n")