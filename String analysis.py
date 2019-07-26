import re

lyrics="""Imagine there's no Heaven #the string to be analysed
It's easy if you try
No Hell below us
Above us only sky

Imagine all the people
Living for today
Aaa haa

Imagine there's no countries
It isn't hard to do
Nothing to kill or die for
And no religion too

Imagine all the people
Living life in peace
Yoo hoo

You may say I'm a dreamer
But I'm not the only one
I hope someday you'll join us
And the world will be as one

Imagine no possessions
I wonder if you can
No need for greed or hunger
A brotherhood of man

Imagine all the people
Sharing all the world
Yoo hoo

You may say I'm a dreamer
But I'm not the only one
I hope someday you'll join us
And the world will live as one
"""
lyrics.strip()
lylist1=re.split(" |\n",lyrics) #to use more than one delimiter
#print(lylist1)
lylist=[]
n1=len(lylist1)
n=0
count=0
freq={}
f=0
for x in range(n1):
    if lylist1[x]!="":
        lylist.append(lylist1[x])
        n+=1
    else:
        continue
print("Printing the list of all words in the string.")
print(lylist)
l=lylist[0]
ulist=[]
for k in lylist:
   if k not in ulist:
        ulist.append(k)
print("Printing the list of words without redundancy.")
print(ulist)
nu=len(ulist)
print("Printing all the unique words.")
for t in ulist:
    for p in lylist:
        if t==p:
            f+=1
    if f==1:
        count+=1
        print(t)

    freq[t]=f
    f=0
print("No. of unique words:",count)
for str in freq:
    if freq[str]>freq[l]:
        l=str
    #elif freq[str]==1:
        #print(str,1)
    else:
        continue
print("Most frequent word is:",l,',',freq[l],'times')






