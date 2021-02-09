#!/usr/bin/env bash

nohup python run_pretraining.py \
    --input_file=WARA_*.tfrecord \
    --output_dir=pretraining_outputWARA_long_original \
    --do_train=True \
    --do_eval=True \
    --num_train_steps=1000000 \
    --save_checkpoints_steps=100000 \
    --learning_rate=4.1e-5 \
    --bert_config_file=bert_config.json \ > outputWARA.log 
    

