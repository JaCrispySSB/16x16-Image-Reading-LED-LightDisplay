import time
import numpy
import board
import neopixel
from PIL import Image
import sys
import os

folderPath = '/home/Ethan.Ahlstrand/Desktop/16x16Art'
print(folderPath)

#set up a loop so iteration is continuous
loops = 0
while loops < 10000:

    # Iterate through files in the folder
    for file in os.listdir(folderPath):
        filePath = os.path.join(folderPath, file)
        print(file)
        
    #begin LED Process
        img = Image.open(filePath)
        img = img.convert("RGB")
        pix = img.load()
        print(img.size)# Get the width and hight of the image for iterating over
        imgX = img.size[0]
        imgY = img.size[1]
        brightness = 0

        pixelSize = img.size[0] / 16
        pixelSize = int(pixelSize)
        print(pixelSize)

        pixelData = list(img.getdata())


        print(len(pixelData))
        allPixels = []
        y = 0
        x = 0

        print(sys.maxsize)
             
        print(allPixels)
             
        pixels = neopixel.NeoPixel(board.D18, 256, brightness=0.1)

        x=0
        i = 1
        totalRGB = [0, 0, 0]
        finalRGB = []


        for RGB in pixelData:
            if i == pixelSize:
                totalRGB[0] = int((totalRGB[0] + RGB[0]) / pixelSize)
                totalRGB[1] = int((totalRGB[1] + RGB[1]) / pixelSize)
                totalRGB[2] = int((totalRGB[2] + RGB[2]) / pixelSize)
                finalRGB.append(totalRGB)
                i = 1
                totalRGB = [0, 0, 0]
            else:
                totalRGB[0] = totalRGB[0] + RGB[0]
                totalRGB[1] = totalRGB[1] + RGB[1]
                totalRGB[2] = totalRGB[2] + RGB[2]
                i = i + 1
                
                
        newRGB = []
        totalRGB = [0, 0, 0]
        ii = 1


        for h in range(16):
            for j in range(16):  # Loop 16 times
                newArray = []
                for i in range(pixelSize):  # Loop for 75 iterations
                    index = (i * 16) + (h*imgX) + j # Calculate the index to select the item from original_array
                    if index < len(finalRGB):
                        item = finalRGB[index]
                        newArray.append(item)
                for RGB in newArray:
                    if ii == pixelSize:
                        totalRGB[0] = int((totalRGB[0] + RGB[0]) / pixelSize)
                        totalRGB[1] = int((totalRGB[1] + RGB[1]) / pixelSize)
                        totalRGB[2] = int((totalRGB[2] + RGB[2]) / pixelSize)
                        newRGB.append(totalRGB)
                        ii = 1
                        totalRGB = [0, 0, 0]
                    else:
                        totalRGB[0] = totalRGB[0] + RGB[0]
                        totalRGB[1] = totalRGB[1] + RGB[1]
                        totalRGB[2] = totalRGB[2] + RGB[2]
                        ii = ii + 1

        finalArray = []

        for i, value in enumerate(newRGB):
            finalArray.append(value)
            
            if (i + 1) % 16 == 0:  # Check if we've added 16 values
                if (i // 16) % 2 == 0:  # Check if it's an odd group
                    finalArray[-16:] = reversed(finalArray[-16:])

        print(finalArray)
        print(newRGB)
        i = 0
        print(len(newRGB))
        print(len(pixels))
        for RGB in finalArray:
            if i > 256:
                exit
            pixels[i] = finalArray[i]
            i = i + 1
            
        time.sleep(5)
#add to loop so we don't run forever!
    loops = loops + 1