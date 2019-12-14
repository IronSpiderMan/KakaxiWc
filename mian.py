from wordcloud import WordCloud, ImageColorGenerator
import imageio, jieba

# 读取文本文件
f = open('kkx.txt', encoding='utf-8')
txt = f.read()
word = jieba.cut(txt)
words = " ".join(word)

# 读取图片
mk = imageio.imread('kkx.png')
# 获取图片颜色产生器
image_color = ImageColorGenerator(mk)

# 获取词云对象
wc = WordCloud(
    width=600,
    height=800,
    background_color='white',
    font_path='msyh.ttc',
    mask=mk,
    contour_width=1,
    contour_color='black'
)

# 根据文字生成词云
wc.generate(words)

# 根据图片颜色重绘词云
rwc = wc.recolor(color_func=image_color)

# 保存词云文件
rwc.to_file("rwc.png")














# import sys
# import pygame
#
# # 屏幕大小
# size = (800, 600)
# # 背景颜色
# bg_color = (230, 230, 230)
#
#
# def run_game():
#     # 初始化游戏
#     pygame.init()
#     # 获取屏幕对象
#     screen = pygame.display.set_mode(size)
#     # 设置标题
#     pygame.display.set_caption("坦克大战")
#     while True:
#         # 监听事件
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         # 重绘屏幕
#         screen.fill(bg_color)
#         pygame.display.flip()
#
# run_game()