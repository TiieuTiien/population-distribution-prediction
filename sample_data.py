import pandas as pd
import glob
import os

# Đường dẫn đến thư mục chứa các file CSV
root_path = './data'  # Relative path to the 'data' directory
output_dir = './data_samples/sample'  # Relative path for output directory

# Print the output directory
print(f'The output directory is set to: {output_dir}')

# Tạo thư mục 'sample' nếu chưa tồn tại
os.makedirs(output_dir, exist_ok=True)

# Lấy các file CSV trực tiếp trong thư mục ./data
csv_files = glob.glob(os.path.join(root_path, '*.csv'))
for file in csv_files:
    df = pd.read_csv(file, low_memory=False)
    sample = df.head(100)
    output_path = os.path.join(output_dir, f'sample_{os.path.basename(file)}')
    sample.to_csv(output_path, index=False)  # Lưu file mẫu vào thư mục 'sample'
    print(f'Sample từ {file} đã được lưu vào {output_path}.')
