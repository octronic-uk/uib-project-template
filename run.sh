#!/bin/bash

echo Starting uib-project-template

echo Starting nginx
nginx

echo Starting API
python model/main.py &
