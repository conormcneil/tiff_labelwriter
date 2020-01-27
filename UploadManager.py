#!/usr/bin/env/python3

from os import path

class UploadManager():
    file = ""
    filename = ""
    basename = ""
    fullpath = ""
    srcpath = ""
    UPLOAD_FOLDER = "tmp/"
    ALLOWED_EXTENSIONS = {'tif'}

    def __init__(self,file = None):
        if file != None:
            self.file = file
            self.filename = file.filename
            self.basename = path.splitext(file.filename)[0]
            self.fullpath = path.join(self.get_uploadfolder(), file.filename)
            self.srcpath = path.join(self.get_uploadfolder(), self.get_srcpath())

    def set_file(self,file):
        self.__init__(file)
    
    def get_file(self):
        return self.file
    
    def get_filename(self):
        return self.filename
    
    def get_basename(self):
        return self.basename
    
    def get_fullpath(self):
        return self.fullpath
    
    def get_srcpath(self):
        return self.srcpath

    def get_uploadfolder(self):
        return self.UPLOAD_FOLDER
    
    def get_labelpath(self):
        return path.join( self.get_uploadfolder(), self.get_basename() + ".xml")
    
    def allowed_file(self,filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS