# from PIL import Image
# import os

# def check_image_size(image_path, tile_size=1024):
#     # 💣 DecompressionBombError 방지
#     Image.MAX_IMAGE_PIXELS = None

#     # 이미지 열기
#     img = Image.open(image_path)
#     width, height = img.size

#     print(f"[INFO] 이미지 경로: {image_path}")
#     print(f"[INFO] 이미지 크기: {width} x {height} (가로 x 세로)")
#     print(f"[INFO] 타일 크기: {tile_size} x {tile_size}")

#     # 몇 개의 패치가 나오는지 계산
#     num_tiles_x = width // tile_size
#     num_tiles_y = height // tile_size

#     remainder_x = width % tile_size
#     remainder_y = height % tile_size

#     print(f"[INFO] 생성 가능한 전체 타일 수:")
#     print(f"       가로 방향: {num_tiles_x} 개")
#     print(f"       세로 방향: {num_tiles_y} 개")
#     print(f"       총 합계: {num_tiles_x * num_tiles_y} 개")
#     print()

#     print(f"[INFO] 남는 영역:")
#     print(f"       오른쪽: {remainder_x} px")
#     print(f"       아래쪽: {remainder_y} px")

#     if remainder_x > 0 or remainder_y > 0:
#         print("⚠️  일부 영역은 타일로 나누어지지 않고 남습니다.")
#         print("👉  처리 전략을 결정해야 합니다: (패딩 / 잘라서 저장 / 버리기 등)")

# # 실행 예시
# if __name__ == "__main__":
#     img_path = "/data2/Satellite/02_PNEO_RGB_8bit_Linear_Scaling.png"
#     check_image_size(img_path, tile_size=1024)

# [INFO] 이미지 경로: /data2/Satellite/02_PNEO_RGB_8bit_Linear_Scaling.png
# [INFO] 이미지 크기: 46909 x 94237 (가로 x 세로)
# [INFO] 타일 크기: 1024 x 1024
# [INFO] 생성 가능한 전체 타일 수:
#        가로 방향: 45 개
#        세로 방향: 92 개
#        총 합계: 4140 개

# [INFO] 남는 영역:
#        오른쪽: 829 px
#        아래쪽: 29 px
# # ⚠️  일부 영역은 타일로 나누어지지 않고 남습니다.
# # 👉  처리 전략을 결정해야 합니다: (패딩 / 잘라서 저장 / 버리기 등)


# from PIL import Image

# Image.MAX_IMAGE_PIXELS = None
# img = Image.open("/data2/Satellite/03_PNEO_RGB_8bit_Custom.png")
# w, h = img.size

# # 중앙 2048x2048 타일 추출
# left = w // 2 - 1024
# top = h // 2 - 1024
# right = left + 2048
# bottom = top + 2048

# crop = img.crop((left, top, right, bottom))
# crop.save("/data2/Satellite/center_patch_custom.png")

# print("중앙 영역 추출 완료: center_patch_custom.png")
