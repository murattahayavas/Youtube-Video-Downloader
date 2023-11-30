from pytube import YouTube
from tkinter import Tk,Label,Entry,Button,filedialog

def ytvideo_downloader():
    link=link_entry.get()
    yt=YouTube(link)
    ys=yt.streams.get_highest_resolution()
    file_local=filedialog.askdirectory()
    filename=file_local+"/video.mp4"
    try:
        info_label.config(text="Video yüksek kalitede indirildi.")
    except Exception as e:
        info_label.config(text=f"Hata: {str(e)}")

    yt_download.update()
    ys.download(file_local)

yt_download=Tk()
yt_download.title("YouTube Video İndirme Uygulaması")
yt_download.geometry("500x300")
yt_download.resizable(0,0)
yt_download.configure(bg="light blue")
text_font = ("Boulder", 18, 'bold')
background="light blue"
foreground="black"
border_width=8

label_description=Label(yt_download,text="Download Video", font=text_font,bg=background,fg=foreground)
label_description.grid(row=0,column=0,padx=10,pady=10)

link_entry=Entry(yt_download,font=text_font,bg="white",fg=foreground)
link_entry.grid(row=0,column=1,padx=10,pady=10)

download_button=Button(yt_download,text="Download Now!",font=text_font,bg="green",fg=foreground,command=ytvideo_downloader)
download_button.grid(row=1,column=0,columnspan=2,pady=20)

info_label=Label(yt_download,text="",font=text_font,bg=background,fg=foreground)
info_label.grid(row=2,column=0,columnspan=2,pady=20)


yt_download.mainloop()