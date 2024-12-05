# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import os
import threading
import os,django,time
import pandas
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

import subprocess
   
        
from window1 import Ui_master
class window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_master()
        self.form.setupUi(self)
        

        
        
        
        
        

        self.form.pushButton_help.clicked.connect(self.helper)
        self.form.lineEdit_command.returnPressed.connect(self.execute)
        
        self.form.pushButton_show_databse.clicked.connect(self.database_show)
        self.form.pushButton_runserver.clicked.connect(self.abhi)
        self.form.pushButton_clear.clicked.connect(self.clear)
        self.form.pushButton_open_site.clicked.connect(lambda: self.open_site(''))
        self.form.pushButton_admin.clicked.connect(lambda: self.open_site('/admin'))
        self.form.pushButton_execute.clicked.connect(self.execute)
        self.form.pushButton_open_shell.clicked.connect(self.shell)
        self.form.pushButton_check.clicked.connect(self.check)
        self.form.pushButton_make_migration.clicked.connect(self.make_migration)
        self.form.pushButton_apply_migration.clicked.connect(self.apply_migration)
        self.form.pushButton_show_migration.clicked.connect(self.show_migration)
        self.form.pushButton_flush_databse.clicked.connect(self.flush_databse)
        
        
        
        self.form.actioncheck.triggered.connect(lambda: self.on_action_triggered(self.form.actioncheck))
        self.form.actioncompilemessages.triggered.connect(lambda: self.on_action_triggered(self.form.actioncompilemessages))
        self.form.actioncreatecachetable.triggered.connect(lambda: self.on_action_triggered(self.form.actioncreatecachetable))
        self.form.actiondbshell.triggered.connect(lambda: self.on_action_triggered(self.form.actiondbshell))
        self.form.actiondiffsettings.triggered.connect(lambda: self.on_action_triggered(self.form.actiondiffsettings))
        self.form.actiondumpdata.triggered.connect(lambda: self.on_action_triggered(self.form.actiondumpdata))
        self.form.actionflush.triggered.connect(lambda: self.on_action_triggered(self.form.actionflush))
        self.form.actioninspectdb.triggered.connect(lambda: self.on_action_triggered(self.form.actioninspectdb))
        self.form.actionloaddata.triggered.connect(lambda: self.on_action_triggered(self.form.actionloaddata))
        self.form.actionmakemessages.triggered.connect(lambda: self.on_action_triggered(self.form.actionmakemessages))
        self.form.actionmakemigrations.triggered.connect(lambda: self.on_action_triggered(self.form.actionmakemigrations))
        self.form.actionmigrate.triggered.connect(lambda: self.on_action_triggered(self.form.actionmigrate))
        self.form.actionoptimizemigration.triggered.connect(lambda: self.on_action_triggered(self.form.actionoptimizemigration))
        self.form.actionsendtestemail.triggered.connect(lambda: self.on_action_triggered(self.form.actionsendtestemail))
        self.form.actionshell.triggered.connect(lambda: self.on_action_triggered(self.form.actionshell))
        self.form.actionshowmigrations.triggered.connect(lambda: self.on_action_triggered(self.form.actionshowmigrations))
        self.form.actionsqlflush.triggered.connect(lambda: self.on_action_triggered(self.form.actionsqlflush))
        self.form.actionsqlmigrate.triggered.connect(lambda: self.on_action_triggered(self.form.actionsqlmigrate))
        self.form.actionsqlsequencereset.triggered.connect(lambda: self.on_action_triggered(self.form.actionsqlsequencereset))
        self.form.actionssquashmigrations.triggered.connect(lambda: self.on_action_triggered(self.form.actionssquashmigrations))
        self.form.actionstartapp.triggered.connect(lambda: self.on_action_triggered(self.form.actionstartapp))
        self.form.actionstartproject.triggered.connect(lambda: self.on_action_triggered(self.form.actionstartproject))
        self.form.actiontest.triggered.connect(lambda: self.on_action_triggered(self.form.actiontest))
        self.form.actiontestserver.triggered.connect(lambda: self.on_action_triggered(self.form.actiontestserver))
        
        
        self.form.actionchangepassword.triggered.connect(lambda: self.on_action_triggered(self.form.actionchangepassword))
        self.form.actioncreatesuperuser.triggered.connect(lambda: self.on_action_triggered(self.form.actioncreatesuperuser))
        self.form.actionremove_stale_contenttypes.triggered.connect(lambda: self.on_action_triggered(self.form.actionremove_stale_contenttypes))
        
        self.form.actioncollectstatic.triggered.connect(lambda: self.on_action_triggered(self.form.actioncollectstatic))
        self.form.actionfindstatic.triggered.connect(lambda: self.on_action_triggered(self.form.actionfindstatic))
        self.form.actionrunserver.triggered.connect(lambda: self.on_action_triggered(self.form.actionrunserver))
        
        self.form.actionclearsessions.triggered.connect(lambda: self.on_action_triggered(self.form.actionclearsessions))
        



        self.txt_x = None
        self.form.actionExit.triggered.connect(self.exit)

    def exit(self):
        QApplication.exit()

    def on_action_triggered(self, action):
        self.txt_x = action.text()
        command = f"python manage.py {self.txt_x}"
        self.form.lineEdit_command.setText(command)
        #print(command)

    def helper(self):
        self.clear()
        os.system(f"python manage.py help {self.txt_x}")
        print("-"*30+"XXX"+"-"*30)

        
    def flush_databse(self):
        self.form.lineEdit_command.setText('python manage.py flush')
    def show_migration(self):
        self.form.lineEdit_command.setText('python manage.py showmigrations')
    def apply_migration(self):
        self.form.lineEdit_command.setText('python manage.py migrate')
    def make_migration(self):
        self.form.lineEdit_command.setText('python manage.py makemigrations')
    def check(self):
        os.system('python manage.py check')
        
    def executer(self,txt0):
        os.system(txt0)
        
    def shell(self):
        subprocess.Popen('start cmd /K "py manage.py shell"', shell=True)
        
    def command_show(self):
        pass
    def execute(self):
        
        cmd = self.form.lineEdit_command.text()
        if 'runserver' in cmd:
            self.abhi()
        else:
            
            os.system(f"{cmd}")
    def open_site(self,text):
        global window_x
        txt = self.form.lineEdit.text()
        url = f"{txt}" + f"{text}"
        #os.system(f"start {url}")
        
        window_x = window_designer()
        window_x.show()
        window_x.form_designer.lineEdit.setText(url)
        window_x.form_designer.webEngineView_5.setUrl(url)
        
    
    def clear(self):
        os.system('cls')
        
        
    def abhi(self):
    # Open a new command prompt and run a specific command
        subprocess.Popen('start cmd /K "py manage.py runserver"', shell=True)
        
        
        
    def database_show(self):
        print('----------------------------Django Database----------------------------')
        # Set the correct settings module
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')
        django.setup()
        
        from login.models import User

        users = User.objects.values()
        #for user in users:
        #    print(f"Name: {user.name}, Phone: {user.phone}, Email: {user.email},password:{user.password}")

        print(pandas.DataFrame(list(users)))
