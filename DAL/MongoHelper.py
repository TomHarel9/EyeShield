from pymongo import MongoClient
import gridfs
from Config import  eye_shield_conf as conf
from Utils.singleton import Singleton
from BI.Suspect import Suspect
from BI.Case import Case
from BI.Image import Image
import cv2
import numpy as np

class DbHelper(Singleton):

    def __init__(self):
        self.client = MongoClient(conf.DB_CONNECTION_STRING)
        self.db = self.client.eyeshield
        self.fs = gridfs.GridFS(self.db)

    def add_suspect(self, suspect):
        return self.db.suspects.insert_one(suspect.asdict())

    def add_case(self, case):
        return self.db.cases.insert_one(case.asdict())

    def save_image(self, image):
        data = cv2.imencode(".png", image.get_data())[1].tostring()
        file_id = self.fs.put(data, location=image.get_location(), timestamp=image.get_timestamp())
        image.set_file_id(file_id)
        return file_id

    def get_all_suspects(self):
        suspects_list = []
        for suspect in self.db.suspects.find():
            suspects_list.append(Suspect(suspect['tz'], suspect['first_name'], suspect['last_name'], suspect['age'],
                                         suspect['images'], suspect['cases']))
        return suspects_list

    def get_all_cases(self):
        cases_list = []
        for case in self.db.cases.find():
            cases_list.append(Case(case['number_id'], case['name'], case['suspects'], case['images']))
        return cases_list

    def get_all_images(self):
        images_list = []
        for im in self.fs.find():
            data = cv2.imdecode(np.fromstring(im.read(), dtype=np.uint8), 1)
            images_list.append(Image(data, im.location, im.timestamp, im._id))
        return images_list

    def get_images(self, images_ids):
        images_list = []
        for file_id in images_ids:
            if self.fs.exists(file_id):
                im = self.fs.get(file_id)
                data = cv2.imdecode(np.fromstring(im.read(), dtype=np.uint8), 1)
                images_list.append(Image(data, im.location, im.timestamp, im._id))
            else:
                print("file not exist")
        return images_list

    def get_one_image(self, file_id):

        if self.fs.exists(file_id):
            im = self.fs.get(file_id)
            data = cv2.imdecode(np.fromstring(im.read(), dtype=np.uint8), 1)
            return Image(data, im.location, im.timestamp, im._id)
        return None


    def get_suspect_by_tz(self, tz):
        q = {'tz': tz}
        suspect = self.db.suspects.find_one(q)
        if suspect is not None:
            return Suspect(suspect['tz'], suspect['first_name'], suspect['last_name'], suspect['age'], suspect['images'], suspect['cases'])

    def get_case_by_id(self, number_id):
        q = {'number_id': number_id}
        case = self.db.cases.find_one(q)
        return Case(case['number_id'], case['name'], case['suspects'], case['images'])

    def update_suspect(self, suspect):
        query = {'tz': suspect.tz}
        newvalues = {"$set": suspect.asdict()}
        self.db.suspects.update_one(query, newvalues,upsert=False)

