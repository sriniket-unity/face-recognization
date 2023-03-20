import face_recognition

# Load the two images
image1 = face_recognition.load_image_file("D:\scripts\python\face rec\download.jpg")
image2 = face_recognition.load_image_file("D:\scripts\python\face rec\Elon_Musk_(3017880307).jpg")

# Find the face locations and encodings in each image
face_locations_1 = face_recognition.face_locations(image1)
face_encodings_1 = face_recognition.face_encodings(image1, face_locations_1)
face_locations_2 = face_recognition.face_locations(image2)
face_encodings_2 = face_recognition.face_encodings(image2, face_locations_2)

# Compare the face encodings and check if they match
if len(face_encodings_1) == 0 or len(face_encodings_2) == 0:
    print("No faces found in one of the images.")
else:
    match_results = face_recognition.compare_faces(face_encodings_1, face_encodings_2)
    if True in match_results:
        print("The two faces are a match!")
    else:
        print("The two faces do not match.")
