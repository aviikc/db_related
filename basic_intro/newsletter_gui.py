from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys
import personal_info

class Frame(QWidget):
    def __init__(self):
        super(Frame, self).__init__()
        uic.loadUi("newsletter_ui.ui", self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Avik's Newsletter")
        self.buttonPress()

    def buttonPress(self):
        self.pushButton_subscribe.clicked.connect(self.onClick)
        # self.pushButton_close.clicked.connect(self.onClose)

    # def validate_data(self):
        
    
    @pyqtSlot()
    def onClick(self):
        email_text = self.lineEdit_email.text()
        conf_email_text = self.lineEdit_confemail.text()
        fname_text = self.lineEdit_fname.text()
        lname_text = self.lineEdit_lname.text()
        # print(email_text)
        layout2 = QMessageBox.question(self, "Insert Data", "Insert Subscriber Data?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if layout2 == QMessageBox.Yes:
            if email_text == conf_email_text:
                if "@" in email_text and "." in email_text:
                    try:
                        personal_info.insert_subscriber_info(email_text, self.casing(fname_text), self.casing(lname_text))
                        self.label_warning.setText(None)
                        layout3 = QMessageBox()
                        layout3.setText("The document has been modified.")

                    except (ValueError, TypeError):
                        self.label_warning.setText("Value error")
                else:
                    self.label_warning.setText("Enter Valid Email")
            else:
                self.label_warning.setText("Email Don't Match")
        else:
            print(" ")

    
    def casing(self, my_text):
        my_new_text = [text for text in my_text.lower()]
        my_new_text[0] = my_new_text[0].upper()
        return "".join(my_new_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = Frame()
    frame.show()
    sys.exit(app.exec_())

