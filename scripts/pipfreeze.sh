#!/bin/sh -e

pip freeze | grep -vFxf requirements.dev.txt > requirements.txt