#!/usr/bin/python3
"""Define geometry."""


class square():
    """Square base class."""

    width = 0

    def __init__(self, *args, **kwargs):
        """Initialize the square."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square."""
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Permiter of my square."""
        return 2 * (self.width * 2)

    def __str__(self):
        """Str repr of square instance."""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
