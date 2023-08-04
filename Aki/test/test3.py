import os
import random

# 获取当前文件的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 构建相对路径
background_dir = os.path.join(current_dir, '..', '..', 'pic', 'background')

# 使用os.listdir获取背景图片文件夹中的所有图片文件名
background_files = os.listdir(background_dir)

# 使用random.choice随机选择一张背景图片
background_image_filename = random.choice(background_files)

# 构建完整的背景图片路径
background_image_path = os.path.join(background_dir, background_image_filename)
