"""EOL"""
import datetime
import time
import argparse


import requests


URL = "https://endoflife.date/api"


def __elo_api_call__(url=URL, product_name="all"):
    """Return a list of products or a list of cycles for a product"""
    return requests.get(f"{url}/{product_name}.json", timeout=30).json()


def get_all_products() -> list:
    """Return a list of products"""
    return __elo_api_call__()


def get_product(product_name) -> list[dict]:
    """Return a list of cycles for a product"""
    return __elo_api_call__(product_name=product_name)


def arg_parser() -> argparse.Namespace:
    """Return a Namespace object with the date argument"""
    parser = argparse.ArgumentParser(description='EOL')
    parser.add_argument("--date", help="Date", default=datetime.date.today().strftime("%Y-%m-%d"))
    args = parser.parse_args()
    return args


def report(args) -> dict[list[dict]]:
    """Return a dict with the EOL date as key and a list of products and cycles as value"""
    eols = {}
    for product in get_all_products():
        for cycle in get_product(product):
            eol = cycle.get("eol", "")
            if str(eol).startswith(args.date):
                _ = eols.setdefault(eol, [])
                _.append({"product": product, "cycle": cycle["cycle"]})
                time.sleep(1)
    return eols


def report_by_eol(eols: dict[list[dict]]) -> None:
    """Print the report"""
    for eol, products in eols.items():
        print(f"{eol}:")
        for product in products:
            print(f"{product['product']}: Release:{product['cycle']}")
        print(f"{'-' * 20}\n")


def main():
    """Main function"""
    args = arg_parser()
    eols = report(args)

    report_by_eol(eols)


if __name__ == '__main__':
    main()
