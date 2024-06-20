### README.md

# Unemployment and Population Data Analysis

This project performs data analysis on unemployment and population data for different countries. It includes functions to read data from CSV files, process it into dictionaries, and compute various statistics such as the highest average unemployment rates and the total unemployment for a given year. Additionally, it includes unit tests to verify the correctness of these functions.

## Files

- `unemployment.py`: Contains the main functions for reading data, creating dictionaries, and computing statistics.
- `unemployment-rate.csv`: CSV file containing unemployment rate data.
- `population.csv`: CSV file containing population data.
- `test_unemployment.py`: Contains unit tests for the functions in `unemployment.py`.

## Functions

- **read_file(filename)**: Reads and returns the lines from a specified file.
- **create_dictionary(lines)**: Creates and returns a nested dictionary from the given lines.
- **year_with_highest_population(country, un_p)**: Finds and returns the year with the highest population for a specified country.
- **highest_ten_avg_unemp(start, end, un_d)**: Returns the 10 countries with the highest average unemployment rate within a specified range of years.
- **lowest_ten_avg_unemp(start, end, un_d)**: Returns the 10 countries with the lowest average unemployment rate within a specified range of years.
- **highest_ten_total_unemp(year, un_d, pop_d)**: Returns the 10 countries with the highest total unemployment for a specified year.

## Unit Tests

- Uses the `unittest` framework to test the functions.
- Tests include:
  - Checking the creation of dictionaries.
  - Finding the year with the highest population.
  - Verifying calculations for the highest and lowest average unemployment rates.
  - Checking the highest total unemployment.

## Usage

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

3. **Run the unit tests**:
   ```bash
   python -m unittest test_unemployment.py
   ```

## Dependencies

- Python 3.x
- `unittest` (included in Python standard library)

## License

Free for Everything and Everyone.

