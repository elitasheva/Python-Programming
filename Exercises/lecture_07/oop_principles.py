from turtle import Turtle, done as turtle_done
from lecture_07.figures.circle import Circle
from lecture_07.figures.square import Square
from lecture_07.figures.triangle import Triangle
from lecture_07.figures.polygon import Polygon
from lecture_07.loaders.json import JSONLoader
from lecture_07.loaders.yaml import YAMLLoader
import importlib
import os
YAML_FILE = "./resources/figures.yaml"
JSON_FILE = "./resources/figures.json"
FIGURES_PATH = "figures."
LOADERS_PATH = "loaders."


def main():
    figures = {'circle': Circle,
               'square': Square,
               'triangle': Triangle,
               'polygon': Polygon}

    loaders = {'yaml': YAMLLoader,
               'json': JSONLoader}

    params = load_input_data(YAML_FILE, loaders)
    draw_figures(params, figures)


def load_input_data(filename, loaders):
    # file, extension = os.path.splitext(filename)
    # loader_module = importlib.import_module(LOADERS_PATH + extension[1:], "lecture_07")
    # loader_name = extension[1:].upper() + "Loader"
    # current_class_loader = getattr(loader_module, loader_name)
    # instance_loader = current_class_loader(filename)
    # return instance_loader.load_input()

    file, extension = os.path.splitext(filename)
    class_loader = loaders[extension[1:]]
    instance_loader = class_loader(filename)
    return instance_loader.load_input()


def draw_figures(params, figures):
    # t = Turtle()
    # for param in params:
    #     figure_type = param.pop('type')
    #     figure_module = importlib.import_module(FIGURES_PATH + figure_type, "lecture_07")
    #     figure_name = figure_type[0].upper() + figure_type[1:]
    #     current_class_figure = getattr(figure_module, figure_name)
    #     instance_figure = current_class_figure(**param)
    #     instance_figure.draw(t)
    # turtle_done()

    t = Turtle()
    for param in params:
        figure_type = param.pop('type')
        current_class_figure = figures[figure_type]
        instance_figure = current_class_figure(**param)
        instance_figure.draw(t)
    turtle_done()


if __name__ == '__main__':
    main()

