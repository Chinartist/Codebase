import os
import zipfile
 
 
import os 
import zipfile
import tarfile
try:
    import rarfile
    import py7zr
except:
    rarfile = None
    py7zr = None
def download_extract(fname,):
    base_dir = os.path.dirname(fname)
    data_dir, ext = os.path.splitext(fname)
    # base_dir = os.path.join(base_dir,data_dir)
    os.makedirs(base_dir,exist_ok=True)
    if ext == '.zip':
        fp = zipfile.ZipFile(fname, 'r')
    elif ext in ('.tar', '.gz',):
        fp = tarfile.open(fname, 'r')
    elif ext in ('.rar'):
        fp = rarfile.RarFile(fname, mode='r')
    elif ext ==".7z":
        fp = py7zr.SevenZipFile(fname, mode='r')
    fp.extractall(base_dir)
    return None

def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')
 
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()
 

if __name__ == "__main__":
    input_path = "/nvme0/public_data/Occupancy/proj/cache/a2d2/camera_lidar/20180810_150607/clip"
    output_path = "/nvme0/public_data/Occupancy/proj/cache/a2d2/camera_lidar/20180810_150607/clip.zip"
    zipDir(input_path, output_path)
    path = '/nvme0/public_data/Occupancy/proj/cache/a2d2/camera-rearcenter-gaimersheim-a2d2.zip'
    # for f in os.listdir('/nvme0/public_data/Occupancy/proj/img2img-turbo/inputs/vehicle_view.zip'):
    #     path = os.path.join('/nvme0/public_data/Occupancy/proj/img2img-turbo/inputs/OpenDataLab___A2D2/raw/A2D2',f)
    #     download_extract(path)
    #     os.remove(path)
    download_extract(path)
    os.remove(path)