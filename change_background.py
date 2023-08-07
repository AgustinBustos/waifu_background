import shutil
import random
import os

dirr='backgrounds'
images=os.listdir(fr"C:\Users\TheQwertyPhoenix\Documents\agusssd\DONOTENTER\{dirr}")

print()

imageq=len(images)-1


# original = fr"C:\Users\TheQwertyPhoenix\Documents\agusssd\DONOTENTER\backgrounds\a{random.randint(0,imageq)}.png"
original = fr"C:\Users\TheQwertyPhoenix\Documents\agusssd\DONOTENTER\{dirr}\{images[random.randint(0,imageq)]}"
target = r'C:\Users\TheQwertyPhoenix\Documents\agusssd\DONOTENTER\selected\selected.png'
shutil.copyfile(original, target)

