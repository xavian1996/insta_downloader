import os
import notify2


profile = input("PROFILE NAME => ")
  
def notify():
    
    notify2.init('INSTA DOWNLOADER')
    n = notify2.Notification("INSTA DOWNLOADER",
                         "Finished Downloading " + profile + " Pics",
                         "insta.jpg"   # Icon name
                        )
    n.show()
    
def insta_down():
  
    
    download = os.system(f"instaloader {profile} ")
    
    if download:
        print(profile,"PICS DOWNLOADED !")
    notify()
    
    
insta_down()