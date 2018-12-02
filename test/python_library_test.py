import unittest
from python_regex_tester.regex_tester import extract_python_lib, \
    make_all_single_lines, get_import_lines, get_import_items


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

import urllib2, base64,     json, os, sys,      re
import (urllib2, base64,     json, os, sys,      re)
import (urllib2, base64,     json, os, sys, \
        re)

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
        self.in_data_all_one_lines = """
#!/usr/bin/env python27
import urllib2
import base64
import json
import os
import sys
import re

import urllib2, base64,     json, os, sys,      re
import (urllib2, base64,     json, os, sys,      re)
import (urllib2, base64,     json, os, sys,         re)

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

        self.in_data_import_lines = [
            "urllib2",
            "base64",
            "json",
            "os",
            "sys",
            "re",
            "urllib2, base64,     json, os, sys,      re",
            "(urllib2, base64,     json, os, sys,      re)",
            "(urllib2, base64,     json, os, sys,         re)"]

        self.in_data_import_items = [
            "urllib2",
            "base64",
            "json",
            "os",
            "sys",
            "re"].sort()

    def test_make_all_single_lines(self):
        expected_text = self.in_data_all_one_lines
        self.assertEqual(expected_text, make_all_single_lines(self.in_data))

    def test_get_import_lines(self):
        expected_text = self.in_data_import_lines
        self.assertEqual(expected_text, get_import_lines(self.in_data_all_one_lines))

    def test_get_import_items(self):
        expected_text = self.in_data_import_items
        self.assertEqual(expected_text, get_import_items(self.in_data_import_lines))

    def test_extract_library_when_typical(self):
        expected_library = self.in_data_import_items
        out_list = extract_python_lib(self.in_data)
        self.assertEqual(expected_library, out_list)

if __name__ == '__main__':
    unittest.main()
