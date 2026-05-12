import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):

    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    # -------------------------
    # ADD
    # -------------------------

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(
            response.status,
            http.client.OK,
            f"Error en la petición API a {url}"
        )

    def test_api_add_invalid_parameter(self):
        url = f"{BASE_URL}/calc/add/a/2"

        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    # -------------------------
    # SUBSTRACT
    # -------------------------

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)

    # -------------------------
    # MULTIPLY
    # -------------------------

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)

    # -------------------------
    # DIVIDE
    # -------------------------

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/6/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/6/0"

        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    # -------------------------
    # POWER
    # -------------------------

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)

    # -------------------------
    # SQUARE ROOT
    # -------------------------

    def test_api_square_root(self):
        url = f"{BASE_URL}/calc/square_root/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)

    def test_api_square_root_negative_number(self):
        url = f"{BASE_URL}/calc/square_root/-9"

        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)

    # -------------------------
    # LOGARITHM
    # -------------------------

    def test_api_logarithm(self):
        url = f"{BASE_URL}/calc/logarithm/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)

    def test_api_logarithm_invalid_number(self):
        url = f"{BASE_URL}/calc/logarithm/0"

        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(context.exception.code, http.client.BAD_REQUEST)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()