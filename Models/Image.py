
class Image:

    def __init__(self, data, location, timestamp, file_id=None, tagged=False):
        self.data = data
        self.location = location
        self.timestamp = timestamp
        self.file_id = file_id
        self.tagged = tagged
        # self.suspects_list = []

    # def add_suspect(self, tz):
    #     if tz not in self.suspects_list:
    #         self.suspects_list.append(tz)

    def get_data(self):
        return self.data

    def get_location(self):
        return self.location

    def get_timestamp(self):
        return self.timestamp

    def set_file_id(self, file_id):
        if not self.file_id:
            self.file_id = file_id

    def isTagged(self):
        return self.tagged

    def tag(self):
        self.tagged = True

    # def get_suspects(self):
    #     return self.suspects_list
