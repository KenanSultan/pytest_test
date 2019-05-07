import pytest
import mycode

class TestMycode:
    def test_hello_world(self):
        assert mycode.hello() == 'Hello, World'