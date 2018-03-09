NAME=pybib

.PHONY: default
default: build

.PHONY: build
build:
	python setup.py bdist_wheel --universal

.PHONY: clean
clean:
	rm -r "build/"
	rm -r "dist/"
	rm -r "$(NAME).egg-info/"

