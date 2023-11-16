from pyquery import PyQuery as pq
doc = pq(filename='my-search-engine.html')
print(doc('li'))