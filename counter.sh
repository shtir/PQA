#!/bin/bash

python ~/PQA/w106.py 1 counter >> /var/log/counter/counter1.log 2>&1 #SD
sleep 1;
python ~/PQA/w106.py 2 counter >> /var/log/counter/counter2.log 2>&1 #EVAP
sleep 1;
python ~/PQA/w106.py 3 counter >> /var/log/counter/counter3.log 2>&1 #Mixing
sleep 1;
python ~/PQA/w106.py 4 counter >> /var/log/counter/counter4.log 2>&1 #A1V1A01
sleep 1;
python ~/PQA/w106.py 5 counter >> /var/log/counter/counter5.log 2>&1 #Demin
sleep 1;
#python ~/PQA/w106.py 6 counter >> /var/log/counter/counter6.log 2>&1 #MainLab1
#sleep 1;
#python ~/PQA/w106.py 7 counter >> /var/log/counter/counter7.log 2>&1 #MainLab2
#sleep 1;
#python ~/PQA/w106.py 8 counter >> /var/log/counter/counter8.log 2>&1 #Diesel
#sleep 1;
#python ~/PQA/w106.py 9 counter >> /var/log/counter/counter9.log 2>&1 #CB1
#sleep 1;
#python ~/PQA/w106.py 10 counter >> /var/log/counter/counter10.log 2>&1 #CB2
#sleep 1;
#python ~/PQA/w106.py 11 counter >> /var/log/counter/counter11.log 2>&1 #CB3
#sleep 1;
python ~/PQA/w106.py 12 counter >> /var/log/counter/counter12.log 2>&1 #T1
sleep 1;
python ~/PQA/w106.py 13 counter >> /var/log/counter/counter13.log 2>&1 #T2
sleep 1;
python ~/PQA/w106.py 14 counter >> /var/log/counter/counter14.log 2>&1 #T3
sleep 1;
python ~/PQA/w106.py 15 counter >> /var/log/counter/counter15.log 2>&1 #LMDP
sleep 1;
python ~/PQA/w106.py 16 counter >> /var/log/counter/counter16.log 2>&1 #ELMDP
sleep 1;
#python ~/PQA/w106.py 17 counter >> /var/log/counter/counter17.log 2>&1 #sole_sefid
#sleep 1;
python ~/PQA/w106.py 18 counter >> /var/log/counter/counter18.log 2>&1 #Ice_bank
sleep 1;
python ~/PQA/w106.py 19 counter >> /var/log/counter/counter19.log 2>&1 #Comp1
sleep 1;
python ~/PQA/w106.py 20 counter >> /var/log/counter/counter20.log 2>&1 #Comp2
sleep 1;
python ~/PQA/w106.py 21 counter >> /var/log/counter/counter21.log 2>&1 #Comp3
sleep 1;
python ~/PQA/w106.py 22 counter >> /var/log/counter/counter22.log 2>&1 #MPP
sleep 1;
