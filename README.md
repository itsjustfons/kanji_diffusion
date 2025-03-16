1. Download kanjidic.xml and kanjivg.xml from http://kanjivg.tagaini.net
2. Run make_annotation.py and direct it to kanjidic.xml and kanjivg.xml
3. Run kanji_visualizer.py and direct it to kanjidic.xml file, and run blank_deleter to filter out any missing characters from the original dataset
3. Run make_csv.py, make_json.py and make_pkt.py, and store the generated anotation files into the same folder containing the generated kanji images
4. Download or git clone Huggingface diffusers: https://github.com/huggingface/diffusers
5. Follow the instructions of Huggingface diffusers by directing the kanji_diffusion3/diffusers/examples/text_to_image/test_text_to_image.py to the folder containing the kanji images. The dataset library of the python code should align the the images to the kanji character

export MODEL_NAME="CompVis/stable-diffusion-v1-4"
export TRAIN_DIR="../../../../kanji_images"

accelerate launch --mixed_precision="fp16" train_text_to_image.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --train_data_dir=$TRAIN_DIR \
  --use_ema \
  --resolution=128 --center_crop --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --gradient_checkpointing \
  --max_train_steps=15000 \
  --learning_rate=1e-05 \
  --max_grad_norm=1 \
  --lr_scheduler="constant" --lr_warmup_steps=0 \
  --output_dir="kanji_diffusion_b" 
  #--enable_xformers_memory_efficient_attention