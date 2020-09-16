# mosaic-picture
Generates a mosaic picture

### How it works:
1) The database of picture is analyzed. THe average color is extracted. Pictures are resized and stored in a dictionnary
2) The picture given as input is resized using Opencv.
3) For each tile in the input image, the average color is calculated
4) The best fit in the picture database is found (the one minimizing the Euclidian distance in the color space)
5) The best tile is included at the right position in the output picture
6) Then the result is saved in the `./outputs` folder

### Requirements:
- Numpy
- Matplotlib
- OpenCV

### Execution:
run `python photomosaic.py [path_picture] [path_database] [param]`  
**path_picture**: path of the picture to transform  (ex ./pictures/rome.jpg)  
**path_database**: path of the folder containing your database of picture (ex ./database)  
**param**: optional, size in pixel of each square tile. Default 25  
example : 'python photomosaic.py ./pictures/taj-mahal.jpg ./database 15'

### Result:

![alt text](https://github.com/Haha89/mosaic-picture/blob/master/pictures/rome.jpg "Input Picture")
![alt text](https://github.com/Haha89/mosaic-picture/blob/master/outputs/rome.jpg "Mosaic generated")

### Next steps:
- Improve the definition of best fit
