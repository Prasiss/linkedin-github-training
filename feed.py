import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml','r') as file:
    yaml_data =yaml.safe_load(file)

    rss_element = xml_tree.Element('rss',{
        'version':'2.0' ,
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.dtd' ,
        'xmlns:content' : 'http://purl.org/rss/1.0/modules/content/'
    }) 

#add the first line of code which includes the version and links to the websites 
channel_element =xml_tree.SubElement(rss_element,'channel')
#gets the link and necessary data from the files which was stored in the yamal_data attribute which we described before
#  
link=yaml_data['link']

xml_tree.SubElement(channel_element,'title').text =yaml_data['title']
xml_tree.SubElement(channel_element,'format').text =yaml_data['format']
xml_tree.SubElement(channel_element,'subtitle').text =yaml_data['subtitle']
xml_tree.SubElement(channel_element,'itunes:author').text =yaml_data['author']
xml_tree.SubElement(channel_element,'description').text =yaml_data['description']
xml_tree.SubElement(channel_element,'itunes:image',{'href': link + yaml_data['image']}) 
xml_tree.SubElement(channel_element,'languge').text =yaml_data['language']
xml_tree.SubElement(channel_element,'link').text =link
# xml_tree.SubElement(channel_element,'title').text =yaml_data['title']


output_tree =xml_tree.ElementTree(rss_element)

output_tree.write('podcast.xml',encoding ='UTF-8' , xml_declaration=True)
