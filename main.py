### Facebook groups emails scraper
# Scripts used to scrape emails from Facebook groups

### Instructions
# 1) Open the Facebook group from where you want to get email addresses
# 2) Scroll down to load several posts (You can use my bash function to scroll down automatically)
# 3) Copy paste openComments() function into your browser console and run it repeatedly until you see "Finished". This means all links for opening more comments have been clicked.
# 4) Copy and run sourceCode(), copy the source code you get in the console and then save it to source_code.txt (Create the file)
# 5) Run this file (main.py) so Python saves the new emails to emails_fb.csv
# 6) If you want to repeat all the process and load more posts, first copy and run removeElements() in the console
# This will remove most of the used posts so your browser can continue working and does not crash because of the big size of the website
# Run removeElements() several times until only a few posts are remaining (don't remove them all, leave a few).


# (Optional) Bash function to scroll down every 4 seconds and load more posts (Run it on bash and then change window to the browser)
# while true; do xdotool key --delay 4000 End; done


'''
/* Open comments */




function openComments() {


function sleepFor( sleepDuration ){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration){ /* do nothing */ } 
}


spans = document.getElementsByTagName("span")

re_list = []

re_list.push(new RegExp("^View previous comment(s)*$"))
re_list.push(new RegExp("^View( )*(\\d)* more comment(s)*$"))
re_list.push(new RegExp("^View previous comment(s)*$"))
re_list.push(new RegExp("^View( )*(\\d)* more (reply|replies)$"))
re_list.push(new RegExp("^(\\d)+ (reply|replies)$"))

clicked = []


for (var i = 0; i < spans.length; i++) {
    for (var j = 0; j < re_list.length; j++) {
        if (re_list[j].test(spans[i].textContent)) {
        console.log("Clicking:",spans[i].textContent)
        spans[i].scrollIntoView();
        sleepFor(2000)
        spans[i].click();

        clicked.push(spans[i]);
        
        }
    }
}
    
if (clicked.length == 0) {
    return "Finished. No more comments to open. Please scroll down to load more posts or run sourceCode() to get current source code."
} else {
    return "All comments opened. Please run openComments() again to open more."
}

}

/* Open comments */
'''




'''
/* Remove used elements */

function removeElements(){

var feed = document.querySelectorAll('[role="feed"]')[0];

var divs = feed.childNodes;

if (divs.length > 2) {
    for (var i = 0; i < divs.length-2; i++) {
        console.log(i)
        console.log(divs.length)
        divs[i].remove();
    }    
} else {
    console.log("Finished")
}


}

/* Remove used elements */
'''




'''
function sourceCode(){
    console.log(document.body.innerHTML)
}

'''



import os

# Function to scrape emails from source_code.txt and save the new ones to emails_fb.csv (It will ignore duplicated ones)
def main():
    import re
    import csv

    # Create needed files if they don't exist
    if not os.path.exists('source_code.txt'):
        with open('source_code.txt', 'w'):
            print("Created source_code.txt")
    if not os.path.exists('emails_fb.csv'):
        with open('emails_fb.csv', 'w'):
            print("Created emails_fb.csv")

    with open('source_code.txt', 'r', errors="ignore") as file:
        line = file.read()

    new_emails = re.findall(r'[\w\.-]+@[\w\.-]+', line) # Regex to get emails
    print(len(new_emails),'emails from facebook group')

    add_emails = []


    with open('emails_fb.csv', 'r',errors="ignore") as csvFile:
        reader = csv.reader(csvFile)
        old_emails = [email[0] for email in reader]
        print('Old emails',len(old_emails))

        for email in new_emails:
            if email in old_emails:
                # DUPLICATED email
                pass
            else:
                # NEW email
                old_emails.append(email)
                add_emails.append(email)

    print('New emails',new_emails)#len(new_emails)
    print('Added emails',len(add_emails))
    print('Total emails',len(old_emails))


    with open('emails_fb.csv','a', newline='') as fd:
        for email in add_emails:
            writer = csv.writer(fd)
            writer.writerow([email])

        print('Successfully written file')


# js_function()
main()


