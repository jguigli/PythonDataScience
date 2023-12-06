from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """Get data csv and display a graph about population in France and China betzeen 1800 and 2050"""
    try:
        data = load("population_total.csv")
        # data_france_china = data.loc[data['country'].isin(['France', 'China'])]
        # print(data_france_china)

        # years = data_france_china[(data_france_china.columns.astype(int) <= 2050)]
        # population = data_france_china.iloc[0:1, 1:].values

        # plt.plot(years, population, linestyle='-')
        # plt.title('Population Projections')
        # plt.xlabel('Year')
        # plt.ylabel('Population')
        # plt.show()
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return


if __name__ == "__main__":
    main()