# End of Life (EOL) Product Checker

This project is a script to check and display products that have an end of life (EOL) date on or after a specified date using the End of Life API (https://endoflife.date/api). By default, it checks for EOL dates matching the current date.

## Features

- Fetches all products from the API.
- Filters products based on EOL date.
- Displays the product name, release cycle, and EOL date for filtered products.
- Allows users to specify a custom date for filtering.

## Dependencies

- Python 3.8 or higher
- requests

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Run the script:

```
python eol_product_checker.py
```

By default, the script will fetch all products from the End of Life API and display those with an EOL date matching the current date.

2. To specify a custom date for filtering, use the `--date` argument:

```
python eol_product_checker.py --date "2023-04-30"
```

## Functions

- `__elo_api_call__(url=URL, product_name="all")`: A private helper function that sends an API request to the specified URL and returns the JSON response.

- `get_all_products() -> list`: Fetches a list of all product names from the End of Life API.

- `get_product(product_name) -> list[dict]`: Fetches a list of release cycles for a given product name, including EOL dates, from the End of Life API.

- `arg_parser() -> argparse.Namespace`: Parses command-line arguments and returns an argparse.Namespace object containing the parsed arguments.

- `main()`: The main function that iterates through all products, fetches their release cycles, filters them based on EOL date, and displays the filtered results.

## License

This project is licensed under the [MIT License](LICENSE).
