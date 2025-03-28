# Ngô Thu Thảo 20216960
import sys
from PyQt5.QtWidgets import QApplication
from menu import Menu


def main():
    app = QApplication(sys.argv)
    main_menu = Menu()
    main_menu.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
