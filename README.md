# End of Life (EOL) Product Checker

This project is a script to check and display products that have an end of life (EOL) date on or after 2023-04-30 using the End of Life API (https://endoflife.date/api).

## Features

- Fetches all products from the API.
- Filters products based on EOL date.
- Displays the product name, release cycle, and EOL date for filtered products.

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

2. The script will fetch all products from the End of Life API and display those with an EOL date on or after 2023-04-30.

## Functions

- `__elo_api_call__(url=URL, product_name="all")`: A private helper function that sends an API request to the specified URL and returns the JSON response.

- `get_all_products() -> list`: Fetches a list of all product names from the End of Life API.

- `get_product(product_name) -> list[dict]`: Fetches a list of release cycles for a given product name, including EOL dates, from the End of Life API.

- `main()`: The main function that iterates through all products, fetches their release cycles, filters them based on EOL date, and displays the filtered results.

## License

This project is licensed under the [MIT License](LICENSE).
