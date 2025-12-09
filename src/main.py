import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn as sk

from visualization_class import CollegeVisualizer
from feature_engineering_class import FeatureEngineer


def main():
    """Main script that executes feature engineering and visualizations."""
    
    # Feature Engineering
    print("Starting feature engineering...")
    engineer = FeatureEngineer('datasets/dataset.csv')
    engineer.engineer_all_features()
    engineer.save_engineered_data()
    print("Feature engineering completed!\n")
    
    # Visualization
    print("Starting visualizations...")
    visualizer = CollegeVisualizer("datasets/engineered_data.csv")
    visualizer.create_all_visualizations()
    visualizer.save_cleaned_data()
    print("Visualizations completed!")


if __name__ == "__main__":
    main()
