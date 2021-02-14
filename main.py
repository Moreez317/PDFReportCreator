from fpdf import FPDF
import datetime
import os.path

now = datetime.datetime.now()

#numberofwork = int(input())
numberofwork = 3;

filename = "report.pdf"

group = "ИКБО-08-19"
studentname = "Борисов А.В."

def writetitlelist():
    pdf.image('logo.jpg', x=98, y=5, w=25)
    pdf.set_font('TNR', '', 12)
    pdf.cell(200, 50, "МИНОБРНАУКИ РОССИИ", align="C")
    pdf.ln(5)
    pdf.cell(200, 55, "Федеральное государственное бюджетное образовательное учереждение", align="C")
    pdf.ln(5)
    pdf.cell(200, 55, "высшего образования", align="C")
    pdf.ln(8)
    pdf.set_font('TNR', '', 14)
    pdf.cell(200, 55, '"МИРЭА - Российский технический университет"', align="C")
    pdf.ln(5)
    pdf.cell(200, 55, '"РТУ МИРЭА"', align="C")
    pdf.ln(5)
    pdf.line(10, 65, 200, 65)
    pdf.line(10, 66, 200, 66)
    pdf.ln(5)
    pdf.set_font('TNR', '', 12)
    pdf.cell(200, 55, 'Институт Информационных технологий', align="C")
    pdf.ln(5)
    pdf.cell(200, 55, 'Кафедра корпоративных информационных систем', align="C")
    pdf.ln(65)
    pdf.set_font('TNR', '', 16)
    pdf.cell(200, 55, 'ОТЧЕТ', align="C")
    pdf.ln(10)
    pdf.cell(200, 55, 'ПО ПРАКТИЧЕСКОЙ РАБОТЕ № ' + str(numberofwork), align="C")
    pdf.ln(10)
    pdf.cell(200, 55, 'По дисциплине «Программирование на языке Python»', align="C")
    pdf.ln(75)
    pdf.set_font('TNR', '', 14)
    pdf.cell(100, 25, 'Выполнил студент группы: ' + group, align="L")
    pdf.cell(120, 25, studentname, align="C")
    pdf.ln(25)
    pdf.set_font('TNR', '', 12)
    pdf.cell(85, 25, 'Практическая работа выполнена: ', align="L")
    pdf.cell(85, 25, now.strftime("«%d»  %m  %Yг."), align="L")
    pdf.line(150, 248, 190, 248)
    pdf.ln(10)
    pdf.cell(85, 25, '«Зачтено» ', align="L")
    pdf.cell(85, 25, now.strftime("«    »  %m  %Yг."), align="L")
    pdf.line(150, 258, 190, 258)

def writeprogramcode():
    pdf.add_page()
    pdf.set_font('TNR', '', 16)
    pdf.cell(100, 15, '1. Исходный код программы', align="L")
    pdf.ln(15)
    with open("code.py", "r") as file:
        text = file.read()
    pdf.set_font('TNR', '', 12)
    pdf.multi_cell(effective_page_width, 5, text)

def writescreenshots():
    pdf.add_page()
    pdf.set_font('TNR', '', 16)
    pdf.cell(100, 15, '2. Результат выполнения программы', align="L")
    pdf.ln(15)
    pdf.set_font('TNR', '', 14)
    pdf.image('screenshot1.png', x=30, y=25, w=150, h=90)
    pdf.ln(85)
    pdf.cell(190, 25, 'Рис. 1', align="C")
    if (os.path.exists("screenshot2.png")):
        pdf.image('screenshot2.png', x=30, y=140, w=150, h=90)
        pdf.ln(115)
        pdf.cell(190, 25, 'Рис. 2', align="C")


pdf = FPDF(unit="mm", format="A4")
pdf.add_page()
effective_page_width=pdf.w-2*pdf.l_margin
pdf.add_font('TNR', '', 'times-new-roman.ttf', uni=True)
writetitlelist()
writeprogramcode()
writescreenshots()
pdf.output(filename)

