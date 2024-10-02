from src.counter_intelligence import counter_intelligence
import pytest


def test_returns_empty_string_when_given_empty_string():
    assert counter_intelligence("") == ""

def test_raises_exception_if_not_given_a_string():
    with pytest.raises(TypeError) as excinfo:
        assert counter_intelligence([])
    assert str(excinfo.value) == "Input must be a string"

    with pytest.raises(TypeError) as excinfo:
        assert counter_intelligence(2)

    with pytest.raises(TypeError) as excinfo:
        assert counter_intelligence({"a": 1})

def test_calculates_shift_and_decodes_for_single_char():
    # Arrange
    test_input = "Y"
    expected = "X"
    # Act
    result = counter_intelligence(test_input)
    # Assert
    assert result == expected

def test_handles_spaces():
    # Arrange
    test_input = " Y"
    expected = " X"
    # Act
    result = counter_intelligence(test_input)
    # Assert
    assert result == expected

def test_decodes_multi_char_input():
    # Arrange
    test_input = "BCD Y"
    expected = "ABC X"
    # Act
    result = counter_intelligence(test_input)
    # Assert
    assert result == expected

    # Arrange
    test_input = "NKRRU YCKKZNKGXZ D"
    expected = "HELLO SWEETHEART X"
    # Act
    result = counter_intelligence(test_input)
    # Assert
    assert result == expected

    # Arrange
    test_input = "ANVNVKNA CX YRLT DY IDLLQRWR XW HXDA FJH QXVN OAXV FXAT, MJAURWP G"
    expected = "REMEMBER TO PICK UP ZUCCHINI ON YOUR WAY HOME FROM WORK, DARLING X"
    # Act
    result = counter_intelligence(test_input)
    # Assert
    assert result == expected

def test_handles_lower_case_input():
    # Arrange
    test_input = "ngbk g toik jge :) d"
    expected = "HAVE A NICE DAY :) X"
    # Act
    result = counter_intelligence(test_input)
    # Assert
    assert result == expected