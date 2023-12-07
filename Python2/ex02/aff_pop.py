from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def remove_million(value):
    return value.rstrip('M')

def main():
    """Get data csv and display a graph about population in France and China betzeen 1800 and 2050"""
    try:
        data = load("population_total.csv")
        data_france = data.loc[data['country'] == 'France']
        data_spain = data.loc[data['country'] == 'Spain']
        # print(data_france)
        # print(data_spain)

        years = data.loc[:, '1800':'2050'].columns.tolist()

        france_population = data_france.loc[:, '1800':'2050'].map(remove_million).values.tolist()
        spain_population = data_spain.loc[:, '1800':'2050'].map(remove_million).values.tolist()

        # print(france_population)
        # print(spain_population)

        plt.plot(years, france_population, label='France', linestyle='-')
        plt.plot(years, spain_population, label='Spain', linestyle='-')
        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.show()
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return


if __name__ == "__main__":
    main()