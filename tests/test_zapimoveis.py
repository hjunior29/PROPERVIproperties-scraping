import pytest
from unittest.mock import patch, Mock
import scrapers
import requests

@patch('scrapers.zapimoveis.utils.db_request.add_properties')
@patch('scrapers.zapimoveis.requests.get')
def test_get_properties_data(mock_get, mock_add_properties):
    
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = """
    <div class="l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-medium card__address">"Setor Bueno, Goiânia"</div>
    <div class="l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-medium card__address">"Residencial Itaipu, Goiânia"</div>
    <p class="l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-bold undefined">R$ 290.000</p>
    <p class="l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-bold undefined">R$ 500.000</p>
    """
    mock_get.return_value = mock_response

    addresses, prices = scrapers.zapimoveis.get_properties_data()

    mock_add_properties.assert_called_once()
    assert addresses, prices == {["Setor Bueno, Goiânia", "Residencial Itaipu, Goiânia"], [450000, 216000]}

@patch('scrapers.zapimoveis.utils.db_request.add_properties')
@patch('scrapers.zapimoveis.requests.get')
def test_get_properties_data_http_error(mock_get, mock_add_properties):

    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("403 Client Error")
    mock_get.return_value = mock_response

    mock_add_properties.assert_not_called()
    assert scrapers.zapimoveis.get_properties_data() == None
