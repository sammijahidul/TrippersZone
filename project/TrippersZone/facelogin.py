import face_recognition
import cv2

user_pic = face_recognition.load_image_file("user_img.jpg")
face_encoding = face_recognition.face_encodings(user_pic)[0]

# face_encoding now contains a universal 'encoding' of facial features that can be compared to any other
# picture of a face

unknown_picture = face_recognition.load_image_file("unknown.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")