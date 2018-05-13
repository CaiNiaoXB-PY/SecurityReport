import os
import zipfile
import time
def make_zip(source_dir,output_filename):
    zipf = zipfile.ZipFile(output_filename,'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent,dirnames,filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent,filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)
            zipf.write(pathfile,arcname)
    zipf.close()
ziptime = time.strftime('%Y%m%d%H',time.localtime(time.time()))
make_zip("C:\\Python27\\CheckResult\\img\\","C:\Python27\CheckResult\SecureReport_OA_Image" + ziptime + ".zip")
