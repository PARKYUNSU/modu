import os

# 경로 설정
train_labels_path = '/Users/parkyunsu/Downloads/Trailllll 2.v2i.yolov11/train/labels'
valid_labels_path = '/Users/parkyunsu/Downloads/Trailllll 2.v2i.yolov11/valid/labels'

# 클래스 매핑 테이블
class_mapping = {
    0: 1,  # Accent Chairs -> chairs
    1: 0,  # Beds -> beds
    2: 1,  # Benches -> chairs
    3: 2,  # Chests -> dressers
    4: 5,  # Coffee Table -> tables
    5: 1,  # Dining Chairs -> chairs
    6: 5,  # Dining Table -> tables
    7: 2,  # Dressers -> dressers
    8: 5,  # End Table -> tables
    9: 3,  # Floor Lamp -> lamps
    10: None,  # Hanging Picture Frames -> 삭제
    11: None,  # Headboard -> 삭제
    12: 2,  # Nightstands -> dressers
    13: None,  # Ottoman -> 삭제
    14: None,  # Plants -> 삭제
    15: None,  # Rugs -> 삭제
    16: 4,  # Sofa -> sofas
    17: 3,  # Table Lamp -> lamps
    18: None,  # Tv -> 삭제
    19: 3,  # Wall Lamps -> lamps
    20: None   # Wall Mirrors -> 삭제
}

def process_labels(label_path):
    for filename in os.listdir(label_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(label_path, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            new_lines = []
            for line in lines:
                parts = line.strip().split()
                class_id = int(parts[0])
                if class_id in class_mapping:
                    new_class_id = class_mapping[class_id]
                    if new_class_id is not None:  # 삭제하지 않을 경우만 추가
                        new_line = f"{new_class_id} {' '.join(parts[1:])}\n"
                        new_lines.append(new_line)
            
            # 파일 덮어쓰기
            with open(file_path, 'w') as file:
                file.writelines(new_lines)

# 변환 실행
process_labels(train_labels_path)
process_labels(valid_labels_path)

print("라벨 파일 변환 완료!")