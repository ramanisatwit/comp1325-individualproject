import pandas as pd
import numpy as np


class FeatureEngineer:
    """A class to handle feature engineering for college datasets."""
    
    def __init__(self, dataset_path: str):
        """
        Initialize the FeatureEngineer with a dataset.
        
        Args:
            dataset_path (str): Path to the CSV dataset file
        """
        self.df = pd.read_csv(dataset_path)
    
    def create_average_graduation_rate(self) -> None:
        """Create average graduation rate feature from 4-year and 6-year rates."""
        self.df["avg_graduation_rate"] = (
            self.df["graduate_rate_4yr"] + self.df["graduate_rate_6yr"]
        ) / 2
    
    def create_graduation_rate_improvement(self) -> None:
        """Create graduation rate improvement feature as difference between 6-year and 4-year rates."""
        self.df["graduation_rate_improvement"] = (
            self.df["graduate_rate_6yr"] - self.df["graduate_rate_4yr"]
        )
    
    def create_selectivity_score(self) -> None:
        """Create selectivity score based on reciprocal of admission rate."""
        self.df["selectivity_score"] = 1 / self.df["admission_rate"]
    
    def create_cohort_size(self) -> None:
        """Create cohort size feature (application_volume * admission_rate)."""
        self.df["cohort_size"] = self.df["application_volume"] * self.df["admission_rate"]
    
    def round_features(self) -> None:
        """Round engineered features to specified decimal places."""
        self.df['avg_graduation_rate'] = self.df['avg_graduation_rate'].round(3)
        self.df['graduation_rate_improvement'] = self.df['graduation_rate_improvement'].round(3)
        self.df['selectivity_score'] = self.df['selectivity_score'].round(2)
        self.df['cohort_size'] = self.df['cohort_size'].round(2)
    
    def engineer_all_features(self) -> None:
        """Execute all feature engineering steps in sequence."""
        self.create_average_graduation_rate()
        self.create_graduation_rate_improvement()
        self.create_selectivity_score()
        self.create_cohort_size()
        self.round_features()
    
    def save_engineered_data(self, output_path: str = 'datasets/engineered_data.csv') -> None:
        """
        Save the engineered dataset to a CSV file.
        
        Args:
            output_path (str): Path where the engineered dataset should be saved
        """
        self.df.to_csv(output_path, index=False)
        print("Engineered dataset saved")
    
    def get_dataframe(self) -> pd.DataFrame:
        """Return the current dataframe."""
        return self.df
