import instaloader

ig =  instaloader.Instaloader()
dp = input("masukkan username :  ")

ig.download_profile(dp,profile_pic_only = True)