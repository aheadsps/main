import pytestfrom src.processing import filter_by_state, sort_by_date# позитивный тест filter_by_state -> 100% PASSEDdef test_filter_by_state_positive(list_of_dictionaries_positive, list_of_dictionaries_positive_expected_values):    assert filter_by_state(list_of_dictionaries_positive) == list_of_dictionaries_positive_expected_values# негативный тест filter_by_state -> 100% PASSEDdef test_filter_by_state_negative(list_of_dictionaries_negative_by_sort_by_state):    with pytest.raises(Exception):        assert filter_by_state(list_of_dictionaries_negative_by_sort_by_state)# позитивный тест sort_by_date -> 100% PASSEDdef test_sort_by_date_positive(list_of_dictionaries_positive, dictionaries_positive_expected_values_by_sort_by_date):    assert sort_by_date(list_of_dictionaries_positive) == dictionaries_positive_expected_values_by_sort_by_date# негативный тест sort_by_date -> 100% PASSEDdef test_sort_by_date_negative(list_of_dictionaries_negative_by_sort_by_date):    with pytest.raises(Exception):        assert sort_by_date(list_of_dictionaries_negative_by_sort_by_date)if __name__ == '__main__':    pytest.main(['-vv'])