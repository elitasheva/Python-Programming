from lecture_07.loaders.loader import Loader
import json


class JSONLoader(Loader):
    def load_input(self):
        with open(self.filename, encoding="utf-8") as f:
            input_data = json.load(f)
            return input_data['params']
