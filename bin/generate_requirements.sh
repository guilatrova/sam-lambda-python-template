#!/bin/bash

poetry export -f requirements.txt --output src/requirements.txt --without-hashes
