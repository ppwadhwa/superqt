from superqt import QElidingLabel
from superqt.qtcompat.QtWidgets import QApplication

app = QApplication([])

widget = QElidingLabel(
    "a skj skjfskfj sdlf sdfl sdlfk jsdf sdlkf jdsf dslfksdl sdlfk sdf sdl "
    "fjsdlf kjsdlfk laskdfsal as lsdfjdsl kfjdslf asfd dslkjfldskf sdlkfj"
)
widget.setWordWrap(True)
widget.show()
app.exec_()
