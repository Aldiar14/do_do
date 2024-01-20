import os
from PyQt5. QtWidgets import(
    QApplication, QWidget,
    QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)
app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Wasy Editor')
ld_image = QLabel('Картинка')
btn_dir = QPushButton('Папка')
lw_files = QListWidget()

btn_left = QPushButton('Лево')
btn_right = QPushButton('право')
btn_flip = QPushButton('зеркало')
btn_sharp = QPushButton('резкость')
btn_ddw = QPushButton('Ч/Б')

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(ld_image, 95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)


row.addLayout(col1,20)
row.addLayout(col2, 80)
win.setLayout(row)

win.show()

workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extensions = ['.jpg','.jpeg','.png','.gif','.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir),extensions)

    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'
    def loodImage(self,dir, filename):
        '''при загрузке запоминаем путь и имя файла'''
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir,filename)
        self.image.open(image_path)
    def showImage(self,path):
        ld_image.hide()
        pixmapimage = QPixmap(path)
        w,h =ld_image.width(), ld_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        ld_image.setPixmap(pixmapimage)
        ld_image.show()
workimage = ImageProcessor()

def showChosenImage():
    if lw_file.currentRow() >=0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)
lw_files.currentRowChanged.connect(showChosenImage)


app.exec()










































