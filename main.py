import os
import csv

path_dir = 'C:/Users/yli55/OneDrive/Desktop/original-videos/'

sorted_nx_files = sorted(os.listdir(path_dir))

for sub_sorted_nx_file in sorted_nx_files:
    save_record = {}
    if sub_sorted_nx_file not in ['.DS_Store']:
        sorted_video_files = sorted(os.listdir(path_dir+sub_sorted_nx_file))
        i = 0
        for sub_sorted_video_file in sorted_video_files:
            ori_path = path_dir+sub_sorted_nx_file+'/'+sub_sorted_video_file
            new_path = path_dir+sub_sorted_nx_file+'/'+f'{i}.mp4'
            os.rename(ori_path, new_path)
            save_record[sub_sorted_video_file] = f'{i}.mp4'
            i += 1

    # open file for writing, "w" is writing
    w = csv.writer(open(path_dir+str(sub_sorted_nx_file)+'.txt', "w"))
    # loop over dictionary keys and values
    for key, val in save_record.items():
        # write every key and value to file
        w.writerow([key, val])

