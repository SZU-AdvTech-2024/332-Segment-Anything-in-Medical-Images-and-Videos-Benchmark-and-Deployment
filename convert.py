import numpy as np
import cv2

img_path = 'data/npy/CT_LiTS/imgs/CT_LiTS_volume-108-202.npy'
img = np.load(img_path)

print(img.shape)  # (1024, 1024, 3)
img = img * 255
img = cv2.imwrite('liTS.png', img)
