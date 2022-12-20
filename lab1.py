import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import Tk
from tkinter import Tk, BOTH, IntVar, LEFT
from tkinter.ttk import Frame, Label, Scale, Style
from tkinter import messagebox
from PIL import *
from tkinter import ttk 

class Image(Frame):

    def Settings(self):

        root = Tk()
        l1 = Label(root)
        l2 = Label(root)
        l3 = Label(root)

        def mv(event):
            l1["text"] = str(int(scale.get()))
            l2["text"] = str(int(scale1.get()))
            l3["text"] = str(int(scale2.get()))

            self.v1 = int(scale.get())
            self.v2 = int(scale1.get())
            self.v3 = int(scale2.get())



        width = 300
        height = 200

        scale = Scale( root, from_=0, to=255, value = 30, command = mv)
        scale.pack(anchor = CENTER)

        scale1 = Scale( root, from_=0, to=255, command = mv)
        scale1.pack(anchor=CENTER)

        scale2 = Scale( root, from_=0, to=255, command = mv)
        scale2.pack(anchor=CENTER)
        

        



        l1.pack()
        l2.pack()
        l3.pack()


        button = Button(root, text="Обработать изображение", command=self.Img)
        button.pack(anchor=CENTER)

        

        root.mainloop()


    def Img(self):
    
        

            img1 = cv2.imread("banana1.jpg", cv2.IMREAD_COLOR)
            img = cv2.imread("banana1.jpg", cv2.IMREAD_COLOR)
            
            canny1 = self.v1
            canny2 = self.v2
            s1 = self.v3
            
            
            width = img.shape[0]
            height  = img.shape[1]

            edge = cv2.Canny(img, canny1, canny2)
        
        
            for k in range (3):
                for i in range(width):
                    for j in range(height):
                        
                        color = img1[i, j, k]
                            
                        if color<=50:
                            color = 0+s1
                        elif color<=100:
                            color = 25+s1
                        elif color<=150:
                            color = 180+s1
                        elif color<=200:
                            color = 210+s1
                        else:
                            color = 255
                        
                        img1[i, j, k] = color
                        img1[i,j] = img1[i,j] - edge[i,j]    

            cv2.startWindowThread()
            cv2.imshow("canny", edge)
            cv2.imshow("cellShading", img1)
            cv2.waitKey(0)


    
      




if __name__ == '__main__':
    def nothing(*arg):
        pass




def Video():
    messagebox.showinfo("Предупреждение", "Чтобы закрыть окно веб-камеры - нажмите 'q'")
    
    cap = cv2.VideoCapture('flower.mp4')
    cv2.namedWindow( "settings" ) # создаем окно настроек
    cv2.resizeWindow("settings", 400, 250)

    percent = 20    
    cv2.createTrackbar('h1', 'settings', 50, 255, nothing)
    cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
    crange = [0,0,0, 0,0,0]

    

    if(cap.isOpened() == False):
        print("Ошибка при чтении видеофайла")
    else:
        while cap.isOpened():
            ret, frame = cap.read()

            width = int(frame.shape[1] * percent / 100) 
            height = int(frame.shape[0] * percent / 100) 

            dim = (width, height)
            frame_re = cv2.resize(frame, dim)

            

            # считываем значения бегунков
            h1 = cv2.getTrackbarPos('h1', 'settings')
            #h1.style()
            s1 = cv2.getTrackbarPos('s1', 'settings')
            v1 = cv2.getTrackbarPos('v1', 'settings')
            h2 = cv2.getTrackbarPos('h2', 'settings')
            s2 = cv2.getTrackbarPos('s2', 'settings')
            v2 = cv2.getTrackbarPos('v2', 'settings')

            # формируем начальный и конечный цвет фильтра
            h_min = np.array((h1, s1, v1), np.uint8)
            h_max = np.array((h2, s2, v2), np.uint8)

            thresh = cv2.inRange(frame_re, h_min, h_max)

            cv2.imshow('result', thresh)
            cv2.imshow('Look', frame_re)



            if cv2.waitKey(40) == 27 & 0xFF == ord('q'):
               break

        cap.release()
        cv2.destroyAllWindows() 

def Video1():

    messagebox.showinfo("Предупреждение", "Чтобы закрыть окно веб-камеры - нажмите 'q'")
    
    cap = cv2.VideoCapture(0)
    cv2.namedWindow( "settings" ) # создаем окно настроек
    cv2.resizeWindow("settings", 400, 250)

    percent = 20    
    cv2.createTrackbar('h1', 'settings', 50, 255, nothing)
    cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
    crange = [0,0,0, 0,0,0]

    

    if(cap.isOpened() == False):
        print("Ошибка при чтении видеофайла")
    else:
        while cap.isOpened():
            ret, frame = cap.read()

            width = int(frame.shape[1] * percent / 50) 
            height = int(frame.shape[0] * percent / 50) 

            dim = (width, height)
            frame_re = cv2.resize(frame, dim)

            

            # считываем значения бегунков
            h1 = cv2.getTrackbarPos('h1', 'settings')
            #h1.style()
            s1 = cv2.getTrackbarPos('s1', 'settings')
            v1 = cv2.getTrackbarPos('v1', 'settings')
            h2 = cv2.getTrackbarPos('h2', 'settings')
            s2 = cv2.getTrackbarPos('s2', 'settings')
            v2 = cv2.getTrackbarPos('v2', 'settings')

            # формируем начальный и конечный цвет фильтра
            h_min = np.array((h1, s1, v1), np.uint8)
            h_max = np.array((h2, s2, v2), np.uint8)

            thresh = cv2.inRange(frame_re, h_min, h_max)

            cv2.imshow('result', thresh)
            cv2.imshow('Look', frame_re)



            if cv2.waitKey(40) == 27 & 0xFF == ord('q'):
               break

        cap.release()
        cv2.destroyAllWindows() 


def clicked2():
    Video()

def clicked3():
    exit()

def clicked4():
    Video1()


def Menu():
    window = Tk()
    window.title("Lab1")

    img = Image()

    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    w = w - 200 # смещение от середины
    h = h - 200
    window.geometry('600x400+{}+{}'.format(w, h))
    window.configure(bg='#bb85f3')

    btn = Button(window, text="Обработка фото", padx=5, pady=5, command = img.Settings, bg='#eec6ea')  
    btn.pack(anchor="center", padx=20, pady=30)

    btn1 = Button(window, text="Обработка видео", padx=5, pady=5, command = clicked2, bg='#eec6ea')  
    btn1.pack(anchor="center", padx=20, pady=30)

    btn2 = Button(window, text="Вывод видео с веб-камеры", padx=5, pady=5, command = clicked4, bg='#eec6ea')  
    btn2.pack(anchor="center", padx=20, pady=30)

    btn3 = Button(window, text="Выход", padx=5, pady=5, command = clicked3, bg='#eec6ea')  
    btn3.pack(anchor="center", padx=20, pady=30)

    window.mainloop()

Menu()