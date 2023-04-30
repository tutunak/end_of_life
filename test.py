"""Unit tests for eol.py"""
import unittest
from unittest.mock import patch
import requests
import argparse
from eol import __elo_api_call__, get_all_products, get_product, arg_parser, report, report_by_eol


class TestEloApiCall(unittest.TestCase):
    """Unit tests for __elo_api_call__"""
    @patch("requests.get")
    def test_elo_api_call(self, mock_get):
        url = "https://api.example.com"
        product_name = "test_product"
        __elo_api_call__(url, product_name)
        mock_get.assert_called_once_with(f"{url}/{product_name}.json")


class TestGetAllProducts(unittest.TestCase):
    """Unit tests for get_all_products"""
    @patch("eol.__elo_api_call__")
    def test_get_all_products(self, mock_elo_api_call):
        get_all_products()
        mock_elo_api_call.assert_called_once_with()


class TestGetProduct(unittest.TestCase):
    """Unit tests for get_product"""
    @patch("eol.__elo_api_call__")
    def test_get_product(self, mock_elo_api_call):
        product_name = "test_product"
        get_product(product_name)
        mock_elo_api_call.assert_called_once_with(product_name=product_name)


class TestArgParser(unittest.TestCase):
    """Unit tests for arg_parser"""
    def test_arg_parser(self):
        with patch("argparse.ArgumentParser.parse_args") as mock_parse_args:
            mock_parse_args.return_value = argparse.Namespace(date="2023-04-30")
            args = arg_parser()
            self.assertEqual(args.date, "2023-04-30")


class TestReport(unittest.TestCase):
    """Unit tests for report"""
    @patch("eol.get_all_products")
    @patch("eol.get_product")
    def test_report(self, mock_get_product, mock_get_all_products):
        mock_get_all_products.return_value = ["product1", "product2"]
        mock_get_product.side_effect = [
            [
                {"cycle": "1.0", "eol": "2023-04-30"},
                {"cycle": "1.1", "eol": "2023-05-30"},
            ],
            [
                {"cycle": "2.0", "eol": "2023-06-30"},
                {"cycle": "2.1", "eol": "2023-04-30"},
            ],
        ]
        args = argparse.Namespace(date="2023-04-30")
        eols = report(args)
        expected_eols = {
            "2023-04-30": [
                {"product": "product1", "cycle": "1.0"},
                {"product": "product2", "cycle": "2.1"},
            ],
        }
        self.assertEqual(eols, expected_eols)


class TestReportByEol(unittest.TestCase):
    """Unit tests for report_by_eol"""
    def test_report_by_eol(self):
        eols = {
            "2023-04-30": [
                {"product": "product1", "cycle": "1.0"},
                {"product": "product2", "cycle": "2.1"},
            ],
        }
        with patch("builtins.print") as mock_print:
            report_by_eol(eols)
            mock_print.assert_any_call("2023-04-30:")
            mock_print.assert_any_call("product1: Release:1.0")
            mock_print.assert_any_call("product2: Release:2.1")
            mock_print.assert_any_call("-" * 20 + "\n")


if __name__ == "__main__":
    unittest.main()
