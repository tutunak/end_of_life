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


def main():
    args = arg_parser()
    for product in get_all_products():
        for cycle in get_product(product):
            eol = cycle.get("eol", "")
            if str(eol).startswith(args.date):
                print(f"{product} : Release: {cycle['cycle']} : {eol}")
        time.sleep(1)


if __name__ == '__main__':
    main()
