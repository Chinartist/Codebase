export HF_ENDPOINT=https://hf-mirror.com

<<<<<<< HEAD
model_name="facebook/VGGT-1B"
=======
model_name="nvidia/difix"
>>>>>>> dcb249609db98b1be03df7744d5a3ec4c87915f7
huggingface-cli download --token $HUGGINGFACE_TOKEN $model_name \
    --local-dir /home/tangyuan/project/cache/$model_name \
    --max-workers 16 \
<<<<<<< HEAD
    --exclude "*.non_ema.bin" "v1-5-pruned.ckpt" "*.ckpt" "*fp8*" "*.pt" "*bin" "*pruned.ckpt" "*fp16.safetensors" "*nonema-pruned.safetensors" "sd3.5_large.safetensors" "*fp16*"\
    # --include "i2vgenxl_canny/*" \
=======
    --exclude "*.non_ema.bin" "v1-5-pruned.ckpt" "*.ckpt" "*fp8*" "*pruned.ckpt" "*fp16.safetensors" "*nonema-pruned.safetensors" "sd3.5_large.safetensors" "*fp16*"\
    --include "unet/*" \
>>>>>>> dcb249609db98b1be03df7744d5a3ec4c87915f7
