from PIL import Image
import os

# ⚠️ 제한 해제
Image.MAX_IMAGE_PIXELS = None

def resize_image(input_path, output_path, scale=0.1):
    img = Image.open(input_path)
    w, h = img.size
    resized = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    resized.save(output_path)
    print(f"🔍 저장됨: {output_path} (해상도 {resized.size})")

# 예시 실행
resize_image(
    "merged_outputs/02_PNEO_RGB_8bit_Linear_Scaling_merged.png",
    "merged_outputs/02_PNEO_preview.png",
    scale=0.1
)
resize_image(
    "merged_outputs/03_PNEO_RGB_8bit_Custom_merged.png",
    "merged_outputs/03_PNEO_preview.png",
    scale=0.1
)
