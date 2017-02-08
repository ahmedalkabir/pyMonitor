"""
    pyMonitor first Version

    Written By :Ahmed Alkabir
"""

#!/usr/bin/python3

import main_ui as Ui
import sys

# Main Thread of Program
def main():
    if float(sys.version[:3]) >= 3.3:
        app = Ui.QtWidgets.QApplication(sys.argv)
        main_window  = Ui.QtWidgets.QMainWindow()
        ui = Ui.Ui_window(main_window)
        main_window.show()
        sys.exit(app.exec_())
    else:
        print('Sorry Bro minimum requirement is 3.3')

if __name__ == "__main__":
    main()