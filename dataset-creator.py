import cv2
import os
import pandas as pd

def video_to_frames(video_path, output_folder):
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    frames_info_df = pd.DataFrame(columns=['Frame Number', 'Timestamp (s)', 'File Name', 'Video Name'])

    for frame_number in range(frame_count):
        ret, frame = cap.read()

        if ret:
            file_name = f"{video_name}_frame_{frame_number:04d}.jpg"
            file_path = os.path.join(output_folder, file_name)

            cv2.imwrite(file_path, frame)

            timestamp = frame_number / fps

            frames_info_df = pd.concat([
                frames_info_df,
                pd.DataFrame({
                    'Frame Number': [frame_number],
                    'Timestamp (s)': [timestamp],
                    'File Name': [file_name],
                    'Video Name': [video_name]
                })
            ], ignore_index=True)
        else:
            break

    frames_info_df.to_csv(os.path.join(output_folder, 'frames_info.csv'), index=False)

    cap.release()

if __name__ == "__main__":
    video_path = 'C:\\Users\\Mohammadreza\\Desktop\\Newfolder\\film filter\\8.mp4' 
    output_folder = 'C:\\Users\\Mohammadreza\\Desktop\\Newfolder\\new-data-test2'  
    video_to_frames(video_path, output_folder)
