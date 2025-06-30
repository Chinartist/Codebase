
DATASET_PATH="/nvme0/public_data/Occupancy/proj/img2img-turbo/outputs/120f/cycle_1_cmp"
colmap feature_extractor \
   --database_path $DATASET_PATH/database.db \
   --image_path $DATASET_PATH/images \
   # --ImageReader.mask_path $DATASET_PATH/masks
colmap exhaustive_matcher \
   --database_path $DATASET_PATH/database.db
mkdir $DATASET_PATH/sparse
colmap mapper \
    --database_path $DATASET_PATH/database.db \
    --image_path $DATASET_PATH/images \
    --output_path $DATASET_PATH/sparse \
    