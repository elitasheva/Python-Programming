from lecture_07.loaders.loader import Loader
import yaml


class YAMLLoader(Loader):
    def load_input(self):
        with open(self.filename) as f:
            input_data = yaml.load(f)
            return input_data
