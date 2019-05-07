import sys
sys.path.append('./')
from main import Quad
import pytest

quad = Quad(20,6,30)

@pytest.fixture()
def r_quad():
    return quad