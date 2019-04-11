	#Image AI library is imported here
	from imageai.Detection import ObjectDetection
	#os and cv2 libraries are imported here for image editing with text
	import os
	import cv2
	#PIL library is imported here for image editing
	from PIL import Image
	from PIL import ImageFont
	from PIL import ImageDraw
	#Execution is defined
	execution_path = os.getcwd ()
	#Input Image Name is defined
	image_name = "Ryerson-University-Street-View.jpg"
	#Output Image Name is defined
	result_image_name = "Ryerson-University-Street-View_Detected_Objects.jpg"
	#Object Detection Class is initialized
	detector = ObjectDetection ()
	detector.setModelTypeAsYOLOv3 ()
	detector.setModelPath (os.path.join (execution_path, "yolo.h5"))
	detector.loadModel (detection_speed = "normal")
	#Object Detection is done with an array as output
	returned_image, detections = detector.detectObjectsFromImage (input_image =
	os.path.
	join
	(execution_path,
	image_name),
	output_type =
	"array",
	minimum_percentage_probability
	=
	30,
	display_percentage_probability
	=
	False,
	display_object_name
	= False)
	#The original image is imported
	img = cv2.imread (image_name, -1)
	#For loop initiated for each detected object to draw the rectangles
	for eachObject
	in detections:
	#Detection Specifications Are printed
	print (eachObject["name"], " : ", eachObject["percentage_probability"],
	" : ", eachObject["box_points"])
	detected_box_points =
	eachObject["box_points"]
	#Detection Box Points Values Are Assinged
	x1 = detected_box_points[0]
	y1 = detected_box_points[1]
	x2 = detected_box_points[2]
	y2 = detected_box_points[3]
	#Length and Width Calculation
	x_dif = abs (x2 - x1)
	y_dif = abs (y2 - y1)
	print (" Length : ", str (x_dif), " Width : ", str (y_dif))
	#Rectangle Coloring Rules
	if x_dif
	>y_dif:
	cv2.rectangle (img, (x1, y1), (x2, y2), (0, 128, 0), 2)
	else
	:
	cv2.rectangle (img, (x1, y1), (x2, y2), (0, 0, 255), 2)
	#Rectangle Coloring Finished
	print ("---------------------------------------------------")
	#For loop initiated for each detected object to print the names
	for eachObject
	in detections:
	detected_box_points = eachObject["box_points"]
	#Print positin is defined as the top left corner of the box
	x1 = detected_box_points[0]
	y1 = detected_box_points[1]
	#Text specifications are assigned with black color as the background
	font = cv2.FONT_HERSHEY_DUPLEX
	bottomLeftCornerOfText = (x1, y1)
	fontScale = 0.62
	fontColor = (0, 0, 0)
	lineType = 3
	cv2.putText (img, eachObject["name"],
	bottomLeftCornerOfText,
	font,
	fontScale,
	fontColor,
	lineType)
	#Text specifications are assigned with white color as foreground
	font = cv2.FONT_HERSHEY_DUPLEX
	bottomLeftCornerOfText = (x1, y1)
	fontScale = 0.6
	fontColor = (255, 255, 255)
	lineType = 2
	#Text print on the image
	cv2.putText (img, eachObject["name"],
	bottomLeftCornerOfText,
	font,
	fontScale,
	fontColor,
	lineType)
	#Resulted image is shown to check the accuracy by the operator
	cv2.imshow ('Resulted Out Put Detection', img)
	#Waiting for the next step key
	k = cv2.waitKey (0)
	if k
	== 27:
	#wait for ESC key to exit
	cv2.destroyAllWindows ()
	elif k == ord ('s'):
	#wait for 's' key to save and exit
	cv2.imwrite (result_image_name, img)
	cv2.destroyAllWindows ()
