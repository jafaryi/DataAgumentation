import os
import random
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

def generate_random_floats(num_points, min_value, max_value):
    return [round(random.uniform(min_value, max_value), 2) for _ in range(num_points)]

def rotate_image(image, angle):
    return image.rotate(angle)

def crop_image(image, crop_factor):
    original_width, original_height = image.size
    crop_width = int(original_width * crop_factor)
    crop_height = int(original_height * crop_factor)
    
    left = (original_width - crop_width) // 2
    top = (original_height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    
    cropped_image = image.crop((left, top, right, bottom))
    
    return cropped_image

def enhance_quality(image):
    # Applying Gaussian blur to enhance quality
    enhanced_image = image.filter(ImageFilter.GaussianBlur(radius=1))
    
    # Converting the image to numpy array for further processing
    enhanced_array = np.array(enhanced_image)
    
    # Applying gamma correction for brightness adjustment
    gamma = 1.2
    enhanced_array = np.power(enhanced_array / float(np.max(enhanced_array)), gamma) * 255.0
    
    # Converting back to PIL image
    enhanced_image = Image.fromarray(enhanced_array.astype('uint8'))
    
    # Enhance contrast
    contrast_enhancer = ImageEnhance.Contrast(enhanced_image)
    enhanced_image = contrast_enhancer.enhance(1)  # Adjust the contrast
    
    # Enhance brightness
    brightness_enhancer = ImageEnhance.Brightness(enhanced_image)
    enhanced_image = brightness_enhancer.enhance(1.2)  # Adjust the brightness
    
    return enhanced_image

def save_image(image, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    image.save(os.path.join(directory, filename))

def process_images(input_folder, output_folder, num_images=5, output_size=(1200, 1200), crop_factor=0.5):
    # ایجاد یک پوشه برای تمام تصاویر پردازش شده
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            input_image_path = os.path.join(input_folder, filename)
            output_directory = output_folder  # پوشهٔ خروجی یکبار ایجاد شده و برای همهٔ تصاویر استفاده می‌شود

            image = Image.open(input_image_path)

            generated_rotations = set()

            for i in range(num_images):
                rotation_angle = None
                while rotation_angle is None or rotation_angle in generated_rotations:
                    rotation_angle = round(random.uniform(-20, 20), 2)

                generated_rotations.add(rotation_angle)

                rotated_image = rotate_image(image, rotation_angle)
                cropped_image = crop_image(rotated_image, crop_factor)
                enhanced_image = enhance_quality(cropped_image)
                
                # تغییر ابعاد تصویر به 640x640 پیکسل
                resized_image = enhanced_image.resize(output_size, Image.ANTIALIAS)
                
                output_filename = f"enhanced_image_{i}_{filename}"  # افزودن نام فایل اصلی به نام تصاویر پردازش شده
                save_image(resized_image, output_directory, output_filename)

if __name__ == "__main__":
    input_folder = 'C:\\Users\\Mohammadreza\\Desktop\\Newfolder\\data\\3'
    output_folder = 'C:\\Users\\Mohammadreza\\Desktop\\Newfolder\\data\\4'
    process_images(input_folder, output_folder)
