import os

# Specify the directory path where the image files are located
directory = 'D:/Bahareh/7/Files/Artificial Intelligence/Git/Artificial-Intelligence/Projects/2 - Aritificial Neural Networks/USPS_images/images/test/'

# Initialize a dictionary to keep track of the count for each digit
digit_count = {str(i): 0 for i in range(10)}

# Iterate over the files in the directory
for filename in os.listdir(directory):
    # Check if the file name matches the desired pattern
    if filename.endswith('.jpg'):
        digit = filename.split('_')[0]
        # Check if the digit is valid (0-9)
        if digit.isdigit():
            # Increment the count for the current digit
            digit_count[digit] += 1
            # Check if the count exceeds the desired limit (e.g., 100)
            if digit_count[digit] > 10:
                file_path = os.path.join(directory, filename)
                # Delete the file
                os.remove(file_path)
                print(f"Deleted file: {filename}")