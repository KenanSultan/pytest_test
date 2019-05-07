import pytest

@pytest.mark.usefixtures("r_quad")
class TestQuad:

    def test_is_valid(self, r_quad):
        assert r_quad.is_valid() == True

    def test_setter(self, r_quad):
        r_quad.setter("10", -20, 30)
        assert r_quad.is_valid() == False