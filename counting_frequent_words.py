import webbrowser,requests
import bs4

counter = 0
strcount = {}
res = requests.get('https://en.wikipedia.org/wiki/Areas_of_mathematics')
bs4obj = bs4.BeautifulSoup(res.content, 'html.parser')
strchunk = bs4obj.get_text()
lcasestrchunk = strchunk.lower().split()
alphachunk = []

### This code is to remove any word that are non alphabetical characters.
for i in range(len(lcasestrchunk)) :
    if lcasestrchunk[i].isalpha():
        alphachunk.append(lcasestrchunk[i])



for i in range(len(alphachunk)):
    strcount.setdefault(alphachunk[i],0)
    strcount[alphachunk[i]]+=1


print( (sorted(strcount.items(), key = lambda t:t[1], reverse=True)[:10]))

    


    
    
        
        



