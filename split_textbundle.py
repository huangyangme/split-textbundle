#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import re

def sanitize_filename(name):
    return re.sub(r'[\/:*?"<>|]', "_", name)

def split_textbundle(bundle_path, output_dir):
    markdown_file = os.path.join(bundle_path, "text.md")
    if not os.path.isfile(markdown_file):
        print(f"未找到 {markdown_file}")
        return

    os.makedirs(output_dir, exist_ok=True)

    with open(markdown_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 按一级标题拆分
    parts = re.split(r'(?m)^# (.+)', content)
    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        body = parts[i+1].strip()
        filename = sanitize_filename(title) + ".md"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as out_f:
            out_f.write(f"# {title}\n{body}\n")
        print(f"保存: {filepath}")

    # 复制 assets 文件夹
    assets_src = os.path.join(bundle_path, "assets")
    if os.path.isdir(assets_src):
        assets_dst = os.path.join(output_dir, "assets")
        if os.path.exists(assets_dst):
            shutil.rmtree(assets_dst)
        shutil.copytree(assets_src, assets_dst)
        print(f"复制 assets 文件夹到 {assets_dst}")

def main():
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 找到目录下唯一的 .textbundle 文件
    bundle_files = [f for f in os.listdir(current_dir) if f.endswith(".textbundle")]
    if len(bundle_files) != 1:
        print("请确保目录下只有一个 .textbundle 文件")
        return

    bundle_path = os.path.join(current_dir, bundle_files[0])
    output_dir = os.path.join(current_dir, "split_output")

    split_textbundle(bundle_path, output_dir)
    print("拆分完成！Markdown 文件已生成在 'split_output' 文件夹中。")

if __name__ == "__main__":
    main()