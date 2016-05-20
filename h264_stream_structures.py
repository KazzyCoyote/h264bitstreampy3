# all you need to represent things in h264stream 
# TODO: finish this 


class Vui:
    def init(self):
        self.aspect_ratio_info_present_flag = xxx
        self.aspect_ratio_idc = xxx
        self.sar_width = xxx
        self.sar_height = xxx
        self.overscan_info_present_flag = xxx
        self.overscan_appropriate_flag = xxx
        self.video_signal_type_present_flag = xxx
        self.video_format;
        self.video_full_range_flag;
        self.colour_description_present_flag;
        self.colour_primaries;
        self.transfer_characteristics;
        self.matrix_coefficients;
        self.chroma_loc_info_present_flag;
        self.chroma_sample_loc_type_top_field;
        self.chroma_sample_loc_type_bottom_field;
        self.timing_info_present_flag;
        self.num_units_in_tick;
        self.time_scale;
        self.fixed_frame_rate_flag;
        self.nal_hrd_parameters_present_flag;
        self.vcl_hrd_parameters_present_flag;
        self.low_delay_hrd_flag;
        self.pic_struct_present_flag;
        self.bitstream_restriction_flag;
        self.motion_vectors_over_pic_boundaries_flag;
        self.max_bytes_per_pic_denom;
        self.max_bits_per_mb_denom;
        self.log2_max_mv_length_horizontal;
        self.log2_max_mv_length_vertical;
        self.num_reorder_frames;
        self.max_dec_frame_buffering;
  
  
class Hrd:
    def init(self): 
        self.cpb_cnt_minus1;
        self.bit_rate_scale;
        self.cpb_size_scale;
        self.bit_rate_value_minus1[32]; # up to cpb_cnt_minus1, which is <= 31
        self.cpb_size_value_minus1[32];
        self.cbr_flag[32];
        self.initial_cpb_removal_delay_length_minus1;
        self.cpb_removal_delay_length_minus1;
        self.dpb_output_delay_length_minus1;
        self.time_offset_length;
  
  
class Sps_t:
    def init(self):
        self.profile_idc;
        self.constraint_set0_flag;
        self.constraint_set1_flag;
        self.constraint_set2_flag;
        self.constraint_set3_flag;
        self.constraint_set4_flag;
        self.constraint_set5_flag;
        self.sreserved_zero_2bits;
        self.level_idc;
        self.seq_parameter_set_id;
        self.chroma_format_idc;
        self.residual_colour_transform_flag;
        self.bit_depth_luma_minus8;
        self.bit_depth_chroma_minus8;
        self.qpprime_y_zero_transform_bypass_flag;
        self.seq_scaling_matrix_present_flag;
        self.seq_scaling_list_present_flag[8];
        self.ScalingList4x4[6];
        self.UseDefaultScalingMatrix4x4Flag[6];
        self.ScalingList8x8[2];
        self.UseDefaultScalingMatrix8x8Flag[2];
        self.log2_max_frame_num_minus4;
        self.pic_order_cnt_type;
        self.log2_max_pic_order_cnt_lsb_minus4;
        self.delta_pic_order_always_zero_flag;
        self.offset_for_non_ref_pic;
        self.offset_for_top_to_bottom_field;
        self.num_ref_frames_in_pic_order_cnt_cycle;
        self.offset_for_ref_frame[256];
        self.num_ref_frames;
        self.gaps_in_frame_num_value_allowed_flag;
        self.pic_width_in_mbs_minus1;
        self.pic_height_in_map_units_minus1;
        self.frame_mbs_only_flag;
        self.mb_adaptive_frame_field_flag;
        self.direct_8x8_inference_flag;
        self.frame_cropping_flag;
        self.frame_crop_left_offset;
        self.frame_crop_right_offset;
        self.rame_crop_top_offset;
        self.frame_crop_bottom_offset;
        self.vui_parameters_present_flag;
    
  
