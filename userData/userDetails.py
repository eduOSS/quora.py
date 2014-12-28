# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

def getTopicName(topic):
    if topic is not None:
        return str(topic.find('span', attrs={'class' : 'TopicName'}).text)
    else:
        return 'NA'
    
def getName(soup):
    return str(soup.find('span', attrs={'class' : 'user'}).string)

def getLocation(soup):
    location = soup.find('div', attrs={'class' : 'ProfileLocationEditor ProfileTopicEditor'})
    return getTopicName(location)

def getEducation(soup):
    education = soup.find('div', attrs={'class' : 'ProfileTopicEditor ProfileEducationEditor'})
    return getTopicName(education)

def getEmployment(soup):
    employment = soup.find('div', attrs={'class' : 'ProfileWorkEditor ProfileTopicEditor'})
    return getTopicName(employment)

def getTopics(soup):
    topics = soup.find('div', attrs={'class' : 'ProfileExpertiseEditor ProfileTopicEditor'})
    knowsAbout = "NA"
    if topics is not None:
        knowsAbout = []
        topics = topics.find_all('span', attrs={'class' : 'TopicName'})
        i = 1
        for topic in topics:
            if i > 3:
                break
            else: 
                knowsAbout.append(str(topic.text))
            i += 1
    return str(knowsAbout)

def getUserDetails(username):
    try:
        soup = BeautifulSoup(urllib2.urlopen('http://www.quora.com/' + username + '/about'))
        name = getName(soup)
        location = getLocation(soup)
        education = getEducation(soup)
        employment = getEmployment(soup)
        topics = getTopics(soup)
         
        stats = soup.find_all('span', attrs={'class' : 'profile_count'})  
        userDetails = {
                       'username'  : username,
                       'name'      : name,
                       'location'  : location,
                       'education' : education,
                       'employment': employment,
                       'topics'    : topics,
                       'questions' : str(stats[0].text),
                       'answers'   : str(stats[1].text),
                       'posts'     : str(stats[2].text),
                       'followers' : str(stats[3].text),
                       'following' : str(stats[4].text),
                       'edits'     : str(stats[5].text)
                       }
        return userDetails
    except:
        print "Username Not Found"

if __name__ == '__main__':
    username = raw_input("Enter Username : ")
    userDetails = getUserDetails(username)
    if userDetails is not None:
        for detail in userDetails:
            print detail + " : " + userDetails[detail]