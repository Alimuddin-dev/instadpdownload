# ini adalah program sederhana menggunakan python
# program ini untuk mendownload foto profile instagram
# by Alimuddin-dev
import instaloader

ig =  instaloader.Instaloader()
dp = input("masukkan username :  ")

ig.download_profile(dp,profile_pic_only = True)