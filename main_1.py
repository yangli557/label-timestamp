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

path_original_label = 'D:/PycharmProjects/label-timestamp/original_label/'
path_video_match_timestamp = 'D:/PycharmProjects/label-timestamp/video_match_timestamp/'
path_process_label = 'D:/PycharmProjects/label-timestamp/process_label/'
dir_original_label = sorted(os.listdir(path_original_label))
dir_video_match_timestamp = sorted(os.listdir(path_video_match_timestamp))
print(dir_original_label)
for sub_original_label in dir_original_label:
    if '~' not in sub_original_label:
        print(sub_original_label)
        path_sub_original_label = path_original_label + sub_original_label
        data_original_label = pd.read_excel(path_sub_original_label,
                                            sheet_name='Sheet1',
                                            header=None,
                                            usecols=[0, 1, 2]).drop(0).reset_index(drop=True)
        data_original_label.columns = ['video_id', 'label-1', 'label-2']
        data_original_label['video_id'] = data_original_label['video_id'].astype(int)
        # data_original_label.drop(data_original_label.columns[3], axis=1)

        if sub_original_label.strip('.xlsx')+'.txt' in dir_video_match_timestamp:
            path_sub_video_match_timestamp = path_video_match_timestamp + sub_original_label.strip('.xlsx')+'.txt'
            data_video_match_timestamp = pd.read_csv(path_sub_video_match_timestamp, sep=',', header=None, names=['timestamp', 'video_id'])
            data_video_match_timestamp['timestamp'] = data_video_match_timestamp['timestamp'].str.replace('.mp4', '')
            data_video_match_timestamp['video_id'] = data_video_match_timestamp['video_id'].str.replace('.mp4', '').astype(int)
            print(data_original_label, data_video_match_timestamp)
            result = pd.merge(data_original_label, data_video_match_timestamp, on='video_id')

            result.to_excel(path_process_label+sub_original_label, index=False)