class Pps_t:
    def init(self):
        self.pic_parameter_set_id;
        self.seq_parameter_set_id;
        self.entropy_coding_mode_flag;
        self.pic_order_present_flag;
        self.num_slice_groups_minus1;
        self.slice_group_map_type;
        self.run_length_minus1[8]; # up to num_slice_groups_minus1, which is <= 7 in Baseline and Extended, 0 otheriwse
        self.top_left[8];
        self.bottom_right[8];
        self.slice_group_change_direction_flag;
        self.slice_group_change_rate_minus1;
        self.pic_size_in_map_units_minus1;
        self.slice_group_id[256]; # FIXME what size?
        self.num_ref_idx_l0_active_minus1;
        self.num_ref_idx_l1_active_minus1;
        self.weighted_pred_flag;
        self.weighted_bipred_idc;
        self.pic_init_qp_minus26;
        self.pic_init_qs_minus26;
        self.chroma_qp_index_offset;
        self.deblocking_filter_control_present_flag;
        self.constrained_intra_pred_flag;
        self.redundant_pic_cnt_present_flag;

    # set iff we carry any of the optional headers
        self._more_rbsp_data_present;

        self.transform_8x8_mode_flag;
        self.pic_scaling_matrix_present_flag;
        self.pic_scaling_list_present_flag[8];
        self.ScalingList4x4[6];
        self.UseDefaultScalingMatrix4x4Flag[6];
        self.ScalingList8x8[2];
        self.UseDefaultScalingMatrix8x8Flag[2];
        self.second_chroma_qp_index_offset;

  
class Pwt:
    def init(self):
        self.luma_log2_weight_denom;
        self.chroma_log2_weight_denom;
        self.luma_weight_l0_flag[64];
        self.luma_weight_l0[64];
        self.luma_offset_l0[64];
        self.chroma_weight_l0_flag[64];
        self.chroma_weight_l0[64][2];
        self.chroma_offset_l0[64][2];
        self.luma_weight_l1_flag[64];
        self.luma_weight_l1[64];
        self.luma_offset_l1[64];
        self.chroma_weight_l1_flag[64];
        self.chroma_weight_l1[64][2];
        self.chroma_offset_l1[64][2];      
        
  
  
class Slice_header_t:
    def init(self):
        self.first_mb_in_slice;
        self.slice_type;
        self.pic_parameter_set_id;
        self.frame_num;
        self.field_pic_flag;
        self.bottom_field_flag;
        self.idr_pic_id;
        self.pic_order_cnt_lsb;
        self.delta_pic_order_cnt_bottom;
        self.delta_pic_order_cnt[ 2 ];
        self.redundant_pic_cnt;
        self.direct_spatial_mv_pred_flag;
        self.num_ref_idx_active_override_flag;
        self.num_ref_idx_l0_active_minus1;
        self.num_ref_idx_l1_active_minus1;
        self.cabac_init_idc;
        self.slice_qp_delta;
        self.sp_for_switch_flag;
        self.slice_qs_delta;
        self.disable_deblocking_filter_idc;
        self.slice_alpha_c0_offset_div2;
        self.slice_beta_offset_div2;
        self.slice_group_change_cycle;



class Reorder_l1:
    def init(self):
        self.reordering_of_pic_nums_idc[64];
        self.abs_diff_pic_num_minus1[64];
        self.long_term_pic_num[64];    
        
class Reorder_l0:
   def init(self):
    

class                 
                  



class Rplr:
    def init(self):
        self.ref_pic_list_reordering_flag_l0;
        self.reorder_l0
        self.ref_pic_list_reordering_flag_l1
        self.reorder_l1



class Drpm:
    def init(self):
        self.no_output_of_prior_pics_flag;
        self.long_term_reference_flag;
        self.adaptive_ref_pic_marking_mode_flag;
        self.memory_management_control_operation[64];
        self.difference_of_pic_nums_minus1[64];
        self.long_term_pic_num[64];
        self.long_term_frame_idx[64];
        self.max_long_term_frame_idx_plus1[64];


class Slice_header_t:
    def init(self):
      
      
      
class Aud_t:
    def init(self):
        self.primary_pic_type
        
