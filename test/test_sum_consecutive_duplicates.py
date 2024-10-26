from src.sum_consecutive_duplicates import (
    sum_consecutive_duplicates,
    reduce_consecutives,
)


class TestSumConsecutiveDuplicates:
    def test_default_behaviour_returns_empty_list_when_given_empty_list(self):
        assert sum_consecutive_duplicates([]) == []

    def test_default_behaviour_returns_given_list_if_there_are_no_duplicates(self):
        assert sum_consecutive_duplicates([1, 2, 3]) == [1, 2, 3]

    def test_handles_one_set_of_consecutive_duplicates(self):
        assert sum_consecutive_duplicates([1, 1, 2, 3]) == [2, 2, 3]

    def test_handles_multiple_sets_of_consecutive_duplicates(self):
        # Arrange
        test_input = [1, 1, 2, 2, 3, 3]
        expected = [2, 4, 6]
        # Act
        result = sum_consecutive_duplicates(test_input)
        # Assert
        assert result == expected

        # Arrange
        test_input = [1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1]
        expected = [2, 2, 4, 2, 3]
        # Act
        result = sum_consecutive_duplicates(test_input)
        # Assert
        assert result == expected


class TestReduceConsecutives:
    def test_recursively_reduces_list_until_no_more_consecutive_duplicates(self):
        # Arrange
        test_input = [1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1]
        expected = [8, 2, 3]
        # Act
        result = reduce_consecutives(test_input)
        # Assert
        assert result == expected
