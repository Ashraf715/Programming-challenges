import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr


def position(html):
    i = 0
    a = 0
    pos_list=[]
    while a < 10:
        
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)        
        newstring = html[open_tr:close_tr]
        lookingfor = '"position">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</', pos_start)
        i = close_tr
        a+=1
        answer_p =newstring[pos_start+len(lookingfor):pos_end]
        pos_list.append(answer_p)
    return pos_list
        

       

def n_artist(html):
    list_artist = []
    b = 0
    name = 0
    while b <10:        
        open_tr = html.find("<tr>", name)
        close_tr = html.find("</tr>", open_tr)    
        newstring = html[open_tr:close_tr]
        lookingfor = '"artist">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find("</", pos_start)
        name=close_tr 
        b +=1        
        entire = newstring[pos_start:pos_end]
        y = entire.partition('/">')[2]
        list_artist.append(y)        
    return list_artist

def songs(html):
    list_song = []
    i = 0
    c = 0
    end = html.find("CENTRAL CEE")
    while c < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
        newstring = html[open_tr:close_tr]
        lookingfor = '"title">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</', pos_start)
        i = close_tr
        c += 1
        entire = (newstring[pos_start:pos_end])
        songz= entire.partition('/">')[2]
        list_song.append(songz)
    return list_song
        
if __name__ == "__main__":
    html = scrape(url)

    print(f"""{'Position':^30}|{'Artist':^30}|{'Song':^30}|
---------------------------------------------------------------------------------------------
""")
    for x in range(0, 10):
        print(f"""{position(html)[x]:^30}{n_artist(html)[x]:^35}{songs(html)[x]:^34}
------------------------------|------------------------------|------------------------------|""")






