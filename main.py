from gui import MainGUI
from pwds_serializer import PWDS_Serializer
from pwds_gui import PWDS_GUI


def main():
    gui = PWDS_GUI()
    serializer = PWDS_Serializer(gui)
    gui.set_serializer(serializer)
    gui.display()
    #test.mainloop()


if __name__ == '__main__':
    main()