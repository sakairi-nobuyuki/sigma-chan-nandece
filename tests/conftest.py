# coding: utf-8

import pytest

@pytest.fixture(scope='function')
def mock_exchange_rate_parameter():
    parameter_dict = {
        'source': 'yahoo_finance',
        'target': 'DEXJPUS',
        'end': '2022/02/27',
        'duration': '100'
    }
    return parameter_dict
