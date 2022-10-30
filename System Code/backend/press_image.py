from PIL import Image
import os

#获取文件夹里面的图片
path=r'D:\newUber\flask\sg_route_map_background.png'
# print(path_list)
#循环图片路径，依次对图片进行压缩

im = Image.open(path)
(x, y) = im.size  # 读取图片尺寸（像素）
x_1 = 800  # 定义缩小后的标准宽度
y_1 = int(y * x_1 / x)  # 计算缩小后的高度
out = im.resize((x_1, y_1), Image.ANTIALIAS)  # 改变尺寸，保持图片高品质
#判断图片的通道模式，若图片在RGBA模式下，需先将其转变为RGB模式
if out.mode=='RGBA':
    #转化为rgb格式
    out=out.convert('RGB')
    #最后保存为jpg格式的图片，这里因为图片本身为jpg所以后缀不更改
out.save('sgmap_small.png')
