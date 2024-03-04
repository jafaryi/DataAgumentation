import os

def remove_files_without_label(source_folder1, source_folder2):
    # گرفتن لیست فایل‌ها از فولدر اول
    files_folder1 = set(os.listdir(source_folder1))

    # گرفتن لیست فایل‌ها از فولدر دوم
    files_folder2 = set(os.listdir(source_folder2))

    # یافتن فایل‌هایی که در فولدر اول وجود دارند ولی در فولدر دوم ندارند
    files_to_remove = files_folder1 - files_folder2

    # حذف فایل‌های بدون لیبل از فولدر اول
    for file_name in files_to_remove:
        file_path = os.path.join(source_folder1, file_name)
        os.remove(file_path)
        print(f"فایل {file_name} بدون لیبل از فولدر {source_folder1} حذف شد.")

# فراخوانی تابع با آدرس فولدرهای مورد نظر
remove_files_without_label('C:\\Users\\Mohammadreza\\Desktop\\Newfolder\\new-data-test2', 'C:\\Users\\Mohammadreza\\Desktop\\Newfolder\\ali-file\\all')
