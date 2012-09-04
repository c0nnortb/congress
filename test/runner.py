#!/usr/bin/env python

import sys
import unittest
sys.path.append("tasks") # allow test classes to easily load tasks
sys.path.append("test") # allow fixtures.py to be loaded

tests = unittest.TestLoader().discover("test")
results = unittest.TextTestRunner().run(tests)

if len(results.failures) > 0:
  exit(1)
else:
  exit(0)