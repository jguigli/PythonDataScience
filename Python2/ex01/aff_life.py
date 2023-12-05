from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """Get data csv and display a graph about it"""
    try:
        data = load("life_expectancy_years.csv")
        # Code pour recuperer les informations France
        data_france = pd.series("")

        ax = df.plot(kind='bar', x='Year', y='Life expectancy', legend=True)
        ax.set_ylabel("France Life expectancy Projections")
        plt.show()
    except Exception as e:
        print(f"Error loading the image: {str(e)}")
        return


if __name__ == "__main__":
    main()
