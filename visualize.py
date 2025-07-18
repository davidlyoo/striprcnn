import os
import cv2
import mmcv
import numpy as np
from mmcv import Config
from mmrotate.datasets import build_dataset
from mmdet.apis import init_detector
from mmrotate.core import obb2poly_np

# --- 설정 ---
config_file = 'configs/strip_rcnn/strip_rcnn_s_fpn_1x_v5_le90.py'
checkpoint_file = '/data2/strip_rcnn/dota+aihub/latest.pth'
result_file = 'work_dirs/strip_rcnn_s_fpn_1x_v5_le90/results.pkl'
output_dir = 'gt_vs_pred_visualization_v5'
os.makedirs(output_dir, exist_ok=True)

# --- 모델 및 데이터셋 로드 ---
cfg = Config.fromfile(config_file)
model = init_detector(config_file, checkpoint_file, device='cuda:0')
dataset = build_dataset(cfg.data.test)
results = mmcv.load(result_file)

# --- 시각화 루프 ---
for idx, result in enumerate(results):
    data_info = dataset.data_infos[idx]
    filename = data_info['filename']
    img_path = os.path.join(dataset.img_prefix, filename)
    img = mmcv.imread(img_path)
    img_gt = img.copy()
    img_pred = img.copy()

    # GT 폴리곤 그리기 (녹색)
    ann = dataset.get_ann_info(idx)
    for poly in ann['polygons']:
        pts = poly.reshape(-1, 2).astype(np.int32)
        cv2.polylines(img_gt, [pts], True, (0, 255, 0), 2)

    # 예측 박스 그리기 (빨간색)
    for cls_idx, dets in enumerate(result):
        for det in dets:
            if det[5] < 0.3:  # confidence threshold
                continue
            obb = det[:5]
            poly_with_score = obb2poly_np(np.array([obb]), version='le90')[0]  # shape: (8,) 또는 (9,)
            if len(poly_with_score) == 9:
                poly = poly_with_score[:8].astype(np.int32).reshape(-1, 2)
            else:
                poly = poly_with_score.astype(np.int32).reshape(-1, 2)

            label = dataset.CLASSES[cls_idx]
            cv2.polylines(img_pred, [poly], True, (0, 0, 255), 2)
            cv2.putText(img_pred, label, tuple(poly[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,255), 1)

    # 나란히 붙이기import os
import cv2
import mmcv
import numpy as np
from mmcv import Config
from mmrotate.datasets import build_dataset
from mmdet.apis import init_detector
from mmrotate.core import obb2poly_np

# --- 설정 ---
config_file = 'configs/strip_rcnn/strip_rcnn_s_fpn_1x_v5_le90.py'
checkpoint_file = '/data2/strip_rcnn/dota+aihub/latest.pth'
result_file = 'work_dirs/strip_rcnn_s_fpn_1x_v5_le90/results.pkl'
output_dir = 'gt_vs_pred_visualization_v5'
os.makedirs(output_dir, exist_ok=True)

# --- 모델 및 데이터셋 로드 ---
cfg = Config.fromfile(config_file)
model = init_detector(config_file, checkpoint_file, device='cuda:0')
dataset = build_dataset(cfg.data.test)
results = mmcv.load(result_file)

# --- 시각화 루프 ---
for idx, result in enumerate(results):
    data_info = dataset.data_infos[idx]
    filename = data_info['filename']
    img_path = os.path.join(dataset.img_prefix, filename)
    img = mmcv.imread(img_path)
    img_gt = img.copy()
    img_pred = img.copy()

    # GT 폴리곤 그리기 (녹색)
    ann = dataset.get_ann_info(idx)
    for poly in ann['polygons']:
        pts = poly.reshape(-1, 2).astype(np.int32)
        cv2.polylines(img_gt, [pts], True, (0, 255, 0), 2)

    # 예측 박스 그리기 (빨간색)
    for cls_idx, dets in enumerate(result):
        for det in dets:
            if det[5] < 0.3:  # confidence threshold
                continue
            obb = det[:5]
            poly = obb2poly_np(np.array([obb]), version='le90')[0]  # shape: (8,)

            # MMRotate 내부가 9개 요소 기대 시 대응
            if poly.shape[0] == 8:
                poly = np.concatenate([poly, [0.0]])  # dummy score

            poly = poly[:8].astype(np.int32).reshape(-1, 2)
            label = dataset.CLASSES[cls_idx]
            cv2.polylines(img_pred, [poly], True, (0, 0, 255), 2)
            cv2.putText(img_pred, label, tuple(poly[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

    # 나란히 붙이기
    combined = np.concatenate((img_gt, img_pred), axis=1)
    out_path = os.path.join(output_dir, f'compare_{filename}')
    cv2.imwrite(out_path, combined)

    if idx >= 9:  # 10장만 생성
        break

    combined = np.concatenate((img_gt, img_pred), axis=1)
    out_path = os.path.join(output_dir, f'compare_{filename}')
    cv2.imwrite(out_path, combined)

    if idx >= 9:  # 10장만 생성
        break
