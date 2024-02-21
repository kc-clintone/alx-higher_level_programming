Import the function from the module:
        >>> base_geometry = __import__("7-base_geometry").BaseGeometry

Check for module docstring:
         >>> m_doc = __import__("7-base_geometry").__doc__
         >>> len(m_doc) > 1
         True
Check for class docstring:
         >>> c_doc = __import__("7-base_geometry").BaseGeometry.__doc__
         >>> len(c_doc) > 1
         True
Check for method docstring:
          >>> me_doc = __import__("7-base_geometry").BaseGeometry.area.__doc__
          >>> len(me_doc) > 1
          True
          >>> me_doc = __import__("7-base_geometry").BaseGeometry.integer_validator.__doc__
          >>> len(me_doc) > 1
          True
Check for area failure:
          >>> fail = base_geometry()
          >>> fail.area()
          Traceback (most recent call last):
          ...
          Exception: area() is not implemented
Check if tyere's too many arguments for area:
          >>> base.area(1)
          Traceback (most recent call last):
          ...
          TypeError: area() takes 1 positional argument but 2 were given
Check the integer validator for parsing integer:
          >>> base.integer_validator("integer", 1)
Check for integer == 0:
          >>> base.integer_validator("integer", 0)
          Traceback (most recent call last):
          ...
          ValueError: integer must be greater than 0
Check for integer < 0;
          >>> base.integer_validator("integer", -5)
          Traceback (most recent call last):
          ...
          ValueError: integer must be greater than 0
Check for non-integer types:
          >>> base.integer_validator("bool", True)
          Traceback (most recent call last):
          ...
          TypeError: bool must be an integer
          >>> base.integer_validator("float", 1.5)
          Traceback (most recent call last):
          ...
          TypeError: float must be an integer
          >>> base.integer_validator("complex", complex(1, 1))
          Traceback (most recent call last):
          ...
          TypeError: complex must be an integer
          >>> base.integer_validator("string", "hello")
          Traceback (most recent call last):
          ...
          TypeError: string must be an integer
          >>> base.integer_validator("tuple", (1, 2))
          Traceback (most recent call last):
          ...
          TypeError: tuple must be an integer
          >>> base.integer_validator("list", [1, 2, 3])
          Traceback (most recent call last):
          ...
          TypeError: list must be an integer
          >>> base.integer_validator("dict", {"key": "value"})
          Traceback (most recent call last):
          ...
          TypeError: dict must be an integer
          >>> base.integer_validator("set", {"hello", "world"})
          Traceback (most recent call last):
          ...
          TypeError: set must be an integer
          >>> base.integer_validator("frozenset", frozenset(["hello", "world"]))
          Traceback (most recent call last):
          ...
          TypeError: frozenset must be an integer
          >>> base.integer_validator("bytes", b"bytes")
          Traceback (most recent call last):
          ...
          TypeError: bytes must be an integer
          >>> base.integer_validator("bytearrays", bytearray(b"bytes"))
          Traceback (most recent call last):
          ...
          TypeError: bytearrays must be an integer
Check for no arguments to integer_validator:
          >>> base.integer_validator()
          Traceback (most recent call last):
          ...
          TypeError: integer_validator() missing 2 required positional arguments: 'name' and 'value'
Check for only 1 argument to integer_validator:
          >>> base.integer_validator("integer")
          Traceback (most recent call last):
          ...
          TypeError: integer_validator() missing 1 required positional argument: 'value'
Check for too many arguments:
          >>> base.integer_validator("integer", 1, 2)
          Traceback (most recent call last):
          ...
          TypeError: integer_validator() takes 3 positional arguments but 4 were given
