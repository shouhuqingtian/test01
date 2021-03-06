# -*- coding:utf-8 -*-
import random
import string
from util.unti_time import strtime, local_doc
import datetime
import logging.handlers
from PIL import Image
from util.chaojiying import Chaojiying_Client


def get_code(driver, id):  # 获取验证码照片
    # 保存截图
    picture_name1 = local_doc() + '/screenshots/' + str(strtime()) + '.png'
    driver.save_screenshot(picture_name1)
    ce = driver.find_element_by_id(id)
    # 显示器比例分辨率
    k = driver.execute_script('return window.devicePixelRatio')
    left = int(ce.location['x'] * k)
    top = int(ce.location['y'] * k)
    right = int(ce.size['width'] * k) + left
    height = int(ce.size['height'] * k) + top
    # 保存验证码图片
    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height))
    picture_name2 = local_doc() + '/screenshots/' + str(strtime()) + '.png'
    img.save(picture_name2)
    chaojiying = Chaojiying_Client('shouhuqingtian', '13691959110', '96001')
    im = open(picture_name2, 'rb').read()
    code_value = chaojiying.PostPic(im, 1902)
    code = code_value['pic_str']
    return code


def gen_random_str():  # 随机生成字符串
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str


def get_logger():
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    rf_handler = logging.handlers.TimedRotatingFileHandler(local_doc() + '/logs/' + 'all.log', when='midnight',
                                                           interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0), encoding='utf-8')
    rf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    f_handler = logging.FileHandler(local_doc() + '/logs/' + 'error.log', encoding='utf-8')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s'))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger
