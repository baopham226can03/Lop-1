import pandas as pd
import os

class AbbreviationReplacer:
    def __init__(self, filepath='data/viettat.xlsx'):
        """
        Khởi tạo class và đọc file chứa từ viết tắt.
        
        Parameters:
        - filepath (str): Đường dẫn đến file Excel chứa các từ viết tắt và từ gốc.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Không tìm thấy file: {filepath}")

        tat = pd.read_excel(filepath)
        tat = tat.iloc[:, :2]
        tat.columns = ['Tắt', 'Gốc']
        tat['Tắt'] = tat['Tắt'].str.lower()
        self.abbreviation_dict = dict(zip(tat['Tắt'], tat['Gốc']))

    def replace(self, text):
        """
        Thay thế từ viết tắt trong văn bản đầu vào bằng từ gốc.

        Parameters:
        - text (str): Chuỗi văn bản cần xử lý.

        Returns:
        - str: Văn bản đã được thay thế từ viết tắt.
        """
        words = text.split()
        replaced_words = [self.abbreviation_dict.get(word.lower(), word) for word in words]
        return ' '.join(replaced_words)