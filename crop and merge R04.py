import PyPDF3
from PyPDF3.pdf import PageObject
from copy import copy

from tkinter import *
from tkinter import filedialog

import os

myWindow = Tk()
myWindow.title("Resize PDF")
myWindow.geometry("500x180")

def inputFile (userInput):

    pdf_input_file = open(userInput, "rb")
    pdf_reader = PyPDF3.PdfFileReader(pdf_input_file)

    pdf_output_file = open("temp.pdf", "wb")
    pdf_writer = PyPDF3.PdfFileWriter()

    total_width = 595
    total_height = 1684

    if pdf_reader.numPages % 2 == 0:
        for x in range(0, pdf_reader.numPages-1, 2):
            page_first = pdf_reader.getPage(x)
            page_second = pdf_reader.getPage(x+1)
            new_page = PageObject.createBlankPage(None, total_width, total_height)
            # Add first page at the 0,0 position
            new_page.mergePage(page_first)
            # Add second page with moving along the axis y
            new_page.mergeTranslatedPage(page_second, 0, 842)
            print(page_first)
            pdf_writer.addPage(new_page)
            pdf_writer.write(pdf_output_file)
        pdf_output_file.close()
    else:
        for x in range(0, pdf_reader.numPages-2, 2):
            page_first = pdf_reader.getPage(x)
            page_second = pdf_reader.getPage(x+1)
            new_page = PageObject.createBlankPage(None, total_width, total_height)
            # Add first page at the 0,0 position
            new_page.mergePage(page_first)
            # Add second page with moving along the axis y
            new_page.mergeTranslatedPage(page_second, 0, 842)
            print(page_first)
            pdf_writer.addPage(new_page)
            pdf_writer.write(pdf_output_file)
        page_last = pdf_reader.getPage(pdf_reader.numPages-1)
        page_blank = PageObject.createBlankPage(None, 595, 842)
        print(pdf_reader.numPages)
        new_page = PageObject.createBlankPage(None, total_width, total_height)
        new_page.mergePage(page_last)
        new_page.mergeTranslatedPage(page_blank, 0, 842)
        pdf_writer.addPage(new_page)
        pdf_writer.write(pdf_output_file)
        pdf_output_file.close()

    pdf_input_file_final = open("temp.pdf", "rb")
    pdf_reader = PyPDF3.PdfFileReader(pdf_input_file_final)

    pdf_output_file_final = open(userInput+' - merged.pdf', "wb")
    pdf_writer = PyPDF3.PdfFileWriter()

    for i in range(pdf_reader.numPages):
        page = pdf_reader.getPage(i)
        a = copy(page)
        a.cropBox.setLowerLeft((0, 421))
        a.cropBox.setLowerRight((595, 421))
        a.cropBox.setUpperLeft((0, 1263))
        a.cropBox.setUpperRight((595, 1263))
        pdf_writer.addPage(a)

        pdf_writer.write(pdf_output_file_final)
        pdf_writer.removeLinks()
    pdf_output_file_final.close()
    pdf_input_file_final.close()
    os.remove("temp.pdf")

def browseFunc():
    filename = filedialog.askopenfilename(filetypes = (("Adobe Acrobat'", "*.pdf"), ("All files", "*.*")))
    posOfLastSlash = filename.rindex("/")
    print(posOfLastSlash)
    path = filename[0:posOfLastSlash]
    pathLabel.config(text='The resized PDF file was saved to the following folder: '+'\n'+path)
    inputFile(filename)
    return

selectLabel_space_1 = Label(myWindow)
selectLabel_space_1.config(text="")
selectLabel_space_1.pack()

selectLabel = Label(myWindow)
selectLabel.config(text="Please select the PDF file")
selectLabel.pack()

browsebutton = Button(myWindow, padx=20, pady=0 ,text="Browse", command= browseFunc)
browsebutton.pack(side=TOP)

selectLabel_space_2 = Label(myWindow)
selectLabel_space_2.config(text="")
selectLabel_space_2.pack()

selectLabel_space_3 = Label(myWindow)
selectLabel_space_3.config(text="This may take a while..., better grab some coffee..., I'll tell you when it's over")
selectLabel_space_3.pack()

pathLabel = Label(myWindow)
pathLabel.pack()

myWindow.mainloop()