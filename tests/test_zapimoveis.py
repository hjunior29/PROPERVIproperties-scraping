import pytest
from unittest.mock import patch, Mock
import scrapers
import requests

@patch('scrapers.zapimoveis.requests.get')
def test_get_property_locations(mock_get):
    
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = """
    <div class="l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-medium card__address">Address 1</div>
    <div class="l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-medium card__address">Address 2</div>
    """
    mock_get.return_value = mock_response

    addresses = scrapers.zapimoveis.get_property_locations()

    assert addresses == ["Address 1", "Address 2"]

@patch('scrapers.zapimoveis.requests.get')
def test_get_property_locations_http_error(mock_get):

    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("403 Client Error")
    mock_get.return_value = mock_response

    addresses = scrapers.zapimoveis.get_property_locations()

    assert addresses == []
