#!/usr/bin/bash

nohup subword-nmt learn-bpe -s 22470 < WARA.full > WARA.vocab 
nohup subword-nmt apply-bpe -c WARA.vocab <WARA.full> WARA_result.txt 
nohup python makevocab.py WARA_result.txt WARAtrue.vocab > output.log
wc -l WARAtrue.vocab
#nohup rm -r WAKA.vocab
#nohup rm -r WAKA_result.txt
