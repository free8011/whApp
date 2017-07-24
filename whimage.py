#-*- coding: utf-8 -*-
import os
import sys
import urllib
import urlparse
from PIL import Image, ImageOps
from api import whAPI
reload(sys)
sys.setdefaultencoding('utf-8')

class Whimage:
    def __init__(self, parent=None):
        self.ofile = ''
        self.tfile = ''
        self.mask = './image/mask.png'

    def circular(self,ofile='', output='',mask=''):
        if not os.path.exists(os.path.dirname(output)):
            os.makedirs(os.path.dirname(output))

        if mask == '':
            mask = self.mask
        alpha = Image.open(mask).convert('L')
        # im = Image.open(ofile.decode('utf8'))
        im = Image.open(ofile)
        outputimg = ImageOps.fit(im, alpha.size, centering=(0.5, 0.5))
        outputimg.putalpha(alpha)
        outputimg.save(output)
        return outputimg

    def getUserThumbnail(self,host='',rootdir='',corpPrefix='', userId=''):
        url = 'http://%s/dat/img/photo_%s.png' % (host, userId)
        rootpath = (os.path.join(rootdir,corpPrefix,'images','users','source'))
        filename = 'photo_%s.png'%userId
        if not os.path.exists(rootpath):
            os.makedirs(rootpath)
        imagePath = os.path.join(rootpath,filename)
        urllib.urlretrieve(url, imagePath)
        return  imagePath

    # def getThumbnail(self,host='',rootdir='',corpPrefix='', type='shot', ):
    def getThumbnail(self,env ,url=''):
        # host = self.env.ShotName, corpPrefix = self.env.Company, rootdir = self.env.SysUserHome, type = self.env.DirType, taskId = self.env
        if env.DirType == 'shot':
            rootpath = os.path.join(env.SysUserHome, env.Company, env.Project,'shot_images', env.SeqId)
        elif env.DirType == 'asset':
            rootpath = os.path.join(env.SysUrootdir, env.corpPrefix, env.Project,'asset_images')

        if not os.path.exists(rootpath):
            os.makedirs(rootpath)
        imagePath = os.path.join(rootpath,os.path.split(url)[1])
        serverName = 'http://%s'%env.ServerName
        thumbnailURL = urlparse.urljoin(serverName,url)
        urllib.urlretrieve(thumbnailURL,imagePath)
        return imagePath


#
# imagePath = unicode("C:\\Users\\simo\\Pictures\\thumbnail_한글.png","euc-kr").encoding('utf-8')
#
# os.makedirs(os.path.dirname(imagePath))
# imagePath2 = "C:\\Users\\simo\\Pictures\\test34_00.png"
# mask = 'D:\\Dev_project\\wormhole\\python\\testProject\\PyQtTest\\image\\mask.png'

#thumbnail = circular(ofile=imagePath, output=imagePath2, mask=mask)

