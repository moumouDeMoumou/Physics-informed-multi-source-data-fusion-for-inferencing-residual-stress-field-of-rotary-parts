# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:42:28 2024

@author: 郭浩楠
"""

import numpy as np
 
# 假设有一个名为 'data.npy' 的文件
file_path = 'xishunew.npy'
 
# 读取.npy文件
data = np.load(file_path)
 
# 使用数据
# print(data)
xishu1 =data[0]

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
cols = np.linspace(-70, 70, 50)
r,z = np.meshgrid(rows,cols)
r = r.reshape((50*50,1))
z = z.reshape((50*50,1))
num_points = 50*50
ls = np.multiply(((r.T)**0),((z.T)**0))
for i in range(1,lie_num):
    ls = np.append(ls.reshape(i,num_points),np.multiply(((r.T)**tt[0,i]),((z.T)**tt[1,i])).reshape(1,num_points),axis = 0)

yl_rr = (np.matmul(xishu1[0],ls).reshape(50,50))
yl_xx = (np.matmul(xishu1[1],ls).reshape(50,50))
yl_zz = (np.matmul(xishu1[2],ls).reshape(50,50))
yl_rz = (np.matmul(xishu1[3],ls).reshape(50,50))


import matplotlib.pyplot as plt

my_dpi = 96
fig, axs = plt.subplots(1, 4,figsize = (10,7))

cc = axs[0].matshow(yl_rr)
fig.colorbar(cc,ax=axs[0],pad = 0.2,shrink = 0.3)
#            axs[0,0].axis('off')
axs[0].set_title('(a) '+r'$ \sigma_{\theta\theta} $',y=-0.5,fontsize = 12)

axs[0].title.set_position([.5, -0.5])
# axs[0,0].title.set_position([.5, -0.3])
# axs[0,0].title.set_position([0.5,0.8])
# axs[0,0].title.set_fontsize(12)

axs[0].axis('off')

########切向


cc = axs[1].matshow(yl_xx)
fig.colorbar(cc,ax=axs[1],pad = 0.2,shrink = 0.3)
#            axs[0,0].axis('off')

axs[1].set_title('(b) '+r'$ \sigma_{\theta\theta} $',y=-0.5,fontsize = 12)
axs[1].axis('off')




#####################################轴向应力

cc = axs[2].matshow(yl_zz)
fig.colorbar(cc,ax=axs[2],pad = 0.2,shrink = 0.3)
#            axs[0,0].axis('off')

axs[2].set_title('(c)  '+r'$ \sigma_{zz} $',y=-0.5,fontsize = 12)
axs[2].axis('off')



##################rz向应力

cc = axs[3].matshow(yl_rz)
fig.colorbar(cc,ax=axs[3],pad = 0.2,shrink = 0.3)
#            axs[0,0].axis('off')

axs[3].set_title('(d) '+r'$ \sigma_{rz} $',y=-0.5,fontsize = 12)
axs[3].axis('off')


# 假设有一个名为 'data.npy' 的文件
file_path = 'bxlnew.npy'
 
# 读取.npy文件
deformation_forces = np.load(file_path)
 
# 使用数据
# print(data)
deformation_force =deformation_forces[0]   





fig, axs = plt.subplots(1, 1,figsize = (16,8),dpi = 100)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, \
                    wspace=0.3 ,hspace=None)
x = np.linspace(1,90,90)
# 解决中文显示问题
#plt.rcParams["font.sans-serif"] = ["KaiTi"]  # 指定默认字体
plt.rc('font' ,family='Times New Roman')
plt.rcParams["axes.unicode_minus"] = False  # 解决保存图像是负号"-"显示为方块的问题
plt.style.use("default") # 设置ggplot样式
####################################6个工步版############################
#这个是试验得到的单步变形量的值
axs.plot(x,deformation_force[:,0],label="Monitoring point 1",linewidth=1.5)
axs.plot(x,deformation_force[:,1],label="Monitoring point 2",linewidth=1.5)
axs.plot(x,deformation_force[:,2],label="Monitoring point 3",linewidth=1.5)
axs.plot(x,deformation_force[:,3],label="Monitoring point 4",linewidth=1.5)
axs.plot(x,deformation_force[:,4],label="Monitoring point 5",linewidth=1.5)
axs.plot(x,deformation_force[:,5],label="Monitoring point 6",linewidth=1.5)


                                

axs.set_xlabel('Mchining step', fontsize=20)
axs.set_ylabel("Deformation force(N)", fontsize=20)
#plt.xticks(fontproperties = '宋体', size = 14) #默认字体大小为6
#plt.yticks(fontproperties = '宋体', size = 14)

#plt.xlim(3,21) #设置x轴的范围
axs.set_title('Deformation force',y=-0.15,fontsize=20)

num1=1.5
num3=3
num4=0
num2=0

axs.legend(['Monitoring point 1','Monitoring point 2','Monitoring point 3','Monitoring point 4','Monitoring point 5','Monitoring point 6'],fontsize=16,bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4)

        

