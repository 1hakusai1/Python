from PIL import Image
import numpy as np

def dotting(input_img,dotsize):
    width,height=input_img.size
    output_img=Image.new("RGB",(width,height))
    for y in range(0,height,dotsize):
        for x in range(0,width,dotsize):
            for j in range(dotsize):
                for i in range(dotsize):
                    if x+i<width and y+j<height:
                        output_img.putpixel((x+i,y+j),input_img.getpixel((x,y)))
    return output_img

input_img=Image.open("input_image.jpg")
print("1ドットの大きさを入力してください。")
dotsize=int(input())
print("作成中...")
output_img=dotting(input_img,dotsize)
output_img.save("output_image.jpg")
print("完了しました")
