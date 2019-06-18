import face_recognition
from PIL import Image, ImageDraw, ImageFont
from os import walk

def get_suspects_info(path):
    suspects_encodings = []
    suspects_names = []
    for x in walk(path):
        for i in x[2]:
            suspect_img = face_recognition.load_image_file(path + "/" + i)
            suspect_img_encoding = face_recognition.face_encodings(suspect_img)[0]
            suspects_encodings.append(suspect_img_encoding)
            suspects_names.append(i.split(".")[0])
    return suspects_encodings, suspects_names

def find_match(unknown_path):
    unknown = face_recognition.load_image_file(unknown_path)
    unknown_face_coordinates = face_recognition.face_locations(unknown)
    unknown_encoding = face_recognition.face_encodings(unknown, unknown_face_coordinates)

    suspects_encodings, suspects_names = get_suspects_info('../images/suspects')

    pil_img = Image.fromarray(unknown)
    draw = ImageDraw.Draw(pil_img)
    for (top, right, bottom, left), face_encoding in zip(unknown_face_coordinates, unknown_encoding):
        matches = face_recognition.compare_faces(suspects_encodings, face_encoding, tolerance=0.52)

        name = "???"

        if True in matches:
            match_index = matches.index(True)
            name = suspects_names[match_index]

        draw.rectangle(((top, left), (right, bottom)), outline=(0, 0, 0))

        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0)
                       , outline=(0, 0, 0))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255),
                  font=ImageFont.truetype("arial.ttf", 18))
    del draw


    pil_img.show()


#
# path = '../images/buffer/Tom&Yoav&Roi&Sagi&Hanny.jpg'
#
# find_match(path)


