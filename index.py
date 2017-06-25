import xml.etree.ElementTree
import urllib

web_site = 'http://ebace17.mapyourshow.com{0}'
end_point = 'http://ebace17.mapyourshow.com/7_0/alphalist.cfm?alpha=*'
file_name = 'parse/temp.html'

anchors = []
html_classes = [
	'<p class="sc-Exhibitor_PhoneFax">',
	'<p class="sc-Exhibitor_Address">',
	'<div class="sc-Exhibitor_SocialMedia">',
	'<h1 class="sc-Exhibitor_Name">']


def parse_parent_page(file_name):
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
	
	def child_open(web_url):
		try:
			data = urllib.urlopen(web_url)
			return data

		except Exception as e:
			print "Please check the web_url"
			print e
			return False


	def child_write_file(data,web_url):
		try:
			with open('parse/temp_a.html','wb') as fd:
				for line in data:
					fd.write(line)

		except Exception as e:
			print "anchor failed"
			print web_url
			return False


	def child_html_parse(data,web_url):
		client_info = {
			'name':None,
			'address':None,
			'phone_number':None,
			'link' : None
		}
		for line in data:
			line = line.strip()


	data = child_open(web_url)
	if not data:
		return
	child_write_file(data,web_url)



def main():
	if not parse_parent_page(file_name):
		print "Error"
		return

	for link in anchors:
		print link
		parse_child_page(link)

if __name__ == '__main__':
	#print wrapper()
	main()