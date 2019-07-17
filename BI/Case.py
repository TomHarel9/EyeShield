
class Case:

    def __init__(self, number_id, name, suspects=[], images=[]):
        self.number_id = number_id
        self.name = name
        self.images = images
        self.suspects = suspects

    def asdict(self):
        return {'number_id': self.number_id, 'name': self.name, 'images': self.images, 'suspects': self.suspects}

    def add_image(self, image_id):
        self.images.append(image_id)

    def add_suspect(self, suspect_id):
        self.cases.append(suspect_id)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)