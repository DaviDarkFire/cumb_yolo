import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import os

def detect_img(annotation_path_val, yolo):
    with open(annotation_path_val) as f:
        lines_val = f.readlines()

    n = len(lines_val)
    all_time = []
    for i in range(n):
        #img = '/home/lavicom/datasets/dataset_Pantanal/anta/Visual/DC_5030.jpg'
        img = lines_val[i].split(',')[0]
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image, exec_time = yolo.detect_image(image, txtpath=os.path.basename(img)[:-3] + 'txt')
            #r_image.show()
            all_time.append(exec_time)
            print(all_time)
            r_image.save(os.path.basename(img))
    print(exec_time)
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''

    parser.add_argument(
        '--path', type=str,
        help='path to txt test file'
    )

    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    FLAGS = parser.parse_args()

    detect_img(FLAGS.path, YOLO(**vars(FLAGS)))