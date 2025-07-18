#!/usr/bin/env python3
"""
MMRotate Strip R-CNN 빠른 디버깅 스크립트

사용법:
python quick_debug.py
"""

import os
import glob
from pathlib import Path

def main():
    print("🚀 MMRotate Strip R-CNN 빠른 문제 진단")
    print("=" * 60)
    
    # 1. 경로 확인
    data_root = '/data2/Satellite/'
    ann_path = os.path.join(data_root, 'annotation')
    img_path = os.path.join(data_root, 'patches')
    
    print(f"\n📁 경로 확인:")
    print(f"  Data root: {data_root} -> {os.path.exists(data_root)}")
    print(f"  Annotation: {ann_path} -> {os.path.exists(ann_path)}")
    print(f"  Images: {img_path} -> {os.path.exists(img_path)}")
    
    # 2. 파일 수 확인
    if os.path.exists(ann_path):
        ann_files = glob.glob(os.path.join(ann_path, '*.txt'))
        print(f"\n📝 Annotation 파일: {len(ann_files)}개")
    else:
        ann_files = []
        print(f"\n❌ Annotation 경로가 존재하지 않습니다!")
    
    if os.path.exists(img_path):
        img_extensions = ['*.png', '*.jpg', '*.jpeg', '*.tif', '*.tiff']
        img_files = []
        for ext in img_extensions:
            img_files.extend(glob.glob(os.path.join(img_path, ext)))
        print(f"🖼️ Image 파일: {len(img_files)}개")
        
        if img_files:
            ext_count = {}
            for img_file in img_files:
                ext = Path(img_file).suffix.lower()
                ext_count[ext] = ext_count.get(ext, 0) + 1
            print(f"   확장자별: {ext_count}")
    else:
        img_files = []
        print(f"\n❌ Image 경로가 존재하지 않습니다!")
    
    # 3. 주요 문제 진단
    print(f"\n🔍 문제 진단:")
    
    issues = []
    
    if not ann_files and not img_files:
        issues.append("❌ Annotation과 Image 파일이 모두 없습니다")
    elif not ann_files:
        issues.append("⚠️ Annotation 파일이 없습니다 (inference 모드에서는 정상)")
    elif not img_files:
        issues.append("❌ Image 파일이 없습니다")
    
    # 4. 시각화 문제 확인
    issues.append("⚠️ 시각화가 안 되는 이유: 테스트 명령어에 --show 플래그가 없습니다")
    
    if issues:
        for issue in issues:
            print(f"  {issue}")
    else:
        print("  ✅ 기본적인 파일 구조는 정상입니다")
    
    # 5. 해결 방안
    print(f"\n💡 해결 방안:")
    print("  1. 시각화 활성화:")
    print("     기존: --show-dir work_dirs/.../test_results/")
    print("     수정: --show --show-dir work_dirs/.../test_results/")
    
    print("\n  2. 이미지 확장자 문제가 있다면:")
    print("     - V5Dataset.load_annotations 메서드 수정 필요")
    print("     - 여러 확장자 자동 탐지 기능 추가")
    
    print("\n  3. 빠른 테스트:")
    print("     첫 번째 이미지 파일 확인 중...")
    
    if img_files:
        first_img = img_files[0]
        print(f"     ✅ 첫 번째 이미지: {Path(first_img).name}")
        print(f"     크기: {os.path.getsize(first_img) / (1024*1024):.1f} MB")
        
        if ann_files:
            first_ann = ann_files[0]
            print(f"     ✅ 첫 번째 annotation: {Path(first_ann).name}")
            
            # 간단한 annotation 내용 확인
            try:
                with open(first_ann, 'r') as f:
                    lines = f.readlines()
                print(f"     annotation 라인 수: {len(lines)}")
                if lines:
                    print(f"     첫 라인: {lines[0].strip()[:50]}...")
            except Exception as e:
               print(f"     ❌ annotation 읽기 오류: {e}")
   
    print(f"\n" + "=" * 60)
    print("✅ 진단 완료!")
    print("\n🔧 추천 다음 단계:")
    print("1. python debug_mmrotate_test.py 실행 (상세 진단)")
    print("2. 테스트 명령어에 --show 플래그 추가")
    print("3. 필요시 fix_v5_dataset.py의 수정 사항 적용")

if __name__ == "__main__":
    main()