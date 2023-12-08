from load_csv import load
import matplotlib.pyplot as plt


def remove_million(value):
    """Converts a population value formatted as a string with
     'M' (million) suffix to a numeric value in millions."""
    return float(value[:-1]) * 1e6


def main():
    """Load population data from a CSV file and plot population
     projections for France and Spain from 1800 to 2050."""
    try:
        data = load("population_total.csv")
        data_france = data.loc[data['country'] == 'France'].iloc[:, 1:]
        data_spain = data.loc[data['country'] == 'Spain'].iloc[:, 1:]

        v_data_france = data_france.values.flatten()
        v_data_spain = data_spain.values.flatten()

        years = data.columns[1:].astype('int')
        france_population = [remove_million(value) for value in v_data_france]
        spain_population = [remove_million(value) for value in v_data_spain]

        plt.plot(years, france_population, label='France', linestyle='-')
        plt.plot(years, spain_population, label='Spain', linestyle='-')

        plt.xticks(range(1800, 2051, 40))
        plt.xlim(1800, 2050)

        ytick_positions = [20000000, 40000000, 60000000]
        plt.yticks(
            ytick_positions,
            [f"{int(value / 1e6)}M" for value in ytick_positions]
            )

        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return


if __name__ == "__main__":
    main()
