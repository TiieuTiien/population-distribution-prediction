import pandas as pd
import glob
import os

# Đường dẫn đến thư mục chứa các thư mục con
root_path = './archive'
output_dir = 'sample'

# Tạo thư mục 'sample' nếu chưa tồn tại
os.makedirs(output_dir, exist_ok=True)

# Duyệt qua các thư mục con và lấy file CSV
for subdir in glob.glob(os.path.join(root_path, '*/')):  # Lấy các thư mục con
    csv_files = glob.glob(os.path.join(subdir, '*.csv'))
    for file in csv_files:
        df = pd.read_csv(file)
        sample = df.head(100)
        output_path = os.path.join(output_dir, f'sample_{os.path.basename(file)}')
        sample.to_csv(output_path, index=False)  # Lưu file mẫu vào thư mục 'sample'
        print(f'Sample từ {file} đã được lưu vào {output_path}.')
