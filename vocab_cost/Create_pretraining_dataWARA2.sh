#!/usr/bin/env bash

nohup python Create_pretraining_data.py \
    --input_file=/mnt/mqs02/data/ogawa/BERT/preprocess-for-BERT/conbination/NUMAS/vocab_cost/WARAresult_2.txt \
    --output_file=WARA_2.tfrecord \
    --vocab_file=WARAtrue.vocab  > CreWR_2.log 
    

