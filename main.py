import glob
from PIL import Image
import sys
import pyocr
import pyocr.builders
#OCRが使用可能かをチェック
tools = pyocr.get_available_tools()
if len(tools) == 0:
    sys.exit(1)
print("1")
#OCRツール名を表示
tool = tools[0]
#OCR対応言語を表示
langs = tool.get_available_languages()
lang = langs[0]
print("1")
afiles = glob.glob("images/*")
filename = afiles
print("1")
     #読み込んだ画像をOCRでテキスト抽出してみる。
try:
    txt = tool.image_to_string(
        Image.open(filename[0]),
        lang="jpn",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    print(txt) 
except:
    print("error")
