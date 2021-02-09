export LD_LIBRARY_PATH=/home/ogawa/anaconda3/lib:$LD_LIBRARY_PATH
transformers-cli convert --model_type bert \
  --tf_checkpoint Wiki/pretraining_outputWIKI445_recipe/model.ckpt-300000 \
  --config Wiki/pytorch_recipe/bert_config.json \
  --pytorch_dump_output Wiki/pytorch_recipe/pytorch_model.bin
