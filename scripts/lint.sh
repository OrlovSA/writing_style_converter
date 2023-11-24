#!/bin/sh -e

flake8 writing_style_converter/

black writing_style_converter/ --check