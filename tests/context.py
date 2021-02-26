# -*- coding: utf-8 -*-

import os
import sys

tests_directory = os.path.dirname(__file__)
relative_path = os.path.join(tests_directory, '..')
absolute_path = os.path.abspath(relative_path)
sys.path.insert(0, absolute_path)
