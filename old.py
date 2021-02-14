from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
import datetime
import os.path

now = datetime.datetime.now()

NumberOfWork = int(input())
#NumberOfWork = 5

fileName = "report.pdf"
title = "Отчет"
group = "ИКБО-08-19"
studentName = "Борисов А.В."

pdfmetrics.registerFont(TTFont('TimesNewRoman', 'times-new-roman.ttf', 'UTF-8'))

def WriteTitleList():
    pdf.setFont('TimesNewRoman', 12)
    pdf.drawImage("logo.jpg", 260, 750, 80, 80)
    pdf.drawString(230, 730, "МИНОБРНАУКИ РОССИИ")
    pdf.drawString(120, 710, "Федеральное государственное бюджетное образовательное учереждение")
    pdf.drawString(245, 690, 'высшего образования')
    pdf.setFont('TimesNewRoman', 14)
    pdf.drawString(140, 650, '"МИРЭА - Российский технологический университет"')
    pdf.drawString(265, 630, 'РТУ МИРЭА')
    pdf.line(50, 611, 550, 611)
    pdf.line(50, 609, 550, 609)
    pdf.setFont('TimesNewRoman', 12)
    pdf.drawString(205, 590, 'Институт Информационных технологий')
    pdf.drawString(180, 570, 'Кафедра корпоративных информационных систем')
    pdf.setFont('TimesNewRoman', 16)
    pdf.drawString(280, 425, 'ОТЧЕТ')
    pdf.drawString(185, 400, 'ПО ПРАКТИЧЕСКОЙ РАБОТЕ № ' + str(NumberOfWork))
    pdf.drawString(133, 375, 'по дисциплине "Програмирование на языке Python"')
    pdf.setFont('TimesNewRoman', 12)
    pdf.drawString(50, 210, 'Выполнил студент группы: ' + group)
    pdf.drawString(477, 210, studentName)
    pdf.drawString(50, 150, 'Практическая работа выполнена: ')
    pdf.drawString(250, 150, now.strftime("«%d»  %m  %Yг."))
    pdf.line(475, 150, 550, 150)
    pdf.drawString(110, 120, '«Зачтено»')
    pdf.drawString(250, 120, now.strftime("«    »  %m  %Yг."))
    pdf.line(475, 120, 550, 120)
    pdf.drawString(292, 50, 'Москва')
    pdf.drawString(300, 35, now.strftime("%Y"))

def WriteProgramCode():
    pdf.setFont('TimesNewRoman', 16)
    pdf.drawString(50, 780, 'Исходный код:')

    with open("code.py", "r") as file:
        text = file.read()

    textObject = pdf.beginText()
    textObject.setTextOrigin(75, 750)
    textObject.setFont('TimesNewRoman', 8)
    for line in text.splitlines(False):
        textObject.textLine(line.rstrip())
    pdf.drawText(textObject)

def WriteScreenshots():
    pdf.setFont('TimesNewRoman', 16)
    pdf.drawString(50, 780, 'Результат выполнения программы:')
    pdf.setFont('TimesNewRoman', 12)
    pdf.drawImage("screenshot1.png", 75, 450, 450, 300)
    pdf.drawString(280, 425, 'Рис. 1')
    if(os.path.exists("screenshot2.png")):
        pdf.drawImage("screenshot2.png", 75, 100, 450, 300)
        pdf.drawString(280, 75, 'Рис. 2')

pdf = canvas.Canvas(fileName, pagesize=A4)
pdf.setTitle(title)
WriteTitleList()
pdf.showPage()
WriteProgramCode()
pdf.showPage()
WriteScreenshots()
pdf.save()

