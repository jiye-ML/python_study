"""
对 data_frame 的每个行处理， 利用多线程加速
"""

def sentence_proc(sentence):
  '''
  预处理模块
  :param sentence:待处理字符串
  :return: 处理后的字符串
  '''
  # 清除无用词
  sentence = clean_sentence(sentence)
  # 切词，默认精确模式，全模式cut参数cut_all=True
  words = jieba.cut(sentence)
  # 过滤停用词
  words = filter_stopwords(words)
  # 拼接成一个字符串,按空格分隔
  return ' '.join(words)


# 处理函数
def data_frame_proc(df):
  '''
  数据集批量处理方法
  :param df: 数据集
  :return:处理好的数据集
  '''
  # 批量预处理 训练集和测试集
  for col_name in ['Brand', 'Model', 'Question', 'Dialogue']:
    df[col_name] = df[col_name].apply(sentence_proc)

  if 'Report' in df.columns:
    # 训练集 Report 预处理
    df['Report'] = df['Report'].apply(sentence_proc)
  return df


import numpy as np
from multiprocessing import cpu_count, Pool

# cpu 数量
cores = cpu_count()
# 分块个数
partitions = cores


def parallelize(df, func):
  """
  多核并行处理模块
  :param df: DataFrame数据
  :param func: 预处理函数
  :return: 处理后的数据
  """
  # 数据切分
  data_split = np.array_split(df, partitions)
  # 进程池
  pool = Pool(cores)
  # 数据分发 合并
  data = pd.concat(pool.map(func, data_split))
  # 关闭进程池
  pool.close()
  # 执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
  pool.join()
  return data


# 多线程处理预处理
train_df = parallelize(train_df, data_frame_proc);
test_df = parallelize(test_df, data_frame_proc);