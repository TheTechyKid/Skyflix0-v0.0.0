#!/usr/bin/env python3
# Skyflix 0.py

import tkinter as tk
import customtkinter as ctk
from pytube import YouTube
import pathlib
import requests
import os
from PIL import Image, ImageTk
from io import BytesIO
import webbrowser
import secrets
import scrapetube
from rich.progress import Progress
import time

username = "a"

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FILE_PATH = r"C:\Users\Gianclarence Solas\Desktop\python books\Skyflix"

# App
app = ctk.CTk()
app.geometry("1100x700")
app.title("Skyflix 0")
app.resizable(False, False)

def get_data(file):
    with open(file) as f:
        link_data = []
        raw_data = f.readlines()
        for link in raw_data:
            x = link.replace("\n", "")
            link_data.append(x)
        return link_data

# Main class
class AppMain():
    """Main App Class. Version 5.0.2."""
    
    # Image vars
    SkyflixWord = tk.PhotoImage(file=pathlib.PurePath(r"Images\SkyFlix.png"))
    
    # Channel lists
    channels = get_data("data.txt")
    
    # tools
    @staticmethod
    def getDes(url):
        youtube = YouTube(url)
        stream = youtube.streams.first()
        desc = youtube.description
        return desc
    
    @staticmethod
    def Greating():
        compliments = ["You're a ray of sunshine!",
                       "You have a heart of gold!",
                       "You're a great listener!",
                       "You're amazing and inspiring!",
                       "You're a true gem!",
                       "You're an incredible friend!",
                       "You're a fantastic team player!",
                       "You're so creative and innovative!",
                       "You have an infectious enthusiasm!",
                       "You have a great sense of humor!",
                       "You have a beautiful soul!",
                       "You're a problem-solving genius!",
                       "You're an absolute pleasure to be around!",
                       "You're a natural born leader!",
                       "You're a hard worker and dedicated!",
                       "You always have a positive attitude!",
                       "You have a remarkable talent!",
                       "You inspire others with your actions!",
                       "You're a valuable asset to any team!",
                       "You're a kind and caring individual!"]
        ranComliment = secrets.choice(compliments)
        Label = ctk.CTkLabel(master=app, text=ranComliment)
        Label.place(x=470, y=650)
    
    @staticmethod
    def getTitle(url):
        """Get the youtube links title."""
        
        url = url
        Title = YouTube(url=url).title
        return Title       
    
    @staticmethod    
    def downloadVid(url):
        """Download the youtube link."""
        
        YouTube(url).streams.get_highest_resolution().download(pathlib.PurePath(r"video"))
    
    @staticmethod
    def clear():
        """Clear all the wigets in the screen."""
        
        for widgets in app.winfo_children():
            widgets.destroy()
    
    @staticmethod
    def playVid(url):
        """Play the video."""

        data = url.replace("https://www.youtube.com/watch?v=", "")

        javascript_code = f"""var pythonData = '{str(data)}';\nvar videoFrame = document.getElementById('video');\nif (videoFrame) {{\n    videoFrame.src = 'https://www.youtube.com/embed/' + pythonData;\n}}
        """
        
        with open('data.js', 'w') as f:
            f.write(javascript_code) 

        file_path = FILE_PATH+r"\videoPlayer.html"
        print(file_path)
        browser = webbrowser.get('"C:/Program Files/Google/Chrome/Application/chrome.exe" %s')
        browser.open(file_path)
    
    @staticmethod
    def getLastestVid(channel):
        """Get the lastest video from a youtube channel."""
        
        video_list = []
        amount_of_videos = 15
        videos = scrapetube.get_channel(channel_url=channel, limit=amount_of_videos)

        for video in videos:
            video_list.append(video['videoId'])
        
        # for vid in video_list:
        #     print(YouTube("https://www.youtube.com/watch?v="+vid).title)
            
        random_video = secrets.choice(video_list)
        
        return "https://www.youtube.com/watch?v="+random_video
    
    def GetThumUrl(url):
        image_url = YouTube(url).thumbnail_url
        return image_url
    
    @staticmethod
    def showURLImage(url, size):
        response = requests.get(url)
        image_data = BytesIO(response.content)
        image_pil = Image.open(image_data)

        # Resize Image
        new_size = (round(image_pil.width / size), round(image_pil.height / size))
        image_resized = image_pil.resize(new_size, Image.LANCZOS)

        image_tk = ImageTk.PhotoImage(image_resized)
        
        return image_tk

    @staticmethod
    def ShortenTitle(title):
        """Shorten the title of the video if it is over 41 char."""
        if len(title) >= 41:
            short_text = title[0:35]+"..."
            return short_text
        else:
            return title
  
    @staticmethod
    def showVideoDetails(url, num):
        app.title("Skyflix 0")
        AppMain.clear()
        urlCleansed = AppMain.GetThumUrl(url)
        imageURL = AppMain.showURLImage(urlCleansed, 3)
        image_label = tk.Label(app, image=imageURL)
        
        Title = ctk.CTkLabel(master=app, text=AppMain.ShortenTitle(YouTube(url).title), font=("Arial", 35))
        
        DesTitle = ctk.CTkLabel(master=app, text="Description", font=("Arial", 20))
        Decription = ctk.CTkTextbox(master=app, height=320, width=1077)
        buttonplay = ctk.CTkButton(master=app, text="Play", width=530, command=num)
        back = ctk.CTkButton(master=app, text="<--", command=AppMain.HomeScreen, width=50)
        
        # Insert Decription
        Decription.insert("0.0", f"""{AppMain.getDes(url)}""")
        
        # Placement
        image_label.pack()
        Title.pack()
        buttonplay.place(x=285, y=140+160)
        DesTitle.place(x=10, y=190+150)
        Decription.place(x=10, y=170 + 200)
        back.place(x=10, y=10)

        app.mainloop()  # Start the main event loop

    a = getLastestVid(channels[0])
    b = getLastestVid(channels[1])
    c = getLastestVid(channels[2])
    d = getLastestVid(channels[3])
    e = getLastestVid(channels[4])
    f = getLastestVid(channels[5])
    g = getLastestVid(channels[6])
    h = getLastestVid(channels[7])   
    i = getLastestVid(channels[8])
    
    with Progress() as progress:
        task1 = progress.add_task("[blue]Fetching Data...[/]", total=10)
        while not progress.finished:
            progress.update(task1, advance=2)
            time.sleep(0.8)
    
    @staticmethod
    def HomeScreen():
        """Home Screen."""
        
        app.title("Skyflix 0")
        os.system('cls')
        AppMain.clear()
        
        def Add0(): AppMain.playVid(AppMain.a)
        def Add1(): AppMain.playVid(AppMain.b)
        def Add2(): AppMain.playVid(AppMain.c)
        def Add3(): AppMain.playVid(AppMain.d)
        def Add4(): AppMain.playVid(AppMain.e)
        def Add5(): AppMain.playVid(AppMain.f)
        def Add6(): AppMain.playVid(AppMain.g)
        def Add7(): AppMain.playVid(AppMain.h)
        def Add8(): AppMain.playVid(AppMain.i)
        
        def Videos():
            thumbnail_image_size = 6
            btnH = 135
            btnW = 226
            
            NewVideosLabel = ctk.CTkLabel(master=app, text="Videos", font=("Arial", 30))
            
            urlCleansed_A = AppMain.GetThumUrl(AppMain.a)
            imageURL_A = AppMain.showURLImage(urlCleansed_A, thumbnail_image_size)
            
            urlCleansed_B = AppMain.GetThumUrl(AppMain.b)
            imageURL_B = AppMain.showURLImage(urlCleansed_B, thumbnail_image_size)
            
            urlCleansed_C = AppMain.GetThumUrl(AppMain.c)
            imageURL_C = AppMain.showURLImage(urlCleansed_C, thumbnail_image_size)
            
            urlCleansed_D = AppMain.GetThumUrl(AppMain.d)
            imageURL_D = AppMain.showURLImage(urlCleansed_D, thumbnail_image_size)
            
            urlCleansed_E = AppMain.GetThumUrl(AppMain.e)
            imageURL_E = AppMain.showURLImage(urlCleansed_E, thumbnail_image_size)
            
            urlCleansed_F = AppMain.GetThumUrl(AppMain.f)
            imageURL_F = AppMain.showURLImage(urlCleansed_F, thumbnail_image_size)
            
            urlCleansed_G = AppMain.GetThumUrl(AppMain.g)
            imageURL_G = AppMain.showURLImage(urlCleansed_G, thumbnail_image_size)
            
            urlCleansed_H = AppMain.GetThumUrl(AppMain.h)
            imageURL_H = AppMain.showURLImage(urlCleansed_H, thumbnail_image_size)
            
            urlCleansed_I = AppMain.GetThumUrl(AppMain.i)
            imageURL_I = AppMain.showURLImage(urlCleansed_I, thumbnail_image_size)
            
            A = ctk.CTkButton(master=app, text="", command=lambda: AppMain.showVideoDetails(AppMain.a, Add0), image=imageURL_A, height=btnH, width=btnW)
            
            B = ctk.CTkButton(master=app, text="", command=lambda: AppMain.showVideoDetails(AppMain.b, Add1), image=imageURL_B, height=btnH, width=btnW)
            
            C = ctk.CTkButton(master=app, text="", command=lambda: AppMain.showVideoDetails(AppMain.c, Add2), image=imageURL_C, height=btnH, width=btnW)
            
            D = ctk.CTkButton(master=app, text="", command=lambda: AppMain.showVideoDetails(AppMain.d, Add3), image=imageURL_D, height=btnH, width=btnW)
            
            E = ctk.CTkButton(master=app, text="", command=lambda: AppMain.showVideoDetails(AppMain.e, Add4), image=imageURL_E, height=btnH, width=btnW)
            
            F = ctk.CTkButton(master=app, text="", command=lambda: AppMain.showVideoDetails(AppMain.f, Add5), image=imageURL_F, height=btnH, width=btnW)
            
            G = ctk.CTkButton(master=app, text="", command=lambda: AppMain.showVideoDetails(AppMain.g, Add6), image=imageURL_G, height=btnH, width=btnW)
            
            H = ctk.CTkButton(master=app, text="", command=lambda: AppMain.showVideoDetails(AppMain.h, Add7), image=imageURL_H, height=btnH, width=btnW)
            
            I = ctk.CTkButton(master=app, text="", command=lambda: AppMain.showVideoDetails(AppMain.i, Add8), image=imageURL_I, height=btnH, width=btnW)
            
            sidebar = ctk.CTkFrame(master=app, width=200, height=700)
            hyperlink = ctk.CTkButton(sidebar, text="Github", command=lambda: webbrowser.open('https://github.com/TheTechyKid/Skyflix-v4.0.2'), width=180)
            userImgUrl = AppMain.showURLImage("https://icon-library.com/images/avatar-icon/avatar-icon-6.jpg", 5)
            userImage = ctk.CTkLabel(sidebar, image=userImgUrl, text="")
            userName = ctk.CTkLabel(sidebar, text="TheTechyKid", font=("Arial", 15))
            
            NewVideosLabel.place(x=150+120, y=45)
            userImage.place(x=45, y=20)
            sidebar.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
            hyperlink.place(x=10, y=655)
            userName.place(x=50, y=125)
            
            # top row
            A.place(x=70+280*0+175, y=90)
            B.place(x=70+280*1+175, y=90)
            C.place(x=70+280*2+175, y=90)
            
            # middle row
            D.place(x=70+175,        y=90+150)
            E.place(x=70+280*2-105, y=90+150)
            F.place(x=70+280*3-105, y=90+150)
            
            # bottom row
            G.place(x=70+280*0+175, y=90+150*2)
            H.place(x=70+280*1+175, y=90+150*2)
            I.place(x=70+280*2+175, y=90+150*2)

        Videos()
        AppMain.Greating()
    
    @staticmethod
    def Login():
        """Login Screen."""

        name_var=tk.StringVar()
        passw_var=tk.StringVar()

        def outputSignIn():
            Username=name_var.get()
            Password=passw_var.get()

            if Username and Password == Username:
                In = ctk.CTkLabel(master=app, text=" "*6+"correct")
                In.place(x=350+150, y=480)
                AppMain.clear()
                AppMain.HomeScreen()

            elif Username and Password == "":
                In = ctk.CTkLabel(master=app, text=" "*5+"No Value")
                In.place(x=350+150, y=480)

            else:
                In = ctk.CTkLabel(master=app, text=" "*5+"Incorrect")
                In.place(x=350+150, y=480)

            # Clear the Username and Passwords
            name_var.set("")
            passw_var.set("")
            
            os.system("cls")
            print("Skyflix 0 Launched\nGo to my GitHub: https://github.com/TheTechyKid")
        
        app.title("Skyflix Sign in")
        SkyflixImage = tk.Label(app, image = AppMain.SkyflixWord, bg="#242424")
        UserName = ctk.CTkEntry(master=app, width=300, textvariable=name_var)
        PassWord = ctk.CTkEntry(master=app, width=300, textvariable=passw_var, show = '*')
        SignIn = ctk.CTkButton(master=app, text="Sign In", command=outputSignIn)
        
        # Placement
        SkyflixImage.place(x=300+100,y=70)
        UserName.place(x=300+100,y=350)
        PassWord.place(x=300+100,y=400)
        SignIn.place(x=325+50+100,y=450)

    def __init__(self):
        AppMain.Login()
   
if __name__ == "__main__":
    AppMain()   

# Mainloop
app.mainloop()
