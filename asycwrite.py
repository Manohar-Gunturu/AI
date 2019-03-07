

def opentracefiles():
    try:
        my_file_handle = open("D:\\new_dir1\\anotherfile.txt")
    except IOError:
        print("File not found or path is incorrect")
