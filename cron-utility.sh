#!/bin/bash

while true; do

# Ice_bank
python ~/PQA/w106.py 18 volt
sleep 2;

# Comp1
python ~/PQA/w106.py 19 volt
sleep 2;

# Comp2
python ~/PQA/w106.py 20 volt
sleep 2;

# Comp3
python ~/PQA/w106.py 21 volt
sleep 2;  

# MPP
python ~/PQA/w106.py 22 volt
sleep 2;

done
