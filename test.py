import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QDialog
from PyQt5.QtGui import QPixmap

class ImageSelectionDialog(QDialog):
    def __init__(self, folder_path):
        super().__init__()

        self.folder_path = folder_path
        self.image_labels = []

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        select_button = QPushButton('Select Folder', self)
        select_button.clicked.connect(self.select_folder)
        layout.addWidget(select_button)

        self.setLayout(layout)

        self.load_images()

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "")
        if folder_path:
            self.folder_path = folder_path
            self.load_images()

    def load_images(self):
        # Clear existing labels
        for label in self.image_labels:
            label.setParent(None)
            label.deleteLater()

        self.image_labels = []

        # Scan folder for image files
        image_extensions = ['png', 'jpg', 'jpeg', 'bmp', 'gif']
        image_files = [f for f in os.listdir(self.folder_path) if f.lower().endswith(tuple(image_extensions))]

        # Create labels for each image
        for image_file in image_files:
            image_path = os.path.join(self.folder_path, image_file)
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                label = QLabel(self)
                label.setPixmap(pixmap)
                self.image_labels.append(label)
                self.layout().addWidget(label)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        open_dialog_button = QPushButton('Open Image Selection Dialog', self)
        open_dialog_button.clicked.connect(self.open_image_selection_dialog)
        layout.addWidget(open_dialog_button)

        self.setLayout(layout)

    def open_image_selection_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "")
        if folder_path:
            image_dialog = ImageSelectionDialog(folder_path)
            image_dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