'''''
   Network Abstraction Layer (NAL) unit
   @see 7.3.1 NAL unit syntax
   @see read_nal_unit
   @see write_nal_unit
   @see debug_nal
'''
        
        
class Nal_t:
    def init(self):
        self.forbidden_zero_bit;
        self.nal_ref_idc;
        self.nal_unit_type;
        self.parsed; # FIXME
        self.sizeof_parsed;

    #uint8_t* rbsp_buf;
    #int rbsp_size;

class Sei_buffering_t:
    def init(self):
        self._is_initialized;
        self.sps_id;
        self.initial_cpb_removal_delay;
        self.nitial_cpb_delay_offset;


typedef struct
{
    int clock_timestamp_flag;
        int ct_type;
        int nuit_field_based_flag;
        int counting_type;
        int full_timestamp_flag;
        int discontinuity_flag;
        int cnt_dropped_flag;
        int n_frames;

        int seconds_value;
        int minutes_value;
        int hours_value;

        int seconds_flag;
        int minutes_flag;
        int hours_flag;

        int time_offset;
} picture_timestamp_t;

typedef struct
{
  int _is_initialized;
  int cpb_removal_delay;
  int dpb_output_delay;
  int pic_struct;
  picture_timestamp_t clock_timestamps[3]; // 3 is the maximum possible value
} sei_picture_timing_t;


typedef struct
{
  int rbsp_size;
  uint8_t* rbsp_buf;
} slice_data_rbsp_t;

/**
   H264 stream
   Contains data structures for all NAL types that can be handled by this library.  
   When reading, data is read into those, and when writing it is written from those.  
   The reason why they are all contained in one place is that some of them depend on others, we need to 
   have all of them available to read or write correctly.
 */
typedef struct
{
    nal_t* nal;
    sps_t* sps;
    pps_t* pps;
    aud_t* aud;
    sei_t* sei; //This is a TEMP pointer at whats in h->seis...    
    int num_seis;
    slice_header_t* sh;
    slice_data_rbsp_t* slice_data;

    sps_t* sps_table[32];
    pps_t* pps_table[256];
    sei_t** seis;

} h264_stream_t;

h264_stream_t* h264_new();
void h264_free(h264_stream_t* h);

int find_nal_unit(uint8_t* buf, int size, int* nal_start, int* nal_end);

int rbsp_to_nal(const uint8_t* rbsp_buf, const int* rbsp_size, uint8_t* nal_buf, int* nal_size);
int nal_to_rbsp(const uint8_t* nal_buf, int* nal_size, uint8_t* rbsp_buf, int* rbsp_size);

int read_nal_unit(h264_stream_t* h, uint8_t* buf, int size);
int peek_nal_unit(h264_stream_t* h, uint8_t* buf, int size);

void read_seq_parameter_set_rbsp(h264_stream_t* h, bs_t* b);
void read_scaling_list(bs_t* b, int* scalingList, int sizeOfScalingList, int* useDefaultScalingMatrixFlag );
void read_vui_parameters(h264_stream_t* h, bs_t* b);
void read_hrd_parameters(h264_stream_t* h, bs_t* b);

void read_pic_parameter_set_rbsp(h264_stream_t* h, bs_t* b);

void read_sei_rbsp(h264_stream_t* h, bs_t* b);
void read_sei_message(h264_stream_t* h, bs_t* b);
void read_access_unit_delimiter_rbsp(h264_stream_t* h, bs_t* b);
void read_end_of_seq_rbsp(h264_stream_t* h, bs_t* b);
void read_end_of_stream_rbsp(h264_stream_t* h, bs_t* b);
void read_filler_data_rbsp(h264_stream_t* h, bs_t* b);

void read_slice_layer_rbsp(h264_stream_t* h, bs_t* b);
void read_rbsp_slice_trailing_bits(h264_stream_t* h, bs_t* b);
void read_rbsp_trailing_bits(h264_stream_t* h, bs_t* b);
void read_slice_header(h264_stream_t* h, bs_t* b);
void read_ref_pic_list_reordering(h264_stream_t* h, bs_t* b);
void read_pred_weight_table(h264_stream_t* h, bs_t* b);
void read_dec_ref_pic_marking(h264_stream_t* h, bs_t* b);

