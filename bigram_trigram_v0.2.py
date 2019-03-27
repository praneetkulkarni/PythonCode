import webbrowser,requests
import bs4



def ngrams_dictonary(ngram_list):
    ngram_dict = {}
    for i in range(len(ngram_list)):
        ngram_dict.setdefault(ngram_list[i],0)
        ngram_dict[ngram_list[i]]+=1
    print( (sorted(ngram_dict.items(), key = lambda t:t[1], reverse=True)[:10]))
    

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


#print(alphachunk)
biagramcounter =0
triagramcounter =0
innterloop =1
biagram = []
triagram = []
d = ()
t = ()

while(biagramcounter< (len(alphachunk)-1)):
    d = (alphachunk[biagramcounter],alphachunk[biagramcounter+1])
    biagram.append(d)
    biagramcounter = biagramcounter+1
    
#print(biagram)
triagramcounter = 0    
while(triagramcounter< (len(alphachunk)-2)):
    t = (alphachunk[triagramcounter],alphachunk[triagramcounter+1],alphachunk[triagramcounter+2])
    triagram.append(t)
    triagramcounter = triagramcounter+1

#print(triagram)
ngrams_dictonary(biagram)
ngrams_dictonary(triagram)



