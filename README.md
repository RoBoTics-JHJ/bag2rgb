```bash
pip install opencv-python realsense2 tqdm
```

### Only extract RGB images and video (no depth)
```bash
python bag2rgb.py --dir [.bag files's Directory] --imgsize [Extracted Image's Size] --fps [FPS] --vcheck [Yes/No Extracting Video]
                        ./                                 (1280, 720)                    30             n (=no, if you don't want a video)
                                                                                                         y (=yes, default)
```


```bash
📁 [Directory]
  ├─ *.bag
  │
  ├─📁 [.bag filename]_IAMGE      // IMAGE dir
  │  └─ [.bag filename]_1.png
  │  └─ [.bag filename]_2.png
  ├─ [.bag filename]_VIDEO.avi    // VIDEO
```
IMAGEs and VIDEOs will be placed in the same dir with ".bag" file
