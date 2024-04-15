import os


source_folder = 'C:\\Users\\Mohammadreza\\Desktop\\Newfolder\\ali-file\\labels'


destination_folder = 'C:\\Users\\Mohammadreza\\Desktop\\Newfolder\\ali-file\\labels1'


os.makedirs(destination_folder, exist_ok=True)


files = os.listdir(source_folder)

# شماره شروع نامگذاری
start_index = 0

# تغییر نام فایل‌ها و انتقال به فولدر مقصد
for file in files:
    # جدا کردن شماره فریم از نام اولیه
    _, frame_number = os.path.splitext(file)
    
    # حاصل جمع شماره شروع و شماره فریم
    new_name = f'frame_{start_index:03d}{frame_number}'
    
    # مسیر فایل مبدأ
    source_path = os.path.join(source_folder, file)
    
    # مسیر فایل مقصد
    destination_path = os.path.join(destination_folder, new_name)
    
    # انتقال و تغییر نام فایل
    os.rename(source_path, destination_path)
    
    # افزایش شماره شروع برای فایل بعدی
    start_index += 1

print('تغییر نام و انتقال فایل‌ها انجام شد.')
