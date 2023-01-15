"""
Note that this file cannot be modified.
If you would like to add your own unit tests, please put these in a separate file.
"""

import pytest

from checker.excessive_cancellations_checker import ExcessiveCancellationsChecker

_checker = ExcessiveCancellationsChecker()

@pytest.fixture
def checker_setup():
    return _checker

def test_companies_involved_in_excessive_cancellations(checker_setup):
    assert checker_setup.companies_involved_in_excessive_cancellations() == ["Ape accountants", "Cauldron cooking"]
