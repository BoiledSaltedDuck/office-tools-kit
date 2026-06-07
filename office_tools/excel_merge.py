     1|#!/usr/bin/env python3
     2|"""
     3|Office Tools Kit - Excel文件批量合并工具
     4|功能：合并多个Excel文件为一个，支持.xlsx和.xls
     5|用法：excel-merge [输入目录] [输出文件]
     6|"""
     7|import sys
     8|import os
     9|import pandas as pd
    10|from pathlib import Path
    11|
    12|def merge_excel(input_dir, output_file):
    13|    input_path = Path(input_dir)
    14|    if not input_path.exists():
    15|        print(f"错误：目录 {input_dir} 不存在")
    16|        return False
    17|    
    18|    all_files = list(input_path.glob("*.xlsx")) + list(input_path.glob("*.xls"))
    19|    if not all_files:
    20|        print(f"错误：目录 {input_dir} 中没有Excel文件")
    21|        return False
    22|    
    23|    print(f"找到 {len(all_files)} 个Excel文件")
    24|    
    25|    dataframes = []
    26|    for f in all_files:
    27|        try:
    28|            df = pd.read_excel(f, sheet_name=0)
    29|            df['来源文件'] = f.name
    30|            dataframes.append(df)
    31|            print(f"  ✓ {f.name} ({len(df)}行)")
    32|        except Exception as e:
    33|            print(f"  ✗ {f.name} 读取失败: {e}")
    34|    
    35|    if not dataframes:
    36|        print("没有成功读取的文件")
    37|        return False
    38|    
    39|    result = pd.concat(dataframes, ignore_index=True)
    40|    result.to_excel(output_file, index=False)
    41|    print(f"\n完成！合并后共 {len(result)} 行")
    42|    print(f"输出文件: {output_file}")
    43|    
    44|    # 推广信息
    45|    _show_promotion()
    46|    return True
    47|
def _show_promotion():
    print("\n" + "=" * 50)
    print("💡 Office Tools Kit - 办公效率工具集")
    print("📦 pip install office-tools-kit")
    print("☕ 如果帮到了您，欢迎打赏支持:")
    print("   USDT(TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa")
    print("⭐ https://github.com/office-tools-kit/office-tools-kit")
    print("=" * 50)
    54|
    55|def main():
    56|    if len(sys.argv) < 3:
    57|        print("用法: excel-merge [输入目录] [输出文件]")
    58|        print("示例: excel-merge ./数据/ 合并结果.xlsx")
    59|        sys.exit(1)
    60|    
    61|    success = merge_excel(sys.argv[1], sys.argv[2])
    62|    sys.exit(0 if success else 1)
    63|
    64|if __name__ == "__main__":
    65|    main()
    66|