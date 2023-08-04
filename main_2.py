import os
import csv
import pandas as pd


# """id, timestamp, class-1-label, class-2-label"""
# path_video_match_timestamp = '/Users/yolandali/Desktop/label-timestamp/video_match_timestamp/'
# dir_video_match_timestamp = sorted(os.listdir(path_video_match_timestamp))
#
# for sub_video_match_timestamp in dir_video_match_timestamp:
#     path_sub_video_match_timestamp = path_video_match_timestamp + sub_video_match_timestamp
#     data_video_match_timestamp = pd.read_csv(path_sub_video_match_timestamp, sep=',', header=None, names=['timestamp', 'label_id'])
#     data_video_match_timestamp['timestamp'] = data_video_match_timestamp['timestamp'].str.replace('.mp4', '')
#     data_video_match_timestamp['label_id'] = data_video_match_timestamp['label_id'].str.replace('.mp4', '')
# remove .mp4 suffix in match files

original_timestamp = 'D:/PycharmProjects/label-timestamp/original_timestamp/'
path_process_label = 'D:/PycharmProjects/label-timestamp/process_label/'
path_process_timestamp = 'D:/PycharmProjects/label-timestamp/process_timestamp/'

dir_process_label = sorted(os.listdir(path_process_label))
dir_original_timestamp = sorted(os.listdir(original_timestamp))
print(dir_process_label)
for sub_process_label in dir_process_label:
    if '~' not in sub_process_label:
        print(sub_process_label)
        path_sub_process_label = path_process_label + sub_process_label
        data_original_label = pd.read_excel(path_sub_process_label,
                                            sheet_name='Sheet1',
                                            header=None).drop(0).reset_index(drop=True)
        data_original_label.columns = ['video_id', 'label-1', 'label-2', 'timestamp']
        print(data_original_label)
        data_original_label['video_id'] = data_original_label['video_id'].astype(int)
        # data_original_label.drop(data_original_label.columns[3], axis=1)

        if sub_process_label.strip('.xlsx')+ '.csv' in dir_original_timestamp:
            path_sub_original_timestamp = original_timestamp + sub_process_label.strip('.xlsx') + '.csv'
            data_original_timestamp = pd.read_csv(path_sub_original_timestamp, sep=',', header=None, names=['id', 'timestamp'])
            #data_original_timestamp['video_id'] = data_original_timestamp['video_id'].astype(int)
            result = pd.merge(data_original_timestamp, data_original_label, how='outer', on='timestamp')
            result.to_excel(path_process_timestamp + sub_process_label, index=False)



