from DAL.MongoHelper import  DbHelper
import cv2
from bson import ObjectId

db = DbHelper()
# # db.add_suspect(Suspect(203973797,"Tomer","Gliksman",28))
# # db.add_suspect(Suspect(204686422,"Tom","Harel",26))
# s1 = db.get_suspect_by_id(203973797)
# print(s1)
# for s in db.get_all_suspects():
#     print(s)
#images = [ObjectId("5d2e067eac60b5371029ec36"), ObjectId("5d2e0691ac60b5371029ec4b")]
s = db.get_suspect_by_tz(203973797)
s.images = []
s.add_image(ObjectId("5d2e4280232629a27397dc13"))
s.add_image(ObjectId("5d2e4284232629a27397dc16"))
s.add_image(ObjectId("5d2e4287232629a27397dc19"))
s.add_image(ObjectId("5d2e428a232629a27397dc1c"))
s.add_image(ObjectId("5d2e4293232629a27397dc28"))
s.add_image(ObjectId("5d2e4296232629a27397dc2b"))
s.add_image(ObjectId("5d2e4298232629a27397dc2e"))
s.add_image(ObjectId("5d2e428c232629a27397dc1f"))
s.add_image(ObjectId("5d2e428e232629a27397dc22"))
s.add_image(ObjectId("5d2e4291232629a27397dc25"))

db.update_suspect(s)
image = db.get_one_image(s.images[0])
print(image.file_id)
while(True):
    cv2.imshow('frame', image.get_data())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()