from xml.dom import minidom
import os
import numpy as np
from shutil import copyfile
from PIL import Image

			
def generate_xml2txt(path='cumbaru_26_agosto_2018', txtpath='cumbaru_26_agosto_2018.txt'):

	xmls = [f for f in os.listdir(path) if f.endswith('.xml')]
	text_file = open(txtpath, "w")

	for xml in xmls:
		mydoc = minidom.parse(os.path.join(path, xml))
		filename = mydoc.getElementsByTagName('filename')[0].firstChild.data.encode("utf-8")
		imgpath = os.path.join(path,xml[:-3]+'JPG')
		objects = mydoc.getElementsByTagName('object')
		text_file.write('%s' % (os.path.abspath(imgpath)))
		for obj in objects:
			name = obj.getElementsByTagName("name")[0].firstChild.data.encode("utf-8").lower()
			class_id = 0
			bndbox = obj.getElementsByTagName("bndbox")[0]
			xmin = bndbox.getElementsByTagName("xmin")[0].firstChild.data.encode("utf-8")
			ymin = bndbox.getElementsByTagName("ymin")[0].firstChild.data.encode("utf-8")
			xmax = bndbox.getElementsByTagName("xmax")[0].firstChild.data.encode("utf-8")
			ymax = bndbox.getElementsByTagName("ymax")[0].firstChild.data.encode("utf-8")
			text_file.write(' %s,%s,%s,%s,%d' % (xmin,ymin,xmax,ymax,class_id))
		text_file.write('\n')

	text_file.close()

generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_0/train', 'folder_0_train.txt')
generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_0/val', 'folder_0_val.txt')
generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_0/test', 'folder_0_test.txt')

generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_1/train', 'folder_1_train.txt')
generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_1/val', 'folder_1_val.txt')
generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_1/test', 'folder_1_test.txt')

generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_2/train', 'folder_2_train.txt')
generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_2/val', 'folder_2_val.txt')
generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_2/test', 'folder_2_test.txt')

generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_3/train', 'folder_3_train.txt')
generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_3/val', 'folder_3_val.txt')
generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_3/test', 'folder_3_test.txt')

generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_4/train', 'folder_4_train.txt')
generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_4/val', 'folder_4_val.txt')
generate_xml2txt('/home/aluno/Experimentos_cumbaru/cumbarus_folders/folder_4/test', 'folder_4_test.txt')
