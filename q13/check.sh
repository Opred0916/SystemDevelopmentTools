#!/bin/sh

ruff format --check
ruff check
pytest