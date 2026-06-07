     1|#!/usr/bin/env python3
     2|"""
     3|Office Tools Kit - PDF合并工具
     4|功能：合并多个PDF文件为一个
     5|用法：pdf-merge [输入目录] [输出文件]
     6|"""
     7|import sys
     8|from pathlib import Path
     9|
    10|try:
    11|    from PyPDF2 import PdfMerger
    12|except ImportError:
    13|    print("正在安装 PyPDF2...")
    14|    import subprocess
    15|    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2", "-q"])
    16|    from PyPDF2 import PdfMerger
    17|
    18|def merge_pdfs(input_dir, output_file):
    19|    input_path = Path(input_dir)
    20|    if not input_path.exists():
    21|        print(f"错误：目录 {input_dir} 不存在")
    22|        return False
    23|    
    24|    pdf_files = list(input_path.glob("*.pdf"))
    25|    if not pdf_files:
    26|        print(f"错误：目录 {input_dir} 中没有PDF文件")
    27|        return False
    28|    
    29|    # 按文件名排序
    30|    pdf_files.sort()
    31|    print(f"找到 {len(pdf_files)} 个PDF文件")
    32|    
    33|    merger = PdfMerger()
    34|    for f in pdf_files:
    35|        try:
    36|            merger.append(str(f))
    37|            print(f"  ✓ {f.name}")
    38|        except Exception as e:
    39|            print(f"  ✗ {f.name} 添加失败: {e}")
    40|    
    41|    merger.write(output_file)
    42|    merger.close()
    43|    
    44|    output_size = Path(output_file).stat().st_size
    45|    print(f"\n完成！输出文件: {output_file}")
    46|    print(f"文件大小: {output_size / 1024:.1f} KB")
    47|    
    48|    # 推广信息
    49|    _show_promotion()
    50|    return True
    51|
def _show_promotion():
    print("\n" + "=" * 50)
    print("💡 Office Tools Kit - 办公效率工具集")
    print("📦 pip install office-tools-kit")
    print("☕ 如果帮到了您，欢迎打赏支持:")
    print("   USDT(TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa")
    print("⭐ https://github.com/office-tools-kit/office-tools-kit")
    print("=" * 50)
    58|
    59|def main():
    60|    if len(sys.argv) < 3:
    61|        print("用法: pdf-merge [输入目录] [输出文件]")
    62|        print("示例: pdf-merge ./pdf文件/ 合并结果.pdf")
    63|        sys.exit(1)
    64|    
    65|    success = merge_pdfs(sys.argv[1], sys.argv[2])
    66|    sys.exit(0 if success else 1)
    67|
    68|if __name__ == "__main__":
    69|    main()
    70|