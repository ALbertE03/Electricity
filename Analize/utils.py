import os
import pandas as pd


def filter_date(df, date_start, date_end, col):
    return df[(date_start <= df[col]) & (df[col] < date_end)]


def join_path(*args):
    return os.path.join(*map(str, args))


def create_df(primer, path):
    list_dfs = []
    d = len(os.listdir(path)) - 1
    for i in range(primer, primer + d):
        path_ = join_path(path, str(i))
        for j in os.listdir(path_):
            df = pd.read_json(join_path(path_, j))
            list_dfs.append(df)
    return pd.concat(list_dfs)
