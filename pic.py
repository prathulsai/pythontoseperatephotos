#import face_recognition
from shutil import copyfile
import face_recognition

# Create an encoding of my facial features that can be compared to other faces
picture_of_me = face_recognition.load_image_file("pic.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# Iterate through all the 10,460 pictures
for i in range(2, 1880):
    # Construct the picture name and print it
    file_name = "1 ("+str(i)+")" + ".jpg"
    print(file_name)

    # Load this picture
    new_picture = face_recognition.load_image_file(file_name)

    # Iterate through every face detected in the new picture
    for face_encoding in face_recognition.face_encodings(new_picture):

        # Run the algorithm of face comaprison for the detected face, with 0.5 tolerance
        results = face_recognition.compare_faces([my_face_encoding], face_encoding, 0.4)

        # Save the image to a seperate folder if there is a match
        if results[0] == True:
            copyfile(file_name, "/media/prathul/9240FE7C40FE667F/compress/home/" + file_name)
	    print(" copied !")
