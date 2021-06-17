class PCComponet:
    def __init__(component, RGBled, brand):
        component.led = RGBled
        component.brand = brand

    def PC(component, x):
        print("it's a pc")

class MotherBoard(PCComponet):
    def PCI(component, x):
        print(x+3)
        super().PC(1)
   

mother_board = MotherBoard(False, "gigabyte")

print(mother_board.brand)
mother_board.PCI(6)
mother_board.PC(0)