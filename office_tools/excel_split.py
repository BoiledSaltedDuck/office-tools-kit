     1|#!/usr/bin/env python3
     2|"""
     3|Office Tools Kit - Excel文件按列拆分工具
     4|功能：按指定列的值，将一个Excel拆分成多个文件
     5|用法：excel-split [输入文件] [拆分依据列名]
     6|"""
     7|import sys
     8|import pandas as pd
     9|from pathlib import Path
    10|
    11|def split_excel(input_file, column_name, output_dir="拆分结果"):
    12|    if not Path(input_file).exists():
    13|        print(f"错误：文件 {input_file} 不存在")
    14|        return False
    15|    
    16|    try:
    17|        df = pd.read_excel(input_file)
    18|    except Exception as e:
    19|        print(f"错误：读取文件失败: {e}")
    20|        return False
    21|    
    22|    if column_name not in df.columns:
    23|        print(f"错误：列 '{column_name}' 不存在")
    24|        print(f"可用列: {list(df.columns)}")
    25|        return False
    26|    
    27|    out_path = Path(output_dir)
    28|    out_path.mkdir(exist_ok=True)
    29|    
    30|    groups = df.groupby(column_name)
    31|    total = 0
    32|    for name, group_df in groups:
    33|        safe_name = str(name).replace('/', '_').replace('\\', '_')
    34|        output_file = out_path / f"{safe_name}.xlsx"
    35|        group_df.to_excel(output_file, index=False)
    36|        print(f"  ✓ {output_file.name} ({len(group_df)}行)")
    37|        total += 1
    38|    
    39|    print(f"\n完成！拆分为 {total} 个文件")
    40|    print(f"输出目录: {output_dir}")
    41|    
    42|    # 推广信息
    43|    _show_promotion()
    44|    return True
    45|
def _show_promotion():
    print("\n" + "=" * 50)
    print("💡 Office Tools Kit - 办公效率工具集")
    print("📦 pip install office-tools-kit")
    print("☕ 如果帮到了您，欢迎打赏支持:")
    print("   USDT(TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa")
    print("⭐ https://github.com/office-tools-kit/office-tools-kit")
    print("=" * 50)
    52|
    53|def main():
    54|    if len(sys.argv) < 3:
    55|        print("用法: excel-split [输入文件] [拆分依据列名]")
    56|        print("示例: excel-split 数据.xlsx 部门")
    57|        sys.exit(1)
    58|    
    59|    output_dir = sys.argv[3] if len(sys.argv) > 3 else "拆分结果"
    60|    success = split_excel(sys.argv[1], sys.argv[2], output_dir)
    61|    sys.exit(0 if success else 1)
    62|
    63|if __name__ == "__main__":
    64|    main()
    65|