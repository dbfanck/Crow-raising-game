from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class MainFrame(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.setupUi()

    def setupUi(self):

        self.setWindowTitle('까마귀 키우기')
        self.setFixedSize(1280,800)

    #함수-이름설정
    def btn_name_clicked(self):

        self.name=self.line_name.text()
        self.lb_name.setText(self.name)
        self.lb_name.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
        self.line_name.deleteLater()
        self.btn_name.deleteLater()
        self.lv_1()

    def start(self):

        #화면 이미지
        self.lb_img=QtWidgets.QLabel(self)
        self.lb_img.setGeometry(220,40,840,580)
        self.lb_img.show()
        pixmap=QtGui.QPixmap('./images/둥지-1.jpg')
        self.lb_img.setPixmap(pixmap)

        #이름 위젯
        self.line_name=QtWidgets.QLineEdit('까마귀 이름을 지어주세요', self)
        self.line_name.setGeometry(440,650,400,50)
        self.line_name.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
        self.line_name.show()

        self.lb_name=QtWidgets.QLabel(self)
        self.lb_name.setGeometry(20,80,180,50)
        self.lb_name.show()

        self.btn_name=QtWidgets.QPushButton('확인',self)
        self.btn_name.setGeometry(860,650,50,50)
        self.btn_name.show()
        self.btn_name.clicked.connect(self.btn_name_clicked)

    #함수-알깨기
    def btn_egg_clicked(self):

        self.egg+=1
        self.lb_egg.setText('알깨기:'+str(self.egg)+'/30클릭')

        if self.egg==10:
            pixmap=QtGui.QPixmap('./images/둥지-2.jpg')
            self.lb_img.setPixmap(pixmap)

        elif self.egg==20:
            pixmap=QtGui.QPixmap('./images/둥지-3.jpg')
            self.lb_img.setPixmap(pixmap)

        elif self.egg==30:
            self.lb_egg.deleteLater()
            self.btn_egg.deleteLater()
            self.lv_2()

    def lv_1(self):

        #레벨 위젯
        self.level=1
        self.lb_level=QtWidgets.QLabel(self)
        self.lb_level.setText('Lv '+str(self.level))
        self.lb_level.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
        self.lb_level.setGeometry(20,40,180,50)
        self.lb_level.show()

        #돈 위젯
        self.money=100
        self.lb_money=QtWidgets.QLabel('보유금액:'+str(self.money), self)
        self.lb_money.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
        self.lb_money.setGeometry(20,120,180,50)
        self.lb_money.show()

        #알깨기 위젯
        self.egg=0
        self.lb_egg=QtWidgets.QLabel('알깨기:'+str(self.egg)+'/30클릭', self)
        self.lb_egg.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
        self.lb_egg.setGeometry(1080,80,180,50)
        self.lb_egg.show()

        self.btn_egg=QtWidgets.QPushButton('알 깨기', self)
        self.btn_egg.setGeometry(540,650,200,100)
        self.btn_egg.show()
        self.btn_egg.clicked.connect(self.btn_egg_clicked)

    #함수-레벨업
    def level_up(self):

        if self.hp>=self.limit and self.hungry>=self.limit and self.study>=self.limit:

            if self.level==2:
                self.lv_3()

            elif self.level==3:
                self.lv_4()

    #함수-삭제
    def delete(self):

        self.btn_work.deleteLater()
        self.btn_hungry.deleteLater()
        self.btn_study.deleteLater()
        self.btn_play.deleteLater()
        self.lb_hp.deleteLater()
        self.lb_hungry.deleteLater()
        self.lb_study.deleteLater()
        self.lb_stress.deleteLater()
        self.lb_level.deleteLater()
        self.lb_name.deleteLater()
        self.lb_money.deleteLater()
        self.lb_1.deleteLater()
        self.lb_2.deleteLater()
        self.lb_3.deleteLater()
        self.lb_4.deleteLater()

    #함수-게임 오버
    def end_stress(self):

        self.delete()

        pixmap=QtGui.QPixmap('./images/떠남.jpg')
        self.lb_img.setPixmap(pixmap)

        self.lb_sad=QtWidgets.QLabel(self)
        self.lb_sad.setGeometry(220,650,840,100)
        self.lb_sad.setText('더이상 여기서 못살겠어요.. 전 야생으로 떠날래요')
        self.lb_sad.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
        self.lb_sad.show()

    #함수-일하기
    def btn_work_clicked(self):

        if self.hp<(self.limit-1):
            self.hp+=1
            self.stress+=2
            self.money+=15
            self.lb_hp.setText('체력:'+str(self.hp)+'/'+str(self.limit))
            self.lb_stress.setText('스트레스:'+str(self.stress)+'/30')
            self.lb_money.setText('보유금액:'+str(self.money))

            if self.stress>=30:
                self.end_stress()

        elif self.hp>=(self.limit-1):
            self.hp+=1
            self.stress+=2
            self.money+=15
            self.lb_hp.setText('체력:'+str(self.hp)+'/'+str(self.limit))
            self.lb_stress.setText('스트레스:'+str(self.stress)+'/30')
            self.lb_money.setText('보유금액:'+str(self.money))

            if self.stress>=30:
                self.end_stress()
            else:
                self.level_up()

    #함수-먹이주기
    def btn_hungry_clicked(self):

        if self.money>=10:

            if self.hungry<(self.limit-1):
                self.hungry+=1
                self.stress-=2
                self.money-=10
                self.lb_hungry.setText('포만감:'+str(self.hungry)+'/'+str(self.limit))
                self.lb_stress.setText('스트레스:'+str(self.stress)+'/30')
                self.lb_money.setText('보유금액:'+str(self.money))

            elif self.hungry>=(self.limit-1):
                self.hungry+=1
                self.stress-=2
                self.money-=10
                self.lb_hungry.setText('포만감:'+str(self.hungry)+'/'+str(self.limit))
                self.lb_stress.setText('스트레스:'+str(self.stress)+'/30')
                self.lb_money.setText('보유금액:'+str(self.money))
                self.level_up()

    #함수-학습하기
    def btn_study_clicked(self):

        if self.study<(self.limit-1):
            self.hp-=1
            self.study+=1
            self.stress+=1
            self.lb_hp.setText('체력:'+str(self.hp)+'/'+str(self.limit))
            self.lb_study.setText('지식:'+str(self.study)+'/'+str(self.limit))
            self.lb_stress.setText('스트레스:'+str(self.stress)+'/30')

            if self.stress>=30:
                self.end_stress()

        elif self.study>=(self.limit-1):
            self.hp-=1
            self.study+=1
            self.stress+=1
            self.lb_hp.setText('체력:'+str(self.hp)+'/'+str(self.limit))
            self.lb_study.setText('지식:'+str(self.study)+'/'+str(self.limit))
            self.lb_stress.setText('스트레스:'+str(self.stress)+'/30')

            if self.stress>=30:
                self.end_stress()
            else:
                self.level_up()

    #함수-놀아주기
    def btn_play_clicked(self):

        if self.hp<(self.limit-1):
            self.hp+=1
            self.hungry-=1
            self.stress-=1
            self.lb_hp.setText('체력:'+str(self.hp)+'/'+str(self.limit))
            self.lb_hungry.setText('포만감:'+str(self.hungry)+'/'+str(self.limit))
            self.lb_stress.setText('스트레스:'+str(self.stress)+'/30')

        elif self.hp>=(self.limit-1):
            self.hp+=1
            self.hungry-=1
            self.stress-=1
            self.lb_hp.setText('체력:'+str(self.hp)+'/'+str(self.limit))
            self.lb_hungry.setText('포만감:'+str(self.hungry)+'/'+str(self.limit))
            self.lb_stress.setText('스트레스:'+str(self.stress)+'/30')
            self.level_up()     

    def lv_2(self):

        self.level+=1
        self.lb_level.setText('Lv '+str(self.level))

        pixmap=QtGui.QPixmap('./images/새끼.jpg')
        self.lb_img.setPixmap(pixmap)

        self.limit=20

        #까마귀 능력치 위젯
        self.hp=0
        self.hungry=0
        self.study=0
        self.stress=0

        self.lb_hp=QtWidgets.QLabel('체력:'+str(self.hp)+'/'+str(self.limit), self)
        self.lb_hungry=QtWidgets.QLabel('포만감:'+str(self.hungry)+'/'+str(self.limit), self)
        self.lb_study=QtWidgets.QLabel('지식:'+str(self.study)+'/'+str(self.limit), self)
        self.lb_stress=QtWidgets.QLabel('스트레스:'+str(self.stress)+'/30', self)

        widget_y=40
        self.stat_List=[self.lb_hp, self.lb_hungry, self.lb_study, self.lb_stress]

        #하단 위젯(일하기/먹이주기/학습하기/놀아주기)
        self.btn_work=QtWidgets.QPushButton('일하기', self)
        self.btn_hungry=QtWidgets.QPushButton('먹이주기', self)
        self.btn_study=QtWidgets.QPushButton('학습하기', self)
        self.btn_play=QtWidgets.QPushButton('놀아주기', self)

        self.lb_1=QtWidgets.QLabel('돈 +15 체력 +1 스트레스 +2', self)
        self.lb_2=QtWidgets.QLabel('돈 -10 포만감 +1 스트레스 -2', self)
        self.lb_3=QtWidgets.QLabel('체력 -1 지식 +1 스트레스 +1', self)
        self.lb_4=QtWidgets.QLabel('체력 +1 포만감 -1 스트레스 -1', self)

        font1=self.lb_1.font()
        font2=self.lb_2.font()
        font3=self.lb_3.font()
        font4=self.lb_4.font()

        widget_x=165
        self.btn_List=[self.btn_work, self.btn_hungry, self.btn_study, self.btn_play]
        self.def_List=[self.btn_work_clicked, self.btn_hungry_clicked, self.btn_study_clicked, self.btn_play_clicked]
        self.lb_List=[self.lb_1, self.lb_2, self.lb_3, self.lb_4]
        font_List=[font1, font2, font3, font4]

        for i in range(4):

            self.stat_List[i].setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
            self.stat_List[i].setGeometry(1080,widget_y,180,50)
            self.stat_List[i].show()

            widget_y+=40

            self.btn_List[i].setGeometry(widget_x,650,200,100)
            self.btn_List[i].show()
            self.btn_List[i].clicked.connect(self.def_List[i])

            self.lb_List[i].setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
            self.lb_List[i].setGeometry(widget_x,750,200,50)
            font_List[i].setPointSize(7)
            self.lb_List[i].setFont(font_List[i])
            self.lb_List[i].show()

            widget_x+=250

    def lv_3(self):

        self.level+=1
        self.lb_level.setText('Lv '+str(self.level))

        pixmap=QtGui.QPixmap('./images/성인.jpg')
        self.lb_img.setPixmap(pixmap)

        self.limit=50
        self.lb_hp.setText('체력:'+str(self.hp)+'/'+str(self.limit))
        self.lb_hungry.setText('포만감:'+str(self.hungry)+'/'+str(self.limit))
        self.lb_study.setText('지식:'+str(self.study)+'/'+str(self.limit))      

    #함수-게임 엔딩
    def lv_4(self):

        self.delete()

        pixmap=QtGui.QPixmap('./images/졸업.jpg')
        self.lb_img.setPixmap(pixmap)

        self.lb_hap=QtWidgets.QLabel(self)
        self.lb_hap.setGeometry(220,650,840,100)
        self.lb_hap.setText('고마워용~ 덕분에 나 '+self.name+', 멋진 까마귀가 되었네용~')
        self.lb_hap.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
        self.lb_hap.show()

app=QtWidgets.QApplication([])
MainFrame=MainFrame()
MainFrame.show()
MainFrame.start()
app.exec_()