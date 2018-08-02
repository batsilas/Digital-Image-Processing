import numpy as np
import matplotlib.image as mpimg
import scipy.misc
from PIL import Image
A = np.array(Image.open('trikoupi6.png'))
C = np.zeros(A.shape)
nrows,ncols = A.shape
B =[0,30,60,90,120,150,180,210,240]


for k in range (0,9):
    for i in range(0,nrows):
        for j in range(0,ncols):
            if(A[i][j]<=B[k]):
                C[i][j] = 0
            else:
                C[i][j] = 255
    scipy.misc.imsave('picK=%d.png'%(B[k]),C)
    
