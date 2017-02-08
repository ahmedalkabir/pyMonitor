"""
    pyMonitor first Version

    Written By :Ahmed Alkabir
"""

#!/usr/bin/python3

import main_ui as Ui
import sys

# Main Thread of Program
def main():
    app = Ui.QtWidgets.QApplication(sys.argv)
    main_window  = Ui.QtWidgets.QMainWindow()
    ui = Ui.Ui_window(main_window)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()