from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """Get data csv and display a graph about life population in France and Belgium"""
    try:
        data = load("life_expectancy_years.csv")
        data_france = data.loc[data['country'] == 'France']
        print()

        years = data_france.columns[1:].values.astype('int')
        life_expectancy = data_france.iloc[0, 1:].values

        # plt.plot(years, life_expectancy, linestyle='-')
        # plt.title('France Life expectancy Projections')
        # plt.xlabel('Years')
        # plt.ylabel('Life excpectancy')
        # plt.show()
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return


if __name__ == "__main__":
    main()