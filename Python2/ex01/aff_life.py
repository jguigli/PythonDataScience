from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """Get data csv and display a graph about life expectancy in France"""
    try:
        data = load("life_expectancy_years.csv")
        data_france = data.loc[data['country'] == 'France']

        years = data_france.columns[1:].values.astype('int')
        life_expectancy = data_france.iloc[0, 1:].values

        plt.plot(years, life_expectancy, linestyle='-')
        plt.title('France Life expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life excpectancy')
        plt.show()
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return


if __name__ == "__main__":
    main()
