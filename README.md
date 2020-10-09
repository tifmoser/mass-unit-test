# mass-unit-test
A tool for formatting unit tests

## Usage
These functions are intended to be used in the Python shell.
```
>>> %Run mass_unit_test.py

>>> mass_unit_test (add5, "1|2|3", '|')
assert_equal(add5(1), ___)
assert_equal(add5(2), ___)
assert_equal(add5(3), ___)

>>> mass_unit_test (add5, "1|2|3", '|', "5_6_7", '_')
assert_equal(add5(1), 5)
assert_equal(add5(2), 6)
assert_equal(add5(3), 7)
```
The output can then be copy+pasted into your own code, for unit testing purposes.

## Contributing
Feel free to play around with the code, suggest improvements, do whatever! (except selling it. That's naughty.)
If you need help figuring out how to create a branch, make a pull request, etc, see below for support.

## Support
You can contact me at tifmoser@udel.edu, or on Discord (Skalisty#6388). The TA's and professors can probably also help you out with most of your problems!
