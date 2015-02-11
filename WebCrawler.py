index = []
def add_to_index(index, keyword, url):
    for e in index:
        if (keyword == e[0]):
            e[1].append(url)
            return index
    tmp = []
    tmplist = []
    tmplist.append(url)
    tmp.append(keyword)
    tmp.append(tmplist)
    index.append(tmp)
    return index

def lookup(index, keyword):
    response = []
    for e in index:
        if(e[0] == keyword):
            for u in e[1]:
                response.append(u)
    return response

def add_page_to_index(index, url, content):
    keywords = content.split()
    for keyword in keywords:
        add_to_index(index, keyword, url)
    return index



def union(flist, slist):
    for e in slist:
        if(e not in flist):
            flist.append(e)
    return flist, slist

def get_next_target(s):
    start_link  = s.find('<a href=')
    if(start_link != -1):
        start_quote = s.find('"', start_link)
        end_quote   = s.find('"', start_quote+1)
        url         = s[start_quote+1:end_quote]
        return url, end_quote
    else:
        return None, 0

def get_all_links(page):
    links = []
    while (True):
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""



#print get_all_links(get_page('http://www.udacity.com/cs101x/index.html'))

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if (page not in crawled):
            content = get_page(page)
            add_page_to_index(index, page, content)
            union (tocrawl, get_all_links(content))
            crawled.append(page)
    return index

#print crawl_web('http://www.udacity.com/cs101x/index.html')