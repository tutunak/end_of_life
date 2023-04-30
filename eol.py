import datetime
import time
import argparse


import requests


URL = "https://endoflife.date/api"


def __elo_api_call__(url=URL, product_name="all"):
    return requests.get(f"{url}/{product_name}.json").json()


def get_all_products() -> list:
    return __elo_api_call__()


def get_product(product_name) -> list[dict]:
    return __elo_api_call__(product_name=product_name)


def arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='EOL')
    parser.add_argument("--date", help="Date", default=datetime.date.today().strftime("%Y-%m-%d"))
    args = parser.parse_args()
    return args


def report(args) -> dict[list[dict]]:
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
    for eol, products in eols.items():
        print(f"{eol}:")
        for product in products:
            print(f"{product['product']}: Release:{product['cycle']}")
        print(f"{'-' * 20}\n")


def main():
    args = arg_parser()
    eols = report(args)

    report_by_eol(eols)


if __name__ == '__main__':
    main()
