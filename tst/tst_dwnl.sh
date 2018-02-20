#!/bin/bash

input_csv="http://rapid-hub.org/data/angles_UCI_CS.csv"
output_csv="http://rapid-hub.org/data/angles_UCI_CS_out.csv"

wget $input_csv 
wget $output_csv
