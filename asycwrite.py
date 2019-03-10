

decision_tracker = 2
file_handle = None


def open_trace(isab):
    global file_handle, decision_tracker
    if isab:
        filename = "traceab"+str(decision_tracker)+".txt"
    else:
        filename = "tracemm"+str(decision_tracker)+".txt"
    try:
        file_handle = open(filename, "w")
        decision_tracker += 1
    except IOError:
        print("File not found or path is incorrect")


def write_trace(lines):
    if file_handle is not None:
        file_handle.write("\n".join(lines))
        file_handle.flush()


def close_trace():
    if file_handle is not None:
        file_handle.close()
