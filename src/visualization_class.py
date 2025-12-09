import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


class CollegeVisualizer:
    """A class to handle visualization of college datasets."""
    
    def __init__(self, file_path: str):
        """
        Initialize the CollegeVisualizer with a dataset.
        
        Args:
            file_path (str): Path to the CSV dataset file
        """
        self.df = pd.read_csv(file_path)
        self._preprocess_data()
        self._set_theme()
    
    def _preprocess_data(self) -> None:
        """Preprocess the data by cleaning application volume column."""
        self.df["application_volume"] = (
            self.df["application_volume"].astype(str)
            .str.replace(",", "")
            .astype(int)
        )
    
    def _set_theme(self) -> None:
        """Set the seaborn theme and palette."""
        sns.set_theme(style="whitegrid", palette="muted")
    
    
    def plot_admission_vs_graduation(self) -> None:
        """Create a scatter plot of admission rate vs 6-year graduation rate."""
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x="admission_rate",
            y="graduate_rate_6yr",
            hue="colleges",
            data=self.df,
            s=100
        )
        plt.title("Admission Rate vs 6-Year Graduation Rate")
        plt.tight_layout()
        plt.savefig("figures/admission_vs_graduation.png", dpi=300)
        plt.show()
    
    def plot_pairplot(self) -> None:
        """Create a pairplot of numeric columns."""
        plt.figure(figsize=(10, 10))
        sns.pairplot(self.df.select_dtypes(include='number'), diag_kind="kde")
        plt.suptitle("Pairplot of College Metrics", y=1.001)
        plt.tight_layout()
        plt.savefig(os.path.join("figures", "pairplot_college_metrics.png"), dpi=300)
        plt.show()
    
    def plot_correlation_heatmap(self) -> None:
        """Create a correlation heatmap of numeric columns."""
        plt.figure(figsize=(8, 5))
        sns.heatmap(
            self.df.select_dtypes(include='number').corr(),
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )
        plt.title("Correlation Heatmap of College Metrics")
        plt.tight_layout()
        plt.savefig("figures/correlation_heatmap.png", dpi=300)
        plt.show()
    
    def plot_application_vs_admission(self) -> None:
        """Create a scatter plot of application volume vs admission rate."""
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x="application_volume",
            y="admission_rate",
            hue="colleges",
            data=self.df,
            s=120
        )
        plt.title("Application Volume vs Admission Rate")
        plt.tight_layout()
        plt.savefig("figures/application_vs_admission.png", dpi=300)
        plt.show()
    
    def plot_graduation_rates_comparison(self) -> None:
        """Create a bar plot comparing 4-year vs 6-year graduation rates."""
        plt.figure(figsize=(10, 6))
        df_melt = self.df.melt(
            id_vars="colleges",
            value_vars=["graduate_rate_4yr", "graduate_rate_6yr"],
            var_name="Graduation Type",
            value_name="Rate"
        )
        sns.barplot(x="Rate", y="colleges", hue="Graduation Type", data=df_melt)
        plt.title("4-Year vs 6-Year Graduation Rates by College")
        plt.tight_layout()
        plt.savefig("figures/graduation_rates_comparison.png", dpi=300)
        plt.show()
    
    def plot_admission_rate_vs_application_volume(self) -> None:
        """Create a dual-axis plot of admission rate vs application volume by college."""
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        ax1.set_xlabel("College")
        ax1.set_ylabel("Admission Rate (%)", color="tab:blue")
        ax1.bar(self.df["colleges"], self.df["admission_rate"], color="tab:blue", alpha=0.7, label="Admission Rate")
        ax1.tick_params(axis="y", labelcolor="tab:blue")
        ax1.set_xticklabels(self.df["colleges"], rotation=45, ha="right")
        
        ax2 = ax1.twinx()
        ax2.set_ylabel("Application Volume", color="tab:orange")
        ax2.plot(self.df["colleges"], self.df["application_volume"], color="tab:orange", marker="o", linewidth=2, label="Application Volume")
        ax2.tick_params(axis="y", labelcolor="tab:orange")
        
        plt.title("Admission Rate vs Application Volume by College")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/admission_rate_vs_application_volume.png", dpi=300)
        plt.show()
    
    def plot_cohort_size_vs_4yr_graduation(self) -> None:
        """Create a scatter plot of cohort size vs 4-year graduation rate."""
        if "cohort_size" not in self.df.columns:
            self.df["cohort_size"] = self.df["application_volume"] * self.df["admission_rate"]
        
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            x="cohort_size",
            y="graduate_rate_4yr",
            hue="colleges",
            data=self.df,
            s=150
        )
        plt.title("Cohort Size vs 4-Year Graduation Rate")
        plt.xlabel("Cohort Size")
        plt.ylabel("4-Year Graduation Rate (%)")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/cohort_size_vs_4yr_graduation.png", dpi=300)
        plt.show()
    
    def plot_cohort_size_vs_6yr_graduation(self) -> None:
        """Create a scatter plot of cohort size vs 6-year graduation rate."""
        if "cohort_size" not in self.df.columns:
            self.df["cohort_size"] = self.df["application_volume"] * self.df["admission_rate"]
        
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            x="cohort_size",
            y="graduate_rate_6yr",
            hue="colleges",
            data=self.df,
            s=150
        )
        plt.title("Cohort Size vs 6-Year Graduation Rate")
        plt.xlabel("Cohort Size")
        plt.ylabel("6-Year Graduation Rate (%)")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/cohort_size_vs_6yr_graduation.png", dpi=300)
        plt.show()
    
    def plot_selectivity_score_vs_6yr_graduation(self) -> None:
        """Create a scatter plot of selectivity score vs 6-year graduation rate."""
        if "selectivity_score" not in self.df.columns:
            self.df["selectivity_score"] = 1 / self.df["admission_rate"]
        
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x="selectivity_score",
            y="graduate_rate_6yr",
            hue="colleges",
            data=self.df,
            s=100
        )
        plt.title("Selectivity Score vs 6-Year Graduation Rate")
        plt.xlabel("Selectivity Score")
        plt.ylabel("6-Year Graduation Rate (%)")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/selectivity_score_vs_6yr_graduation.png", dpi=300)
        plt.show()
    
    def plot_admission_rate_vs_6yr_graduation(self) -> None:
        """Create a scatter plot of admission rate vs 6-year graduation rate."""
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x="admission_rate",
            y="graduate_rate_6yr",
            hue="colleges",
            data=self.df,
            s=100
        )
        plt.title("Admission Rate vs 6-Year Graduation Rate")
        plt.xlabel("Admission Rate (%)")
        plt.ylabel("6-Year Graduation Rate (%)")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/admission_rate_vs_6yr_graduation.png", dpi=300)
        plt.show()
    
    def plot_tuition_vs_6yr_graduation(self) -> None:
        """Create a scatter plot of tuition rate vs 6-year graduation rate."""
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x="tuition_rate",
            y="graduate_rate_6yr",
            hue="colleges",
            data=self.df,
            s=100
        )
        plt.title("Tuition Rate vs 6-Year Graduation Rate")
        plt.xlabel("Tuition Rate")
        plt.ylabel("6-Year Graduation Rate (%)")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/tuition_vs_6yr_graduation.png", dpi=300)
        plt.show()
    
    def create_all_visualizations(self) -> None:
        """Execute all visualization steps in sequence."""
        self.plot_admission_vs_graduation()
        self.plot_pairplot()
        self.plot_correlation_heatmap()
        self.plot_application_vs_admission()
        self.plot_graduation_rates_comparison()
        self.plot_admission_rate_vs_application_volume()
        self.plot_cohort_size_vs_4yr_graduation()
        self.plot_cohort_size_vs_6yr_graduation()
        self.plot_selectivity_score_vs_6yr_graduation()
        self.plot_admission_rate_vs_6yr_graduation()
        self.plot_tuition_vs_6yr_graduation()
    
    def save_cleaned_data(self, output_path: str = "datasets/college_data_cleaned.csv") -> None:
        """
        Save the cleaned dataset to a CSV file.
        
        Args:
            output_path (str): Path where the cleaned dataset should be saved
        """
        self.df.to_csv(output_path, index=False)
    
    def get_dataframe(self) -> pd.DataFrame:
        """Return the current dataframe."""
        return self.df


if __name__ == "__main__":
    # Example usage
    visualizer = CollegeVisualizer("datasets/college_data.csv")
    visualizer.create_all_visualizations()
    visualizer.save_cleaned_data()
