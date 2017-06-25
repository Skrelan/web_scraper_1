import xml.etree.ElementTree
import urllib
from BeautifulSoup import BeautifulSoup as soup
import csv
import datetime

"""
ALL THE CONFIGS
"""
web_site = 'http://ebace17.mapyourshow.com{0}'
end_point = 'http://ebace17.mapyourshow.com/7_0/alphalist.cfm?alpha=*'
file_name = 'parse/temp.html'

anchors = [] #stores all the anchor tags
client_data = [] #stores the end result
html_classes = {
	'phone_number' : ['sc-Exhibitor_PhoneFax','p'],
	'address': ['sc-Exhibitor_Address','p'],
	'social_media' : ['sc-Exhibitor_SocialMedia','div'],
	'name': ['sc-Exhibitor_Name','h1'],
	'link': ['sc-Exhibitor_Url','p']}


def parse_parent_page(file_name):
	"""
	About: This function parses the parent page and stores all the 
		   links pointing to the vendors
		Args: file_name (str)
		Returns: Bool
	"""
	try:
		with open(file_name, 'r') as fd:
			for line in fd:
				line = line.strip()
				if line.startswith('<a href="/7_0/exhibitor/'):	
					anchors.append(web_site.format(line[line.find('href=')+6:-2]))
					#print line 

		return True
	except Exception as e:
		print "Something broke while writing the file"
		print e
		return False


def parse_child_page(web_url):
	"""
	About: This function is recursively called and parses 
		    the pages whoes url is given to it 
		Args: web_url (str)
		Returns: None
	"""
	
	def child_open(web_url):
		"""
		About: This is a helper function which loads the html
			   of the passed url
			Args: web_url (str)
			Returns
		"""
		try:
			data = urllib.urlopen(web_url)
			result = data.read()
			data.close()
			return result

		except Exception as e:
			print "Please check the web_url"
			print e
			return False


	def child_html_parse(data,web_url):
		"""
		About: This is a helper function which parses the html
			   using the keys and values for the python dict 
			   named html_classes
			Args: data (str), web_url (str)
			Returns: None
		"""
		client_info = {
			'name':None,
			'address':None,
			'phone_number':None,
			'link' : None
		}
		#t=  BeautifulSoup(html).findChildren("p", { "class" : "sc-Exhibitor_PhoneFax" })
		page_soup = soup(data)
		for key in client_info.keys():
			try:
				client_info[key] = page_soup.findAll(html_classes[key][1], {"class" : html_classes[key][0]})[0].text.encode('utf-8')
			except Exception as e:
				print "{0} key failed for link {1}".format(key,web_url)
		client_data.append(client_info)

	html = child_open(web_url)
	if not html:
		return
	child_html_parse(html,web_url)


def dict_to_csv(dict_data):
	"""
	About: This function writes the dict data into an csv
		Args: dict_data (dict)
		Returns: None
	"""
	ts = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	keys = client_data[0].keys()
	with open('output/data{0}.csv'.format(ts),'wb') as output:
		dict_writer = csv.DictWriter(output,keys)
		dict_writer.writeheader()
		dict_writer.writerows(dict_data)


def main():
	"""
	About: This is the main function, it runs all the above logic
		Args: None
		Returns: None
	"""
	if not parse_parent_page(file_name):
		print "Error"
		return

	for link in anchors:
		print link
		parse_child_page(link)

	dict_to_csv(client_data)

if __name__ == '__main__':
	main()