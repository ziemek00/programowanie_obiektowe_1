from model import Model
from view import View
from controller import Controller

def main():
    model = Model()
    view = View()
    controller = Controller(view, model)
    view.set_controller(controller)
    controller.start()

if __name__ == "__main__":
    main()
