# encoding=utf-8

import os
import nibabel as nib
import matplotlib.pyplot as plt

# 3D图像路径（nii.gz文件路径）
nii_file_path = '/Users/shirley/Downloads/FLARE22Train/images/FLARE22_Tr_0001_0000.nii.gz'

# 保存2D切片的文件夹
output_dir = 'extracted_slices'
os.makedirs(output_dir, exist_ok=True)

# 加载NIfTI文件
try:
    nii_img = nib.load(nii_file_path)
    data = nii_img.get_fdata()
except Exception as e:
    print(f"Error loading NIfTI file: {e}")
    exit()

# 选择一个切片（请根据您的数据实际情况调整轴和索引）
depth_index = data.shape[2] // 2
slice_data = data[:, :, depth_index]

# 归一化数据以用于图像保存（将像素值缩放到0-1范围，以便Matplotlib正确显示和保存）
if slice_data.max() != slice_data.min():
    slice_data = (slice_data - slice_data.min()) / (slice_data.max() - slice_data.min())

# 保存为PNG文件
output_png_path = os.path.join(output_dir, f'slice_z_{depth_index}.png')

# 使用灰度图colormap保存
plt.imsave(output_png_path, slice_data, cmap='gray')

print(f"Successfully extracted slice and saved to: {output_png_path}")



