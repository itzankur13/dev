import Image

im = Image.open("C:\\MyDocs\\dev\\PixelShmixel\\kimmiller.jpg")
seq = im.getdata()

imSize = im.size
imX = imSize[0]
imY = imSize[1]

#start
f = file("C:\\MyDocs\\dev\\PixelShmixel\\kim.htm","w")
imgSeqLen = len(seq)
pixel = 0

strAppInfo = "<sup>Image generated by PixelShmixel, a Python script by Arlo Emerson, Lante Corp. 2002</sup><br>"

strTableHeader = "<table cellpadding=0 border=0 cellspacing=0"
strTableHeader += " width="
strTableHeader += str(imX)
strTableHeader += " height="
strTableHeader += str(imY)
strTableHeader += ">"
		
myList = []
intRow = 0
intColumn = 0
blnStartRow = 1

myList.append(strTableHeader)

while pixel < imgSeqLen:
	intColumn = intColumn + 1
	# start row
	if blnStartRow == 1:
		myList.append("<tr>")
		blnStartRow = 0
	# append cell
	myList.append("<td ")
	myList.append("bgcolor='rgb")
	# convert rgb to hex 
	myList.append(str(seq[pixel]))
	myList.append("'></td>")
	# close row
	if intRow < imY:
		if intColumn == imX:
			intColumn = 0 #reset column counter
			myList.append("</tr>")
			blnStartRow = 1
			intRow = intRow + 1
	pixel = pixel + 1
myList.append("</table>")
myList.append(strAppInfo)

f.writelines(myList)
 		
