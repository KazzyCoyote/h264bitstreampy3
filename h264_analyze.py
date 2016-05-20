# the code of a loop that analyzes h264 bit stream goes here.

import h264_stream as h264
import h264_nal as nal
import sys

BUFSIZE = 32 * 1024 * 1024

# TODO: make this work

def main(): 
    print "calling h264 analyze!" 
    args = sys.argv
    if len(args) != 2: 
        print "error! should give the file name" 
        break
    input_file = open(args[1])
    h = h264.init_h264_stream()
    
    while True:
        buf = input_file.read(xxxx)
        nal_start, nal_end, length = nal.find_nal_unit(buf) # how the nal can remember the last place? 
        while (nal_start):
            # here we could add "verbose" option later
            print("!! Found NAL at offset " + str(off + (p - buf) + nal_start) + " size " + str(nal_end - nal_start))
            p += nal_start
            nal_unit = nal.read_debug_nal_unit(buf, nal_start, nal_end)
            h.nal = nal_unit
            
            if (opt_probe and h.nal.nal_unit_type = NAL_UNIT_TYPE_SPS):
                constraint_byte = h.sps.constraint_set0_flag << 7
                constraint_byte = h.sps.constraint_set1_flag << 6
                constraint_byte = h.sps.constraint_set2_flag << 5
                constraint_byte = h.sps.constraint_set3_flag << 4
                constraint_byte = h.sps.constraint_set4_flag << 3
                constraint_byte = h.sps.constraint_set4_flag << 3
                
                print("codec: avc1." + str(h.sps.profile_idc) + str(constraint_byte) + str(h.sps.level_idc))
                break
            # 
            # here in the c code there is something commented out. Not sure if it is there in the beginning. Need to see the repository.
            
            p += (nal_end - nal_start)
            sz -= nal_end
            
        if p == buf:
            print("!! Did not find any NALs between offset " + str(off) + " size " + str(off + sz) + " discarding")
            p = buf + sz
            sz = 0
            
        off += p - buf
        p = buf
        
     
   
            