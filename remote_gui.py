from classes import Television

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_channel_images(folder_name="Channels"):
    images = []
    for i in range(Television.MAX_CHANNEL + 1):
        folder_and_file_name = folder_name + f"/channel{i}.png"
        images.append(QPixmap(folder_and_file_name).scaledToWidth(200))

    return images


class TVRemoteGUI(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remote")
        self.resize(300, 400)

        self.muted = False
        self.curr_channel = Television.MIN_CHANNEL
        self.curr_volume = Television.MIN_VOLUME
        self.channel_images = load_channel_images()
        self.tv_instance = Television()

        # Make the GUI in the setupUI method
        self.setupUI()

    def setupUI(self):
        self.pic = QLabel()
        self.pic.setPixmap(self.channel_images[0])
        self.pic.setAlignment(Qt.AlignCenter)

        # create a vertical layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.pic)
        vbox.addStretch()

        # the volume label
        volume_label = QLabel("Volume")
        volume_label.setAlignment(Qt.AlignCenter)

        vbox.addWidget(volume_label)
        vbox.addStretch()

        # create a central widget for QMainWindow and assign the layout
        frame = QWidget()
        frame.setLayout(vbox)
        self.setCentralWidget(frame)

        exitAction = QAction("Exit", self)
        exitAction.triggered.connect(self.close)

        self.slider = QSlider(Qt.Horizontal, frame)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(1)
        # self.slider.valueChanged[int].connect(self.onSliderChange)
        self.slider.setMinimum(Television.MIN_VOLUME)
        self.slider.setMaximum(Television.MAX_VOLUME)

        vbox.addWidget(self.slider)
        vbox.addStretch()

        self.power_btn = QPushButton("Power")
        self.power_btn.clicked.connect(self.onPowerClick)

        vbox.addWidget(self.power_btn)
        vbox.addStretch()

        label = QLabel("Worked hard to create this thing")
        label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(label)
        vbox.addStretch()

        vbox2 = QVBoxLayout()
        label = QLabel("Channel")
        label.setAlignment(Qt.AlignCenter)
        vbox2.addWidget(label)
        vbox2.addStretch()

        self.channel_up_btn = QPushButton("▲")
        self.channel_up_btn.clicked.connect(lambda: self.onChannelChange(up=True))
        # self.channel_up_btn.setAlignment(Qt.AlignCenter)
        vbox2.addWidget(self.channel_up_btn)
        vbox2.addStretch()

        self.channel_down_btn = QPushButton("▼")
        self.channel_down_btn.clicked.connect(lambda: self.onChannelChange(up=False))
        # self.channel_down_btn.setAlignment(Qt.AlignCenter)
        vbox2.addWidget(self.channel_down_btn)
        vbox2.addStretch()

        vbox3 = QVBoxLayout()
        label = QLabel("Volume")
        label.setAlignment(Qt.AlignCenter)
        vbox3.addWidget(label)
        vbox3.addStretch()

        self.volume_up_btn = QPushButton("+")
        self.volume_up_btn.clicked.connect(lambda: self.onVolumeChange(up=True))
        # self.volume_up_btn.setAlignment(Qt.AlignCenter)
        vbox3.addWidget(self.volume_up_btn)
        vbox3.addStretch()

        self.volume_down_btn = QPushButton("-")
        self.volume_down_btn.clicked.connect(lambda: self.onVolumeChange(up=False))
        # self.volume_down_btn.setAlignment(Qt.AlignCenter)
        vbox3.addWidget(self.volume_down_btn)
        vbox3.addStretch()
        vbox3.setAlignment(Qt.AlignCenter)
        vbox2.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox2)
        hbox.addStretch()

        self.mute_btn = QPushButton("Mute")
        self.mute_btn.clicked.connect(self.onMute)
        hbox.addWidget(self.mute_btn)
        hbox.addStretch()

        hbox.addLayout(vbox3)
        hbox.addStretch()
        hbox.setAlignment(Qt.AlignCenter)

        vbox.addLayout(hbox)

    def onPowerClick(self):
        if self.tv_instance.get_tv_status():
            self.pic.setPixmap(self.channel_images[0])

        else:
            self.pic.setPixmap(self.channel_images[self.curr_channel + 1])

        self.tv_instance.power()
        print("Current TV status:", self.tv_instance.get_tv_status())

        # self.pic.setAlignment(Qt.AlignCenter)
        QApplication.processEvents()

    def onVolumeChange(self, up):
        if up:
            curr_volume = self.tv_instance.volume_up()
        else:
            curr_volume = self.tv_instance.volume_down()

        self.slider.setValue(curr_volume)
        QApplication.processEvents()

    def onChannelChange(self, up):
        if up:
            self.curr_channel = self.tv_instance.channel_up()

        else:
            self.curr_channel = self.tv_instance.channel_down()

        print("Curr channel:", self.curr_channel)
        self.pic.setPixmap(self.channel_images[self.curr_channel + 1])

        QApplication.processEvents()

    def onMute(self):
        if self.muted == False:
            self.volume_down_btn.setDisabled(True)
            self.volume_up_btn.setDisabled(True)
            self.muted = True

        else:
            self.volume_down_btn.setDisabled(False)
            self.volume_up_btn.setDisabled(False)
            self.muted = False

        QApplication.processEvents()
