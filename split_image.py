from PIL import Image
import os

def split_image(image_path, output_dir, tile_size=1024, overlap=0):
    Image.MAX_IMAGE_PIXELS = None  # PIL 제한 해제

    os.makedirs(output_dir, exist_ok=True)

    img = Image.open(image_path)
    img_w, img_h = img.size
    basename = os.path.splitext(os.path.basename(image_path))[0]

    count = 0
    for top in range(0, img_h, tile_size - overlap):
        for left in range(0, img_w, tile_size - overlap):
            right = min(left + tile_size, img_w)
            bottom = min(top + tile_size, img_h)

            patch = img.crop((left, top, right, bottom))
            patch_w, patch_h = patch.size

            # 마지막 타일만 패딩
            if patch_w < tile_size or patch_h < tile_size:
                padded = Image.new('RGB', (tile_size, tile_size), (0, 0, 0))
                padded.paste(patch, (0, 0))
                patch = padded

            patch_name = f"{basename}_{top}_{left}.png"
            patch.save(os.path.join(output_dir, patch_name))
            count += 1

    print(f"[✔] {basename} → 총 {count}개 타일 저장 완료")
    print(f"    경로: {output_dir}")


if __name__ == "__main__":
    split_image("/data2/Satellite/02_PNEO_RGB_8bit_Linear_Scaling.png", "/data2/Satellite/patches")
    split_image("/data2/Satellite/03_PNEO_RGB_8bit_Custom.png", "/data2/Satellite/patches")
