# images to videos: ffmpeg -framerate 30 -i frame_%06d.png -codec copy output.mp4

import os
import cv2
import time
import argparse
import numpy as np
from tqdm import tqdm

import pyrealsense2 as rs


def extract_frames(bag_file, img_size=(1280, 720), fps=30, vcheck='n'):
    file_name = bag_file[:-4]
    imgdir_name = os.path.join(opt.dir, f'[{file_name}]_IMAGE')
    if not os.path.exists(imgdir_name):
        os.makedirs(imgdir_name)
    video = cv2.VideoWriter(os.path.join(opt.dir, f'[{file_name}]_VIDEO.avi'),  // make class to save video
                            cv2.VideoWriter_fourcc(*'MJPG'),
                            fps,
                            img_size)

    config = rs.config()
    rs.config.enable_device_from_file(config, os.path.join(opt.dir, bag_file), repeat_playback=False)
    pipeline = rs.pipeline()
    pipeline.start(config)
    config.enable_stream(rs.stream.color, img_size[0], img_size[1], rs.format.bgr8, fps)
    align_to = rs.stream.color
    align = rs.align(align_to)

    i = 0
    while True:
        try:
            frames = pipeline.wait_for_frames()
        except:
            break
        aligned_frames = align.process(frames)

        color_frame = aligned_frames.get_color_frame()

        if color_frame is None:
            pipeline.stop()

        color_image = np.asanyarray(color_frame.get_data())

        color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)
        cv2.imwrite(os.path.join(opt.dir, f'[{file_name}]_IMAGE', f'{file_name}_{i + 1}.png'),  // save image
                    color_image,
                    [cv2.IMWRITE_PNG_COMPRESSION, 0])
        if vcheck.lower() != 'n' and vcheck.lower() != 'no':
            video.write(color_image)
        i += 1
    video.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='bag2rgb.py')
    parser.add_argument('--dir', type=str, default='./', help='*.bag files directory')
    parser.add_argument('--imgsize', type=tuple, default=(1280, 720), help='image size')
    parser.add_argument('--fps', type=int, default=30, help='video frame rate')
    parser.add_argument('--vcheck', type=str, default='y', help='make video .avi')
    opt = parser.parse_args()

    bag_files = [file for file in os.listdir(opt.dir) if file.split('.')[-1] == 'bag']
    if len(bag_files) == 0:
        print('There is no .bag file')
        exit()
    for i, bag in tqdm(enumerate(bag_files),
                       total=len(bag_files),
                       desc='.bag files',
                       leave=True):
        extract_frames(bag, img_size=opt.imgsize, fps=opt.fps, vcheck=opt.vcheck)

        if i == len(bag_files) - 1:
            print('Complete!')
        time.sleep(0.005)
