#!/bin/sh -e

isort writing_style_converter/
isort tests/

black writing_style_converter/
black tests/