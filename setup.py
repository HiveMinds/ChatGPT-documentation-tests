"""Packaging logic for gpt_docs_and_tests."""
from __future__ import annotations

import os
import sys

import setuptools

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
setuptools.setup()
