#!/bin/bash

while true; do

# H1V1A01
python ~/PQA/w106.py 1 volt
sleep 2;

# F1V1A01 
python ~/PQA/w106.py 2 volt
sleep 2;

# A1V1A02
python ~/PQA/w106.py 3 volt
sleep 2;

# A1V1A01
python ~/PQA/w106.py 4 volt
sleep 2;

# D1V1A01
python ~/PQA/w106.py 5 volt
sleep 2;

done
