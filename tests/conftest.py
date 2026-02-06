"""
Docstring for tests.conftest
"""
import pytest

@pytest.fixture
def qualidade() -> str:
    return "bonita"