int more_rbsp_trailing_data(h264_stream_t* h, bs_t* b);

int write_nal_unit(h264_stream_t* h, uint8_t* buf, int size);

void write_seq_parameter_set_rbsp(h264_stream_t* h, bs_t* b);
void write_scaling_list(bs_t* b, int* scalingList, int sizeOfScalingList, int* useDefaultScalingMatrixFlag );
void write_vui_parameters(h264_stream_t* h, bs_t* b);
void write_hrd_parameters(h264_stream_t* h, bs_t* b);

void write_pic_parameter_set_rbsp(h264_stream_t* h, bs_t* b);

void write_sei_rbsp(h264_stream_t* h, bs_t* b);
void write_sei_message(h264_stream_t* h, bs_t* b);
void write_access_unit_delimiter_rbsp(h264_stream_t* h, bs_t* b);
void write_end_of_seq_rbsp(h264_stream_t* h, bs_t* b);
void write_end_of_stream_rbsp(h264_stream_t* h, bs_t* b);
void write_filler_data_rbsp(h264_stream_t* h, bs_t* b);

void write_slice_layer_rbsp(h264_stream_t* h, bs_t* b);
void write_rbsp_slice_trailing_bits(h264_stream_t* h, bs_t* b);
void write_rbsp_trailing_bits(h264_stream_t* h, bs_t* b);
void write_slice_header(h264_stream_t* h, bs_t* b);
void write_ref_pic_list_reordering(h264_stream_t* h, bs_t* b);
void write_pred_weight_table(h264_stream_t* h, bs_t* b);
void write_dec_ref_pic_marking(h264_stream_t* h, bs_t* b);

int read_debug_nal_unit(h264_stream_t* h, uint8_t* buf, int size);

void debug_sps(sps_t* sps);
void debug_pps(pps_t* pps);
void debug_slice_header(slice_header_t* sh);
void debug_nal(h264_stream_t* h, nal_t* nal);

void debug_bytes(uint8_t* buf, int len);

void read_sei_payload( h264_stream_t* h, bs_t* b, int payloadType, int payloadSize);
void write_sei_payload( h264_stream_t* h, bs_t* b, int payloadType, int payloadSize);

//NAL ref idc codes
#define NAL_REF_IDC_PRIORITY_HIGHEST    3
#define NAL_REF_IDC_PRIORITY_HIGH       2
#define NAL_REF_IDC_PRIORITY_LOW        1
#define NAL_REF_IDC_PRIORITY_DISPOSABLE 0

//Table 7-1 NAL unit type codes
#define NAL_UNIT_TYPE_UNSPECIFIED                    0    // Unspecified
#define NAL_UNIT_TYPE_CODED_SLICE_NON_IDR            1    // Coded slice of a non-IDR picture
#define NAL_UNIT_TYPE_CODED_SLICE_DATA_PARTITION_A   2    // Coded slice data partition A
#define NAL_UNIT_TYPE_CODED_SLICE_DATA_PARTITION_B   3    // Coded slice data partition B
#define NAL_UNIT_TYPE_CODED_SLICE_DATA_PARTITION_C   4    // Coded slice data partition C
#define NAL_UNIT_TYPE_CODED_SLICE_IDR                5    // Coded slice of an IDR picture
#define NAL_UNIT_TYPE_SEI                            6    // Supplemental enhancement information (SEI)
#define NAL_UNIT_TYPE_SPS                            7    // Sequence parameter set
#define NAL_UNIT_TYPE_PPS                            8    // Picture parameter set
#define NAL_UNIT_TYPE_AUD                            9    // Access unit delimiter
#define NAL_UNIT_TYPE_END_OF_SEQUENCE               10    // End of sequence
#define NAL_UNIT_TYPE_END_OF_STREAM                 11    // End of stream
#define NAL_UNIT_TYPE_FILLER                        12    // Filler data
#define NAL_UNIT_TYPE_SPS_EXT                       13    // Sequence parameter set extension
                                             // 14..18    // Reserved
