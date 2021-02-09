#!/usr/bin/env bash

nohup python run_pretraining.py \
    --input_file=WARA_1.tfrecord \
    --output_dir=pretraining_outputWARA9.6_try \
    --do_train=True \
    --do_eval=True \
    --num_train_steps=10000 \
    --save_checkpoints_steps=10000 \
    --learning_rate=9.6e-5 \
    --bert_config_file=bert_config.json \ > outputWARA.log 
    

