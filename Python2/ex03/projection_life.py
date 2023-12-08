from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Load data on life expectancy and income per person
     from CSV files for the year 1900, and create a scatter
      plot to visualize the relationship between GDP and life expectancy."""
    try:
        file1 = "life_expectancy_years.csv"
        file2 = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        data_life_expectancy = load(file1)
        data_income_per_person = load(file2)

        dle1900 = data_life_expectancy['1900']
        gdp1900 = data_income_per_person['1900']

        plt.scatter(gdp1900, dle1900)

        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])

        plt.title('1900')
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life expectancy')
        plt.show()
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return


if __name__ == "__main__":
    main()
