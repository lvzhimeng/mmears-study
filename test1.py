import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('Button Button Button Button Button Button', self)
        btn.setToolTip('This is a <b>测试包</b> widget')

        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())   #按钮根据内容多少自适应宽高

        # 移动窗口的位置
        btn.move(50, 50)
        # 设置窗口的位置和大小,从屏幕左上角（300，300）开始，显示800*500的框
        self.setGeometry(300, 300, 800, 500)
        # 设置窗口的标题
        self.setWindowTitle('这是窗口标题')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('20210414164721.png'))
        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())