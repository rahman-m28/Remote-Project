from remote_gui import *

def main():
    app = QApplication([])

    # Create our custom application
    window = TVRemoteGUI()

    # And show it
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
