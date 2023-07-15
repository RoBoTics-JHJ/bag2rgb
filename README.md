```bash
pip install opencv-python realsense2 tqdm
```

```bash
python bag2rgb.py --dir [.bag files's Directory] --imgsize [Extracted Image's Size] --fps [FPS] --vcheck [Yes/No Extracting Video]
                        ./                                 (1280, 720)                    30             n (default)
                                                                                                         y (=yes, if you want a video)
```


```bash
[Directory]
  ├─*.bag
  │
  ├─[.bag filename]_IAMGE      // IMAGE dir Will be created
  │  └─[.bag filename]_1.png
  │  └─[.bag filename]_2.png
  ├─[.bag filename]_VIDEO.avi   // VIDEO Will be created
```
