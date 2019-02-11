import webbrowser

ans = input('''
Juice File Manager 4.0 Websites
=======================================
Which Website Would You Like To Go To?

1. JFM Home Page

2. Enders Blog

#: ''')

if ans == '1':
  webbrowser.open('https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal', new=1)

if ans == '2':
  webbrowser.open('https://endernightlord-chromebook.github.io/EnderNightLord-Web.io/', new=1)
