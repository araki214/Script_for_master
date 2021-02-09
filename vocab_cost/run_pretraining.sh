#!/usr/bin/env bash

nohup python run_pretraining2.py \
    --input_file=WARA_1.tfrecord \
    --output_dir=pretraining_outputWARA4.1_30_ver2 \
    --do_train=True \
    --do_eval=True \
    --num_train_steps=300000 \
    --save_checkpoints_steps=300000 \
    --learning_rate=4.1e-5 \
    --bert_config_file=bert_config.json \ > outputWARA.log 
    

