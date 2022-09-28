#1/usr/bin/python3
"""Doc"""


class MyInt(int):
    def __eq__(self, value):
        return self.real != value
    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value

