import sys
import h264_nal as nal
import h264_stream as h264

# this is the main program  of the project
# Structure:
#    main.py: for calling all these class to read and manipulate the bitstreams
#    h264_analyze.py: get input and output the stream-level structure
#    h264_stream.py: representaiton of the h264 bit stream
#    h264_nal.py: representation of the NAL unit
#    h264_sei.py: not sure what this is, SEI may be an unit
#    h264_avcc.py: reflects h264_avcc.c
#    h264_slice_data.py: representation of a slice


def main(): 
    print "calling main"
    print sys.argv
    if len(sys.argv) > 1:
        print "input file: " + sys.argv[1]
    # read the input file 
    input_file = open(sys.argv[1])
    buf = input_file.read(xxxx)
    # now we may not need a buffer?
    start, end, length = nal.find_nal_unit(buf)
    nal_unit = nal.read_nal_unit(buf, start, end)
    h = h264.init_h264_stream()
    h.nal = nal_unit # why a h only has one NAL?
    debug_nal(h, h.nal) # should print out something
    
    
if __name__ == '__main__':
    main()
    