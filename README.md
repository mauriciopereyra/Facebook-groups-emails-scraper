<h1>Script for scraping emails from Facebook groups comments</h1>

<h2>Features</h2>

1) This script will open comments on facebook groups 
2) Copy the source code 
3) Scrape emails from source code 
4) Save the scraped emails to a .csv file

<h2>How to use</h2>

1) Open the Facebook group from where you want to get email addresses
2) Scroll down to load several posts
3) Copy paste openComments() function into your browser console and run it repeatedly until you see "Finished". This means all links for opening more comments have been clicked.
4) Copy and run sourceCode(), copy the source code you get in the console and then save it to source_code.txt (Create the file)
5) Run file main.py to save the new emails to the file emails_fb.csv
6) If you want to repeat all the process and load more posts, first copy and run removeElements() in the console
<br>This will remove most of the used posts so your browser can continue working and does not crash because of the big size of the website
<br>Run removeElements() several times until only a few posts are remaining (don't remove them all, leave a few or Facebook will not load more posts).
