export HF_ENDPOINT=https://hf-mirror.com

model_name="nvidia/difix"
huggingface-cli download --token $HUGGINGFACE_TOKEN $model_name \
    --local-dir /nvme0/public_data/Occupancy/proj/cache/$model_name \
    --max-workers 16 \
    --exclude "*.non_ema.bin" "v1-5-pruned.ckpt" "*.ckpt" "*fp8*" "*pruned.ckpt" "*fp16.safetensors" "*nonema-pruned.safetensors" "sd3.5_large.safetensors" "*fp16*"\
    --include "unet/*" \