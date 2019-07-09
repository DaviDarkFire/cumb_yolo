import csv
import yaml
import os
import numpy as np
import random

txtpath = 'all.txt'
txtpath_train = 'train.txt'
txtpath_val = 'val.txt'
pathImages = '/home/dnunes/datasets/FOTOS_DRONE'
all_classes = ['isolador', 'poste', 'cruzeta']

with open('poste-energisa.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	rows = list(reader)
	totalrows = len(rows)
	n_train = int(totalrows * 0.9)
	n_val = totalrows - n_train
	train_val = np.append(np.zeros(n_train), np.ones(n_val))
	random.shuffle(train_val)

	text_file = open(txtpath, "w")
	text_file_train = open(txtpath_train, "w")
	text_file_val = open(txtpath_val, "w")
	img_names = []
	for i, row in enumerate(rows):
		img_name = row['External ID']
		imgpath = os.path.join(pathImages, img_name)
		#print(img_name)
		if row['Label'] == 'Skip': continue
		labels = yaml.load(row['Label'])
		classes = labels.keys()

		if img_name in img_names:
			print(' Imagens com nomes iguais: %s\n' % img_name)
			continue
		img_names.append(img_name)

		text_file.write('%s' % (imgpath))
		if train_val[i] == 0:
			text_file_train.write('%s' % (imgpath))
		else:
			text_file_val.write('%s' % (imgpath))
		for c in classes:
			class_id = all_classes.index(c)
			anno = labels[c]
			for a in anno:
				canto_superior = a['geometry'][0]
				canto_inferior = a['geometry'][2]
				xmin = canto_superior['x']
				ymin = canto_superior['y']
				xmax = canto_inferior['x']
				ymax = canto_inferior['y']
				text_file.write(' %d,%d,%d,%d,%d' % (xmin,ymin,xmax,ymax,class_id))
				if train_val[i] == 0:
					text_file_train.write(' %d,%d,%d,%d,%d' % (xmin,ymin,xmax,ymax,class_id))
				else:
					text_file_val.write(' %d,%d,%d,%d,%d' % (xmin,ymin,xmax,ymax,class_id))
		text_file.write('\n')
		if train_val[i] == 0:
			text_file_train.write('\n')
		else:
			text_file_val.write('\n')
	text_file.close()
	text_file_train.close()
	text_file_val.close()


