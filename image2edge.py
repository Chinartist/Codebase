import os
import cv2
import numpy as np
from PIL import Image
import glob

def canny_from_pil(image, low_threshold=50, high_threshold=100):
    ori_image = np.array(image)[..., :3]
    # print(ori_image.shape)
    image = cv2.Canny(ori_image, low_threshold, high_threshold)
    image = image[:, :, None]
    image = np.concatenate([image, image, image], axis=2)
    return image
image_dir = "/home/tangyuan/project/Four_View_sr_masked"
save_dir = "/home/tangyuan/project/Four_View_sr_masked-edge"



os.makedirs(os.path.join(save_dir), exist_ok=True)
for i,image_file in enumerate(os.listdir(image_dir)):
    image = Image.open(os.path.join(image_dir,image_file))
    control_image = canny_from_pil(image)
    # control_image.save(os.path.join(save_dir,os.path.basename(image_file)))
    cv2.imwrite(os.path.join(save_dir,os.path.basename(image_file)),control_image)