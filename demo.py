import tkinter as tk
import pygame
from pygame.locals import *
import numpy as np
from PIL import Image, ImageTk

# 初始化 Pygame
pygame.init()

# 定义 3D 模型渲染函数
def render_3d_model():
    # 创建 Pygame 窗口
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("3D Model Rendering")

    # 简单的 3D 场景示例：绘制一个彩色矩形
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 200))

    # 保存渲染图像
    pygame.image.save(screen, "rendered_image.png")

    # 生成简单的深度图（模拟）
    depth_map = np.random.randint(0, 256, (400, 400), dtype=np.uint8)
    depth_image = Image.fromarray(depth_map)
    depth_image.save("depth_map.png")

    return "rendered_image.png", "depth_map.png"

# 创建 Tkinter 窗口
root = tk.Tk()
root.title("3D Model Rendering and Depth Map")

# 渲染 3D 模型并获取图像和深度图
image_path, depth_map_path = render_3d_model()

# 打开渲染图像和深度图
rendered_image = Image.open(image_path)
depth_map_image = Image.open(depth_map_path)

# 将图像转换为 Tkinter 可用的格式
tk_rendered_image = ImageTk.PhotoImage(rendered_image)
tk_depth_map_image = ImageTk.PhotoImage(depth_map_image)

# 创建两个 Canvas 并显示图像
left_canvas = tk.Canvas(root, width=400, height=400)
left_canvas.pack(side=tk.LEFT)
left_canvas.create_image(0, 0, anchor=tk.NW, image=tk_rendered_image)

right_canvas = tk.Canvas(root, width=400, height=400)
right_canvas.pack(side=tk.RIGHT)
right_canvas.create_image(0, 0, anchor=tk.NW, image=tk_depth_map_image)

# 运行 Tkinter 主循环
root.mainloop()

# 退出 Pygame
pygame.quit()