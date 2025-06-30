import cv2
import numpy as np
import os
import random
dir = "/nvme0/public_data/Occupancy/proj/Generation/cosmos-predict1/datasets/instance_6"
image_dir = f"{dir}/images"
mask_dir = f"{dir}/masks"
output_dir = f"{dir}/instance"
for m in os.listdir(mask_dir):
    # if "R" in m:
    #     continue
    mask = cv2.imread(os.path.join(mask_dir, m), cv2.IMREAD_GRAYSCALE)
    image = cv2.imread(os.path.join(image_dir, m.replace("png", "jpg")))
    contours, _ =cv2.findContours( mask.astype(np.uint8),mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        cut_image = image[y:y+h, x:x+w]
        cut_sem = mask[y:y+h, x:x+w]
        cut_image[cut_sem == 0] = 255
        os.makedirs(output_dir, exist_ok=True)
        # cut_image  =cv2.resize(cut_image, (256, 256), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(os.path.join(output_dir,m),cut_image)
def BboxFromMask(mask):
    contours, _ = cv2.findContours(mask.astype(np.uint8), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    bboxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        bboxes.append((x, y, w, h))
    return bboxes