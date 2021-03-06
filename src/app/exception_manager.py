import traceback
import sys
from PyQt5.QtWidgets import QMessageBox, QApplication

in_qt_loop = False
window = None


def handle_exception(type, value, tb):
    # Print exception traceback on console
    traceback.print_tb(tb)

    # Display exception in a GUI message box
    mbox = QMessageBox(window)
    mbox.setModal(True)
    mbox.setIcon(QMessageBox.Warning)
    mbox.setWindowTitle('An error has occurred! [uh-oh?]')

    if isinstance(value, PermissionError):
        msg = f'Permission denied while trying to write to file: {value.filename}'
        info = 'That file is most likely read-only. Please make sure to disable that on the file/folder properties and trying again!'
    else:
        msg = f'Error: {value}'
        info = 'An exception has occurred in the code. The details are provided below.'

    mbox.setText(msg)
    mbox.setInformativeText(info)
    mbox.setDetailedText(str(traceback.format_tb(tb)))
    mbox.show()

    if not in_qt_loop:
        app = QApplication([])
        sys.exit(app.exec_())
