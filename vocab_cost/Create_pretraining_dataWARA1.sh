#!/usr/bin/env bash

nohup python Create_pretraining_data.py \
    --input_file=WARA_result.txt \
    --output_file=WARA_1.tfrecord \
    --vocab_file=WARAtrue.vocab  > CreWR_1.log 
    

