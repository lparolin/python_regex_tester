import unittest
from python_regex_tester.regex_tester import extract_python_lib


class PythonLibraryTest(unittest.TestCase):

    def setUp(self):
        self.in_data = """
#!/usr/bin/env python27
import urllib2
import base64
import json
import os
import sys
import re

os.system("clear")
print "-" * 80
print "Command Line Search Tool"
print "-" * 80

def Banner(text):
    print "=" * 70
    print text
    print "=" * 70
    sys.stdout.flush()
"""

    def test_extract_library_when_typical(self):
        expected_library = [
            "urllib2",
            "ase64",
            "json",
            "os",
            "sys",
            "re"
        ]
        out_list = extract_python_lib(self.in_data)
        self.assertEqual(expected_library, out_list)


if __name__ == '__main__':
    unittest.main()
