
import json
import os
from pprint import pprint
import re

#todo: get username
username = 'kristaisak' 

cur_dir = os.path.dirname(os.path.realpath(__file__))
print(cur_dir)

#todo: get username of the friend and id
dir_file = cur_dir + '/facebook-' + username + '/messages/inbox/danaepapadopetraki_wlomjg8rja/message_1.json'
#todo: loop through all json files

data = json.loads(open(dir_file, encoding="utf8").read().replace('\n', '')) # threads,user
#print(data)

#todo: get the username
USERNAME = "Christina Isakoglou" #TODO: should be given from user


youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
youtube_regex = (r"http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?")
links = []
#look for the link in the "content" node
for i_message in range(0, len(data["messages"])): #len(data["messages"]
    if ('content' in list(data["messages"][i_message].keys())):

        content = data["messages"][i_message]["content"]
        if (re.match(youtube_regex, content)):
            links.append(re.search(youtube_regex, content).group(0))

#print(links)
print(len(links))
#write the links into a text
write_file = open(cur_dir + "\links.txt", "w")
for link in links:
	write_file.write(link +"\n")
write_file.close()