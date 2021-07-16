#!/usr/bin/python3

"""Testing the Binary class and module."""

from binary import TestTwosComplement, TestBinary

if __name__ == "__main__":
    TestTwosComplement().selftest()  # run self-test test cases
    TestBinary().selftest()  # run self-test test cases

# End of file