#define NAL_UNIT_TYPE_CODED_SLICE_AUX               19    // Coded slice of an auxiliary coded picture without partitioning
                                             // 20..23    // Reserved
                                             // 24..31    // Unspecified

 

//7.4.3 Table 7-6. Name association to slice_type
#define SH_SLICE_TYPE_P        0        // P (P slice)
#define SH_SLICE_TYPE_B        1        // B (B slice)
#define SH_SLICE_TYPE_I        2        // I (I slice)
#define SH_SLICE_TYPE_SP       3        // SP (SP slice)
#define SH_SLICE_TYPE_SI       4        // SI (SI slice)
//as per footnote to Table 7-6, the *_ONLY slice types indicate that all other slices in that picture are of the same type
#define SH_SLICE_TYPE_P_ONLY    5        // P (P slice)
#define SH_SLICE_TYPE_B_ONLY    6        // B (B slice)
#define SH_SLICE_TYPE_I_ONLY    7        // I (I slice)
#define SH_SLICE_TYPE_SP_ONLY   8        // SP (SP slice)
#define SH_SLICE_TYPE_SI_ONLY   9        // SI (SI slice)

//Appendix E. Table E-1  Meaning of sample aspect ratio indicator
#define SAR_Unspecified  0           // Unspecified
#define SAR_1_1        1             //  1:1
#define SAR_12_11      2             // 12:11
#define SAR_10_11      3             // 10:11
#define SAR_16_11      4             // 16:11
#define SAR_40_33      5             // 40:33
#define SAR_24_11      6             // 24:11
#define SAR_20_11      7             // 20:11
#define SAR_32_11      8             // 32:11
#define SAR_80_33      9             // 80:33
#define SAR_18_11     10             // 18:11
#define SAR_15_11     11             // 15:11
#define SAR_64_33     12             // 64:33
#define SAR_160_99    13             // 160:99
                                     // 14..254           Reserved
#define SAR_Extended      255        // Extended_SAR

//7.4.3.1 Table 7-7 reordering_of_pic_nums_idc operations for reordering of reference picture lists
#define RPLR_IDC_ABS_DIFF_ADD       0
#define RPLR_IDC_ABS_DIFF_SUBTRACT  1
#define RPLR_IDC_LONG_TERM          2
#define RPLR_IDC_END                3

//7.4.3.3 Table 7-9 Memory management control operation (memory_management_control_operation) values
#define MMCO_END                     0
#define MMCO_SHORT_TERM_UNUSED       1
#define MMCO_LONG_TERM_UNUSED        2
#define MMCO_SHORT_TERM_TO_LONG_TERM 3
#define MMCO_LONG_TERM_MAX_INDEX     4
#define MMCO_ALL_UNUSED              5
#define MMCO_CURRENT_TO_LONG_TERM    6

//7.4.2.4 Table 7-5 Meaning of primary_pic_type
#define AUD_PRIMARY_PIC_TYPE_I       0                // I
#define AUD_PRIMARY_PIC_TYPE_IP      1                // I, P
#define AUD_PRIMARY_PIC_TYPE_IPB     2                // I, P, B
#define AUD_PRIMARY_PIC_TYPE_SI      3                // SI
#define AUD_PRIMARY_PIC_TYPE_SISP    4                // SI, SP
#define AUD_PRIMARY_PIC_TYPE_ISI     5                // I, SI
#define AUD_PRIMARY_PIC_TYPE_ISIPSP  6                // I, SI, P, SP
#define AUD_PRIMARY_PIC_TYPE_ISIPSPB 7                // I, SI, P, SP, B

#define H264_PROFILE_BASELINE  66
#define H264_PROFILE_MAIN      77
#define H264_PROFILE_EXTENDED  88
#define H264_PROFILE_HIGH     100

// file handle for debug output
extern FILE* h264_dbgfile;

      

    