from src.queue_time import (
    queue_time,
    CustomersValidationError,
    CheckoutsValidationError,
)
import pytest


def test_calculates_time_required():
    # Arrange
    test_customers = [2, 2, 2]
    test_checkouts = 1
    expected = 6
    # Act
    result = queue_time(test_customers, test_checkouts)
    # Assert
    assert result == expected

    # Arrange
    test_customers = [2, 10]
    test_checkouts = 2
    expected = 10
    # Act
    result = queue_time(test_customers, test_checkouts)
    # Assert
    assert result == expected

    # Arrange
    test_customers = [2, 2, 2]
    test_checkouts = 2
    expected = 4
    # Act
    result = queue_time(test_customers, test_checkouts)
    # Assert
    assert result == expected

    # Arrange
    test_customers = [2, 3, 10]
    test_checkouts = 2
    expected = 12
    # Act
    result = queue_time(test_customers, test_checkouts)
    # Assert
    assert result == expected


def test_returns_0_if_no_customers():
    # Arrange
    test_customers = []
    test_checkouts = 2
    expected = 0
    # Act
    result = queue_time(test_customers, test_checkouts)
    # Assert
    assert result == expected


def test_raises_customers_validation_error_if_customers_is_not_a_list():
    with pytest.raises(CustomersValidationError) as excinfo:
        queue_time(2, 2)
    assert str(excinfo.value) == "Customers must be a list of positive integers"


def test_raises_customers_validation_error_if_customers_is_not_a_list_of_positive_integers():
    with pytest.raises(CustomersValidationError) as excinfo:
        queue_time([2, 2, 0], 2)
    assert str(excinfo.value) == "Customers must be a list of positive integers"

    with pytest.raises(CustomersValidationError) as excinfo:
        queue_time([2, 2, "three"], 2)
    assert str(excinfo.value) == "Customers must be a list of positive integers"


def test_raises_checkouts_validation_error_if_checkouts_is_not_a_positive_integer():
    with pytest.raises(CheckoutsValidationError) as excinfo:
        queue_time([2, 2, 2], 0)
    assert str(excinfo.value) == "Checkouts must be a positive integer"

    with pytest.raises(CheckoutsValidationError) as excinfo:
        queue_time([2, 2, 2], "three")
    assert str(excinfo.value) == "Checkouts must be a positive integer"
