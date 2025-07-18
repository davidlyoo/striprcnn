from PIL import Image
import os
import re
from collections import defaultdict

def merge_per_original(input_dir, output_dir, tile_size=1024):
    os.makedirs(output_dir, exist_ok=True)

    # ex) 02_PNEO_RGB_8bit_Linear_Scaling_36864_25600.png
    pattern = re.compile(r"(.+?)_(\d+)_(\d+)\.png")
    grouped = defaultdict(list)

    # 1. 파일 그룹화
    for filename in os.listdir(input_dir):
        match = pattern.match(filename)
        if match:
            base = match.group(1)
            top = int(match.group(2))
            left = int(match.group(3))
            grouped[base].append((filename, top, left))

    print(f"[INFO] Found {len(grouped)} original images to merge")

    # 2. 각 그룹별로 merge 수행
    for base, tiles in grouped.items():
        max_right = max(left for _, _, left in tiles) + tile_size
        max_bottom = max(top for _, top, _ in tiles) + tile_size
        canvas = Image.new('RGB', (max_right, max_bottom), (0, 0, 0))

        for filename, top, left in tiles:
            patch_path = os.path.join(input_dir, filename)
            patch = Image.open(patch_path)
            canvas.paste(patch, (left, top))

        output_path = os.path.join(output_dir, f"{base}_merged.png")
        canvas.save(output_path)
        print(f"✅ Merged {base} → {output_path}")

# 실행
merge_per_original(
    input_dir="/home/davidlyoo/projects/Strip-R-CNN/work_dirs/strip_rcnn_s_fpn_1x_v6_le90/satellite/test_results",
    output_dir="merged_outputs",
    tile_size=1024  # split 시 사용한 타일 크기
)
