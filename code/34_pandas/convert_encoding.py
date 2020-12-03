import argparse
import pandas as pd


def convert_encoding(file_path, origin_encoding, dest_encoding):
  _df = pd.read_csv(file_path, encoding=origin_encoding)
  _df.to_csv(file_path, encoding=dest_encoding, index=False)


if __name__ == '__main__':

  parser = argparse.ArgumentParser(
    description="csv 文件转换编码"
  )
  parser.add_argument(
    '-f', '--file_path', type=str, nargs='?', help='csv file path'
  )
  parser.add_argument(
    '-o', '--origin_encoding', type=str, help='input file encoding'
  )
  parser.add_argument(
    '-d', '--dest_encoding', type=str, help='dest file encoding'
  )
  args = parser.parse_args()

  convert_encoding(args.file_path, args.origin_encoding, args.dest_encoding)
