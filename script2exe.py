# coding=u8
# script2exe.py

import sys
import os
from optparse import OptionParser
import re


def getOpt():
    usage = "%prog [-i <in_path>][-ico <ico_path>][-o <exe_path>]"
    parser = OptionParser(usage)
    parser.add_option("-i","--input",dest="in_path",metavar="script_file",help="Input file")
    parser.add_option("-c","--icon",dest="ico_path",metavar="icon_file",help="Add a icon file")
    parser.add_option("-o","--output",dest="out_path",metavar="exe_file",help="Output exe path")
    return parser.parse_args()

def checkFile(path):
    if not os.path.exists(path) or not os.path.isfile(path):
        print ("Error: File {} not exits".format(path))
        exit()

def inputReport(in_path,ico_path):
    if not ico_path:
        print('Accept: input file {}'.format(in_path))
    else:
        print('Accept: input file {}, icon file {}'.format(in_path,ico_path))

def writeFile(string,path):
    try:
        with open(path,'w') as file:
            file.write(string)
    except:
        print('Error: Write {} failed.'.format(path))
        exit()

def writeFileB(data,path):
    try:
        with open(path,'wb') as file:
            file.write(data)
            file.flush()
    except:
        print('Error: Write {} failed.'.format(path))
        exit()

def copyFile(path_from,path_to):
    with open(path_from,'r') as file:
        string = file.read()
    writeFile(string,path_to)

def copyFileB(path_from,path_to):
    with open(path_from,'rb') as file:
        data = file.read()
    writeFileB(data,path_to)

def cmkdir(path):
    if(os.path.exists(path)==False or os.path.isdir(path)==False):
        os.mkdir(path)

def main():
    # accept options
    (options, args) = getOpt()
    if options.in_path:
        in_path = options.in_path
        in_path = os.path.abspath(in_path)
    elif len(args)>0:
        in_path = args[0]
        in_path = os.path.abspath(in_path)
    else:
        print('Error: No input file')
        exit()
    checkFile(in_path)
    if options.ico_path:
        ico_path = options.ico_path
        ico_path = os.path.abspath(ico_path)
        checkFile(ico_path)
    else:
        ico_path = None
    if options.out_path:
        out_path = options.out_path
    else:
        out_path = in_path[:in_path.rfind('.')]+'.exe'
    inputReport(in_path,ico_path)    

    # confirm path
    thisDir = os.path.split(os.path.realpath(sys.argv[0]))[0] 
    temp_dir_path = thisDir+'/temp'
    in_dir_path = thisDir+'/script'
    (in_dir,in_file) = os.path.split(in_path)
    (in_name,in_ext) = os.path.splitext(in_file)
    temp_path = temp_dir_path+'/{}'.format(in_name)
    in_copy_path = in_dir_path+os.sep+in_file
    c_path = temp_path+'/{}.c'.format(in_name)
    exe_path = temp_path+'/{}.exe'.format(in_name)
    if ico_path:
        rc_path = temp_path+'/{}.rc'.format(in_name)
        o_path =  temp_path+'/{}.o'.format(in_name)
        (ico_dir,ico_file) = os.path.split(ico_path)
        ico_copy_path = temp_path+os.sep+ico_file
    
    # start conversion
    cmkdir(temp_dir_path)
    cmkdir(in_dir_path)
    cmkdir(temp_path)
    copyFile(in_path,in_copy_path)
    c_code = '#include <stdlib.h>\nmain(){system("'+in_copy_path+'");}'
    c_code = re.sub('\\\\','/',c_code)
    writeFile(c_code,c_path)
    if ico_path:
        copyFileB(ico_path,ico_copy_path)
        rc_code = 'id ICON "{}"'.format(ico_copy_path)
        rc_code = re.sub('\\\\','/',rc_code)
        writeFile(rc_code,rc_path)
        os.system('windres "{}" "{}"'.format(rc_path,o_path))
        os.system('gcc {} {} -o {}'.format(c_path,o_path,exe_path))
    else:
        os.system('gcc {} -o {}'.format(c_path,exe_path))
    copyFileB(exe_path,out_path)
    print('Complete: Create {}'.format(out_path))

main()

