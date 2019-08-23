#!/bin/bash
cut -d, -f9,10 ~/chou_lab/EVE/test_filtered.csv
cut -d, -f13 ~/chou_lab/EVE/test_filtered.csv > test_names.csv
