#!/usr/bin/env bash

nohup python Create_pretraining_data.py \
    --input_file=WARA_result_2.txt \
    --output_file=WARA_2.tfrecord \
    --vocab_file=WARAtrue.vocab  > CreWR_2.log 
    

