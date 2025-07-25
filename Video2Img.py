import cv2
import os

def video2imgs(videoPath, imgPath):
    if not os.path.exists(imgPath):
        os.makedirs(imgPath)             # 目标文件夹不存在，则创建
    cap = cv2.VideoCapture(videoPath)    # 获取视频
    judge = cap.isOpened()                 # 判断是否能打开成功
    print(judge)
    fps = cap.get(cv2.CAP_PROP_FPS)      # 帧率，视频每秒展示多少张图片
    print('fps:',fps)

    frames = 1                           # 用于统计所有帧数
    count = 1                            # 用于统计保存的图片数量

    while(judge):
        flag, frame = cap.read()         # 读取每一张图片 flag表示是否读取成功，frame是图片
        if not flag:
            print(flag)
            print("Process finished!")
            break
        else:
            if frames % 1 == 0:        
                imgname =  str(count).rjust(3,'0') + ".jpg"
                newPath = os.path.join(imgPath , imgname)
                print(imgname)
                # frame=frame[:,frame.shape[1]//2:,:]  # 裁剪图片，保留右半部分
                cv2.imwrite(newPath, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
                # cv2.imencode('.jpg', frame)[1].tofile(newPath)
                count += 1
        frames += 1
    cap.release()
    print("共有 %d 张图片"%(count-1))
video2imgs('/nvme0/public_data/Occupancy/proj/Generation/cosmos-predict1/outputs/0.mp4','/nvme0/public_data/Occupancy/proj/vggt/examples/drive/images')  # 视频路径，图片保存路径
