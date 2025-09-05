import os
import pandas as pd
import numpy as np
from PIL import Image
import cv2
from argparse_dataclass import dataclass,ArgumentParser
@dataclass
class Options:
    data_dir: str = "/home/tangyuan/project/car_segment_"
    output_dir: str = "/home/tangyuan/project/car_segment_wjq"

parser = ArgumentParser(Options)
args = parser.parse_args()

video_names = os.listdir(args.data_dir)
for video_name in video_names:
    video_path = os.path.join(args.data_dir, video_name)
    instance_names = os.listdir(video_path)
    for instance_name in instance_names:
        instance_path = os.path.join(video_path, instance_name)
        image_path = os.path.join(instance_path, "images")
        mask_path = os.path.join(instance_path, "masks")
        mask_files = sorted(os.listdir(mask_path))
        cam_list = ["CamS","CamE","CamW","CamN"]
        cam2name = {k:[] for k in cam_list}
        for mask_file in mask_files:
            for cam in cam_list:
                if cam in mask_file:
                    cam2name[cam].append(mask_file)
        best_names = []
        for cam in cam_list:
            best_mask_name = cam2name[cam][0]
            max_area =( np.array(Image.open(os.path.join(mask_path, best_mask_name)))>0).sum()
            for mask_name in cam2name[cam]:
                mask = Image.open(os.path.join(mask_path, mask_name))
                area = (np.array(mask)>0).sum()
                if area > max_area:
                    max_area = area
                    best_mask_name = mask_name
            if max_area>0:
                best_names.append(best_mask_name)
        output_dir = os.path.join(args.output_dir, video_name,instance_name,"Four_View")
        os.makedirs(output_dir,exist_ok=True)
        
        for best_name in best_names:
            image = np.array(Image.open(os.path.join(image_path, best_name.replace(".png", ".jpg"))))
            mask = np.array(Image.open(os.path.join(mask_path, best_name)))
            contours, _ =cv2.findContours( mask.astype(np.uint8),mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
            contour = max(contours, key=cv2.contourArea)
            
            b = 20
            x, y, w, h = cv2.boundingRect(contour)
            x = max(0, x - b)
            y = max(0, y - b)
            w = min(image.shape[1] - x, w + 2 * b)
            h = min(image.shape[0] - y, h + 2 * b)
            cut_image = image[y:y+h, x:x+w]
            cut_sem = mask[y:y+h, x:x+w]
            Image.fromarray(cut_image).save(os.path.join(output_dir,best_name.replace(".png", f".jpg")))
        if best_names ==3:
            Image.open(os.path.join(output_dir,best_name.replace(".png", f".jpg"))).save(os.path.join(output_dir,best_name.replace(".png", f"_copy.jpg")))

