#!/usr/bin/env python3
# Skyflix 0.py

import tkinter as tk
import customtkinter as ctk
from pytube import YouTube
import pathlib
import random
import requests
import os
from PIL import Image, ImageTk
from io import BytesIO
import webbrowser
from youtubesearchpython import SearchVideos
import random
import scrapetube

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# App
app = ctk.CTk()
app.geometry("1100x700")
app.title("Skyflix 0")
app.resizable(False, False)

# Main class
class AppMain():
    """Main App Class. Version 5.0.2."""
    
    # Image vars
    SkyflixWord = tk.PhotoImage(file=pathlib.PurePath(r"Images\SkyFlix.png"))
    HomeWord = tk.PhotoImage(file=pathlib.PurePath(r"Images\Home.png"))
    SettingsWord = tk.PhotoImage(file=pathlib.PurePath(r"Images\Settings.png"))
    sideBarImage = tk.PhotoImage(file=pathlib.PurePath(r"Images\Side Bar.png"))
    ProfilePic = tk.PhotoImage(file=pathlib.PurePath(r"Images\profile pic.png"))
    
    # Channel lists
    channels = [
                "https://www.youtube.com/@Danny-Gonzalez",
                "https://www.youtube.com/@ryan",
                "https://www.youtube.com/@NetworkChuck",
                "https://www.youtube.com/user/mrbeast6000",
                "https://www.youtube.com/@DailyDoseOfInternet",
                "https://www.youtube.com/@danielthrasher",
                "https://www.youtube.com/@ThatMumboJumbo",
                "https://www.youtube.com/@Logdotzip",
                "https://www.youtube.com/@jacksepticeye"
                ]
    
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
        ranComliment = random.choice(compliments)
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
        """Clear all th wigets in the screen."""
        
        for widgets in app.winfo_children():
            widgets.destroy()
    
    @staticmethod
    def playVid(url):
        """Play the video."""

        data = url.replace("https://www.youtube.com/watch?v=", "")

        javascript_code = f"""var pythonData = '{str(data)}';
        var videoFrame = document.getElementById('video');
        if (videoFrame) {{
            videoFrame.src = 'https://www.youtube.com/embed/' + pythonData;
        }}
        """
        
        with open('data.js', 'w') as f:
            f.write(javascript_code)

        file_path = r'C:\Users\Gianclarence Solas\Desktop\python books\Skyflix\videoPlayer.html'
        print(file_path)
        browser = webbrowser.get('"C:/Program Files/Google/Chrome/Application/chrome.exe" %s')
        browser.open(file_path)
    
    @staticmethod
    def getLastestVid(channel):
        """Get the lastest video from a youtube channel."""
        
        video_list = []
        videos = scrapetube.get_channel(channel_url=channel, limit=4)

        for video in videos:
            video_list.append(video['videoId'])
            
        random_video = random.choice(video_list)
        return "https://www.youtube.com/watch?v="+random_video
    
    @staticmethod
    def showURLImage(url, size):
        image_url = YouTube(url).thumbnail_url
        response = requests.get(image_url)
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

        imageURL = AppMain.showURLImage(url, 3)
        image_label = tk.Label(app, image=imageURL)
        
        Title = ctk.CTkLabel(master=app, text=AppMain.ShortenTitle(YouTube(url).title), font=("Arial", 35))
        
        DesTitle = ctk.CTkLabel(master=app, text="Description", font=("Arial", 20))
        Decription = ctk.CTkTextbox(master=app, height=300, width=500)
        buttonplay = ctk.CTkButton(master=app, text="Play", width=530, command=num)
        back = ctk.CTkButton(master=app, text="<--", command=AppMain.HomeScreen, width=50)
        
        # Insert Decription
        Decription.insert("0.0", f"""{AppMain.getDes(url)}""")
        
        # Placement
        image_label.pack()
        Title.pack()
        buttonplay.place(x=530, y=140 + 230)
        DesTitle.place(x=10, y=190 + 220)
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
        
        def sideBar():
            SideBar = tk.Label(app, image = AppMain.sideBarImage, bg="#242424")
            SideBar.place(x=-2, y=-2)
        
        def Icon():
            LabelPic = tk.Label(app, image=AppMain.ProfilePic, bg="#3C3C3C")
            LabelPic.place(x=17, y=10)
        
        def Videos():
            NewVideosLabel = ctk.CTkLabel(master=app, text="Videos", font=("Arial", 25))
            
            A = ctk.CTkButton(master=app, text=AppMain.ShortenTitle(AppMain.getTitle(AppMain.a)), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.a, Add0))
            B = ctk.CTkButton(master=app, text=AppMain.ShortenTitle(AppMain.getTitle(AppMain.b)), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.b, Add1))
            C = ctk.CTkButton(master=app, text=AppMain.ShortenTitle(AppMain.getTitle(AppMain.c)), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.c, Add2))
            D = ctk.CTkButton(master=app, text=AppMain.ShortenTitle(AppMain.getTitle(AppMain.d)), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.d, Add3))
            E = ctk.CTkButton(master=app, text=AppMain.ShortenTitle(AppMain.getTitle(AppMain.e)), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.e, Add4))
            F = ctk.CTkButton(master=app, text=AppMain.ShortenTitle(AppMain.getTitle(AppMain.f)), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.f, Add5))
            G = ctk.CTkButton(master=app, text=AppMain.ShortenTitle(AppMain.getTitle(AppMain.g)), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.g, Add6))
            H = ctk.CTkButton(master=app, text=AppMain.ShortenTitle(AppMain.getTitle(AppMain.h)), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.h, Add7))
            I = ctk.CTkButton(master=app, text=AppMain.ShortenTitle(AppMain.getTitle(AppMain.i)), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.i, Add8))
            
            NewVideosLabel.place(x=70+280*0+100, y=120)
            
            # top row
            A.place(x=70+280*0+100, y=170)
            B.place(x=70+280*1+100, y=170)
            C.place(x=70+280*2+100, y=170)
            
            # middle row
            D.place(x=70+100, y=170+50)
            E.place(x=70+280*2-180, y=170+50)
            F.place(x=70+280*3-180, y=170+50)
            
            # bottom row
            G.place(x=70+280*0+100, y=170+100)
            H.place(x=70+280*1+100, y=170+100)
            I.place(x=70+280*2+100, y=170+100)
        
        sideBar()
        Icon()
        HomeImage = tk.Label(app, image = AppMain.HomeWord, bg="#242424")
        Videos()
        AppMain.Greating()
        
        HomeImage.place(x=350+150, y=40)
    
    @staticmethod
    def Login():
        """Login Screen."""

        name_var=tk.StringVar()
        passw_var=tk.StringVar()

        def outputSignIn():
            Username=name_var.get()
            Password=passw_var.get()

            if Username and Password == "a":
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
