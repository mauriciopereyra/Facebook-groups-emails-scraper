<h1>Script used to scrape emails from Facebook groups</h1>
<h2>This script will open comments on facebook groups, then copy the source code, scrape emails from source code and save the scraped emails to a .csv file</h2>

<b>Instructions</b>
1) Open the Facebook group from where you want to get email addresses
2) Scroll down to load several posts (You can use my bash function to scroll down automatically)
3) Copy paste openComments() function into your browser console and run it repeatedly until you see "Finished". This means all links for opening more comments have been clicked.
4) Copy and run sourceCode(), copy the source code you get in the console and then save it to source_code.txt (Create the file)
5) Run this file (main.py) so Python saves the new emails to emails_fb.csv
6) If you want to repeat all the process and load more posts, first copy and run removeElements() in the console
This will remove most of the used posts so your browser can continue working and does not crash because of the big size of the website
Run removeElements() several times until only a few posts are remaining (don't remove them all, leave a few).