#---------------------------x----------------------------------

from PySide6.QtCore import Qt
class window_designer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        from window2 import Ui_designer
        from PySide6.QtWebEngineCore import ( QWebEngineSettings,QWebEngineProfile)
        from PySide6.QtGui import QIcon
        
        self.form_designer = Ui_designer()
        self.form_designer.setupUi(self)
        
        self.resizeEvent = self.on_resize10
        


        self.form_designer.lineEdit.setVisible(True)
        self.form_designer.lineEdit.move(125,1)
        self.form_designer.widget_toolbar.setVisible(True)


        self.form_designer.webEngineView_5.move(0,0)
        
        self.form_designer.widget_toolbar.move(0,0)
        self.form_designer.toolButton_aerrow_left.setVisible(True)
        self.form_designer.toolButton_aerrow_left.move(5,0)
        self.form_designer.toolButton_aerrow_right.setVisible(True)
        self.form_designer.toolButton_aerrow_right.move(30,0)
        self.form_designer.toolButton_refresh.setVisible(True)
        self.form_designer.toolButton_refresh.move(55,0)
        self.form_designer.pushButton_go.setVisible(True)
        self.form_designer.pushButton_go.move(80,0)
        self.form_designer.pushButton_save_page.setVisible(True)
        self.form_designer.pushButton_maximise.setVisible(True)
        self.form_designer.pushButton_go.clicked.connect(self.opener)


        self.form_designer.lineEdit.setStyleSheet("""
            QLineEdit {
                border: 2px solid rgb(0, 0, 0); /* Custom border color */
                border-radius: 8px; /* Optional: Make the corners rounded */
                
                                          
                background-color: rgb(240, 240, 240); /* Background color */
                alternate-background-color: rgb(100, 100, 100); /* Alternate background color */
                selection-background-color: rgb(137, 143, 255); /* Selected text background color */
                selection-color: rgb(0, 0, 0); /* Selected text color */
                color: rgb(0, 0, 0); /* Text color */
            }
        """)


       
        self.form_designer.lineEdit.returnPressed.connect(self.navigate)
        
        

        


        #self.settings = self.form_designer.webEngineView_5.page().profile()
        #self.settings.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        
     

        self.profile = self.form_designer.webEngineView_5.page().profile()
        self.profile.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanAccessClipboard, True)
        self.profile.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanPaste, True)
        #profile.downloadRequested.connect(self.on_downloadRequested)

        #self.form_designer.webEngineView_5.setPage(CustomWebEnginePage(self))
        self.form_designer.webEngineView_5.setZoomFactor(0.8)
       
        profile1 = QWebEngineProfile.defaultProfile()
        profile1.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")




        self.form_designer.toolButton_aerrow_left.clicked.connect(self.form_designer.webEngineView_5.back)
        self.form_designer.toolButton_aerrow_right.clicked.connect(self.form_designer.webEngineView_5.forward)
        self.form_designer.toolButton_refresh.clicked.connect(self.form_designer.webEngineView_5.reload)    
        
        self.form_designer.pushButton_maximise.clicked.connect(self.fulldisplay)
        self.fullscreen = False



    def fulldisplay(self):
        
        if self.fullscreen:
            self.showNormal()
            self.fullscreen = False
        else:
            self.showFullScreen()
            self.fullscreen = True




    def enterEvent(self, event):
        
        # Focus the window when the mouse enters
        self.activateWindow()  # Bring window to the front
        self.setFocus(Qt.OtherFocusReason)  # Set focus explicitly
        super().enterEvent(event)

    def opener(self):
        my_url = self.form_designer.webEngineView_5.url().toString()
        os.system(f"start {my_url}")




    '''def on_downloadRequested(self, download: QWebEngineDownloadRequest):
        # Open file dialog to select download location
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", download.suggestedFileName())
        
        if file_path:
            # Print debug info
            print(f"Download path selected: {file_path}")
            directory = QFileInfo(file_path).absolutePath()
            file_name = QFileInfo(file_path).fileName()

            print(f"Directory: {directory}")
            print(f"File Name: {file_name}")

            if QDir(directory).exists():
                print("Directory exists, proceeding with download.")
            else:
                print("Directory does not exist, creating directory.")
                if QDir().mkpath(directory):
                    print("Directory created successfully.")
                else:
                    print("Failed to create directory.")
                    QMessageBox.critical(self, "Error", f"Failed to create directory: {directory}")
                    return
            
            # Set the download directory and file name
            download.setDownloadDirectory(directory)
            download.setDownloadFileName(file_name)
            download.accept()

            print("Download accepted.")
        else:
            download.cancel()
            print("Download was canceled by the user.")'''

       


    def navigate(self):
        self.form_designer.webEngineView_5.setUrl(self.form_designer.lineEdit.text())
        


    def on_resize10(self, event):
        x,y = self.geometry().width(),self.geometry().height()
        self.form_designer.webEngineView_5.setGeometry(1,23,x-3,y-26)
        self.form_designer.widget_toolbar.setGeometry(0,0,x-2,23)
        self.form_designer.lineEdit.setGeometry(130,0,x-260,22)
        self.form_designer.pushButton_save_page.setGeometry(x-130,1,22,22)
        self.form_designer.pushButton_maximise.setGeometry(x-105,-1,22,22)
    


        
    '''def search(self):
        url = self.form.lineEdit.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.form.webEngineView_5.setUrl(url)'''

    

   

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = window()
    widget.show()
    
    sys.exit(app.exec())