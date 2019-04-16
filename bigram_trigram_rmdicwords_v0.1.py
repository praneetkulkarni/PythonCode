import webbrowser,requests
import bs4



def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

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
nondictchunk = []
if __name__ == '__main__':
        english_words = load_words()
### This code is to remove dictionay words
for i in range(len(lcasestrchunk)) :
    if lcasestrchunk[i].isalpha():
        if lcasestrchunk[i] not in english_words:
            #print(lcasestrchunk[i])
            nondictchunk.append(lcasestrchunk[i])
        


#print(nondictchunk)



biagramcounter =0
triagramcounter =0
innterloop =1
biagram = []
triagram = []
d = ()
t = ()

while(biagramcounter< (len(nondictchunk)-1)):
    d = (nondictchunk[biagramcounter],nondictchunk[biagramcounter+1])
    biagram.append(d)
    biagramcounter = biagramcounter+1
    
#print(biagram)
triagramcounter = 0    
while(triagramcounter< (len(nondictchunk)-2)):
    t = (nondictchunk[triagramcounter],nondictchunk[triagramcounter+1],nondictchunk[triagramcounter+2])
    triagram.append(t)
    triagramcounter = triagramcounter+1

#print(triagram)
ngrams_dictonary(biagram)
ngrams_dictonary(triagram)

