#!/usr/bash

CC=python
MAKE=make
FLAKES=pyflakes

.PHONY: clean

# Remove all the compiled files
clean:
	@echo "Cleaning..."
	find . -name "*.pyc" | xargs rm -rf

help:
	@echo "*** Help ***"
	@echo "#> make [all] - compile all files"
	@echo "#> make clean - remove all .pyc files"
