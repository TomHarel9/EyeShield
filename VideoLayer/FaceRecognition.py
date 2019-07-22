import face_recognition
import cv2
#   from PIL import Image, ImageDraw, ImageFont
from DAL.MongoHelper import DbHelper


def get_known_suspects_info():

    known_face_encodings = []
    known_face_names = []
    db = DbHelper()

    for suspect in db.get_all_suspects():
        if suspect.images:
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            suspect_rgb_img = db.get_one_image(suspect.images[0]).get_data()[:, :, ::-1]
            suspect_img_encoding = face_recognition.face_encodings(suspect_rgb_img)[0]
            known_face_encodings.append(suspect_img_encoding)
            known_face_names.append(suspect.tz)

    return known_face_encodings, known_face_names


def find_match(frame):
    face_names = []
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    unknown_face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    known_face_encodings, known_face_names = get_known_suspects_info()

    # pil_img = Image.fromarray(frame)
    # draw = ImageDraw.Draw(pil_img)
    for (top, right, bottom, left), face_encoding in zip(face_locations, unknown_face_encodings):

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.52)

        # name = "unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]
            face_names.append(name)

        # draw.rectangle(((top, left), (right, bottom)), outline=(0, 0, 0))
        #
        # text_width, text_height = draw.textsize(name)
        # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0)
        #                , outline=(0, 0, 0))
        # draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255),
        #           font=ImageFont.truetype("arial.ttf", 18))
    # del draw
    return face_names


