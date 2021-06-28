#!/bin/bash

while true; do

# MainLab1
python ~/PQA/w106.py 6 volt
sleep 2;

# MainLab2
python ~/PQA/w106.py 7 volt
sleep 2;

# LMDP
python ~/PQA/w106.py 15 volt
sleep 2;

# ELMDP
python ~/PQA/w106.py 16 volt
sleep 2;

# sole_sefid
python ~/PQA/w106.py 17 volt
sleep 2;

done
