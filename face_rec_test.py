import face_recognition

salah_image = face_recognition.load_image_file("Faces/Abo_Salah.jpg")
salah_face_encoding = face_recognition.face_encodings(salah_image)[0]

ibrahim_image = face_recognition.load_image_file("Faces/Ahmed_Ibrahim.jpg")
ibrahim_face_encoding = face_recognition.face_encodings(ibrahim_image)[0]

ayman_image = face_recognition.load_image_file("Faces/Ayman.jpg")
ayman_face_encoding = face_recognition.face_encodings(ayman_image)[0]

mahmoud_image = face_recognition.load_image_file("Faces/Mahmoud.jpg")
mahmoud_face_encoding = face_recognition.face_encodings(mahmoud_image)[0]

mashhour_image = face_recognition.load_image_file("Faces/Mashhour.jpg")
mashhour_face_encoding = face_recognition.face_encodings(mashhour_image)[0]

shibob_image = face_recognition.load_image_file("Faces/Shibob.jpg")
shibob_face_encoding = face_recognition.face_encodings(shibob_image)[0]


c_image = face_recognition.load_image_file("Faces/Shibob.jpg")
c_face_encoding = face_recognition.face_encodings(c_image)[0]

known_face_encodings = [
    salah_face_encoding,
    ibrahim_face_encoding,
    ayman_face_encoding,
    mahmoud_face_encoding,
    mashhour_face_encoding,
    shibob_face_encoding
]

known_face_names = [
    "Salah",
    "Ahmed Ibrahim",
    "Ayman",
    "Mahmoud",
    "Mashhour",
    "Shibob"
]

matches = face_recognition.compare_faces(known_face_encodings, c_face_encoding)

name = "Unknown"

if True in matches:
	first_match_index = matches.index(True)
	name = known_face_names[first_match_index]
	print(name)