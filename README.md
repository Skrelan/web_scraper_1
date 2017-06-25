#Specific web scraper

Requirments:
⋅⋅* Python 2.7 
⋅⋅* pip (https://pip.pypa.io/en/stable/installing/)
⋅⋅* BeautifulSoup (to download this open up terminal and write sudo pip install BeautifulSoup)


⋅⋅* Step 1: go to the website using your browser (chrome)
⋅⋅* Step 2: right click inspect
⋅⋅* Step 3: scroll all the way down, untill there are no more elements that load
⋅⋅* Step 4: right click the last element and chose inspect
⋅⋅* Step 5: in the code that pops up scroll up to parent, <table id="jq-regular-exhibitors" class="mys-results mys-zebra mys-hover"> (_see parse/example.html to see what the copy paste should look like_)
⋅⋅* Step 6: close the parent and right click copy it
⋅⋅* Step 7: Store that in parse/temp.html
⋅⋅* Step 8: Open terminal and run python index.py
⋅⋅* Step 9: Once the script finishes running, go to output/ folder and your file should be there
⋅⋅* Step 10: Have a shot of Tequila

works only for URL http://ebace17.mapyourshow.com/7_0/alphalist.cfm?alpha=*'