# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:26:38 2024

@author: 郭浩楠
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:53:22 2024

@author: 郭浩楠
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:01:32 2023

@author: 郭浩楠
"""
import numpy as np
import torch
import matplotlib.pyplot as plt
#fig = plt.figure(figsize=(10, 7))
xishu1 = [-499.999972163061,
12409.5341023398,
4698.86973636409,
-42.9974520058392,
-177.139955380376,
-65.6802968014837,
-0.0292918880326185,
0.467877222389366,
0.948366941669721,
0.343619400728396,
-2.85173519880239e-05,
0.000212962266607855,
-0.00169315158225515,
-0.00225715694169534,
-0.000797019801370004,
-1.85510204356672e-08,
9.47960031583713e-08,
-3.84030940909101e-07,
2.03773030530206e-06,
2.01516367415139e-06,
6.91429866920962e-07,]



xishu1 = np.reshape(np.array(xishu1,dtype = np.double),(1,int(len(xishu1)/1)))

cishu = 5
lie_num=0
for i in range(1,cishu+2):
    lie_num=lie_num+i


tt = np.zeros((2,lie_num))
k = 1
for i in range(1,cishu+1):
    for j in range(i+1):
        tt[0,k] = j
        tt[1,k] = i-j
        k = k+1




cishu = 5


lie_num=0
for i in range(1,cishu+2):
    lie_num=lie_num+i


tt = np.zeros((2,lie_num))
k = 1
for i in range(1,cishu+1):
    for j in range(i+1):
        tt[0,k] = j
        tt[1,k] = i-j
        k = k+1

rows = np.linspace(270, 300, 50)
cols = np.linspace(-65, 65, 50)
r,z = np.meshgrid(rows,cols)
r = r.reshape((50*50,1))
z = z.reshape((50*50,1))
points = np.concatenate((r, z), axis=1)


def creat_data(points):

        
# 
    
    

        
    r = points[:,0].reshape(len(points),1)
    z = points[:,1].reshape(len(points),1)


    ls = np.multiply(((r.T)**0),((z.T)**0))
    for i in range(1,lie_num):
        ls = np.append(ls.reshape(i,len(points)),np.multiply(((r.T)**tt[0,i]),((z.T)**tt[1,i])).reshape(1,len(points)),axis = 0)
    


    yl_xx =  (np.matmul(xishu1[0],ls).reshape(len(points),1))

    
    return yl_xx


yl_xx_lkf= \
            creat_data(points)  


import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False  # 解决保存图像是负号"-"显示为方块的问题
plt.rc('font',family='Times New Roman') 
my_dpi = 100
fig, axs = plt.subplots(1 ,1,figsize = (5,5),dpi=100)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, \
                    wspace=0.5, hspace=0.5)



###轮廓法的数据
            
cc = axs.matshow(yl_xx_lkf.reshape(50,50))
# fig.colorbar(cc,ax=axs[1])
fig.colorbar(cc,ax=axs,pad = 0.2,shrink = 0.5)
#            axs[0,0].axis('off')

axs.set_title('(b) '+r'$ \sigma_{\theta\theta} $'+" of contour method",y=-0.1,fontsize = 12)
axs.title.set_position([.5, -0.1])
# axs[0,0].title.set_position([.5, -0.3])
# axs[0,0].title.set_position([0.5,0.8])
# axs[0,0].title.set_fontsize(12)

axs.axis('off')



