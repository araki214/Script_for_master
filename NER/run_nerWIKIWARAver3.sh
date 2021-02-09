#!/usr/bin/env bash

nohup  python BERT_NER.py\
    --task_name="NER"  \
    --do_lower_case=False \
    --crf=True \
    --do_train=True   \
    --do_eval=True   \
    --do_predict=True \
    --data_dir=data  \
    --vocab_file=WIKIWARA/vocab.txt  \
    --bert_config_file=WIKIWARA/bert_config.json \
    --init_checkpoint=WIKIWARA/model.ckpt   \
    --max_seq_length=128   \
    --train_batch_size=32   \
    --learning_rate=2e-5   \
    --num_train_epochs=4.0   \
    --output_dir=./output/WIKIWARAver3


perl conlleval.pl -d '\t' < ./output/WIKIWARAver3/label_test.txt
