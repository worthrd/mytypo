import pytest
import os

from ..mytypo import check_typo
# this comment has miss spel word

def test_typo_correction():
    p = os.path.abspath(".") + "/mytypo/tests/test_mytypo.py"
    suggestions = check_typo(path=p)
    assert len(suggestions) == 1
