

class Suspect:

    def __init__(self, tz, first_name, last_name, age, images=[], cases=[]):
        self.tz = tz
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.images = images
        self.cases = cases

    def asdict(self):
        return {'tz': self.tz, 'first_name': self.first_name, 'last_name': self.last_name,
                'age': self.age, 'images': self.images, 'cases': self.cases}

    def add_image(self, image_id):
        self.images.append(image_id)

    def add_case(self, case_id):
        self.cases.append(case_id)

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_images(self):
        return self.images

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
