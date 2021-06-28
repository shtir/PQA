#!/bin/bash

while true; do

# Diesel
python ~/PQA/w106.py 8 volt
sleep 1;

# B1
python ~/PQA/w106.py 9 volt
sleep 1;

# B2
python ~/PQA/w106.py 10 volt
sleep 1;

# B3
python ~/PQA/w106.py 11 volt
sleep 1;

# T1
python ~/PQA/w106.py 12 volt
sleep 1;

# T2
python ~/PQA/w106.py 13 volt
sleep 1;

# T3
python ~/PQA/w106.py 14 volt
sleep 1;

done
