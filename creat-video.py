import cv2
import os

def create_video_from_images(image_folder, video_name, fps=30):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()


image_folder = 'C:\\Users\\Mohammadreza\\Desktop\\Newfolder\\video-data'
# نام ویدیو خروجی
video_name = 'C:\\Users\\Mohammadreza\\Desktop\\Newfolder\\testVideo.mp4'

# ساخت ویدیو
create_video_from_images(image_folder, video_name)
