# http://pandas.pydata.org/pandas-docs/stable/10min.html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Object Creation
def object_creation():

    # Series by list
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)

    # DataFrame by numpy array
    dates = pd.date_range('20170708', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)

    df2 = pd.DataFrame({
        'A': 1.,
        'B': pd.Timestamp('20170518'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(['test', 'train', 'test', 'train']),
        'F': 'foo'
    })
    print(df2)
    print(df2.dtypes)

    pass



# viewing data
def viewing_data():
    # DataFrame by numpy array
    dates = pd.date_range('20170518', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    # see the top & bottom rows  of the frame
    print(df.head(n=2))
    print(df.tail(n=2))
    # Display the index, columns, and the underlying numpy data
    print(df.index)
    print(df.columns)
    print(df.values)
    # Discribe shows a quick statistic summary of your data
    print(df.describe())

    # transposing your data
    print(df.T)

    # soring by an axis
    print(df.sort_index(axis=0, ascending=True))
    print(df.sort_index(axis=0, ascending=False))
    print(df.sort_index(axis=1, ascending=True))
    print(df.sort_index(axis=1, ascending=False))
    # sort by values
    print(df.sort_values(by='B'))
    print(df.sort_values(by=['A', 'B']))
    pass


def selection_getting():
    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    # Selecting a single column, which yields a Series, equivalent to df.A
    print(df["A"])
    print(df.A)

    # Selecting via [], which slices the rows.
    print(df[0: 3])
    print(df["2017-05-20":"2017-05-22"])
    pass


def selection_by_label():
    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    # for getting a cross section using a label
    print(df.loc[dates[0]])

    # selecting on a multi-axis by label
    print(df.loc[:, ['A', 'B']])

    # showing label slicing, both endpoints are included
    print(df.loc[dates[1]:dates[3], ['A', 'B']])

    # reduction in the dimensions of the returned object
    print(df.loc[dates[2], ['C', 'B']])

    # for getting a scalar value
    print(df.loc[dates[2], 'C'])

    # for getting fast access to a scalar
    print(df.at[dates[2], 'B'])

    pass


def selection_by_position():
    dates = pd.date_range('20170707', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)

    # select via the position of the passed intergers
    print(df.iloc[3])

    # by integer slices, action similar to numpy
    print(df.iloc[2:4, 1:3])

    # by lists of integer position locations, similar to the numpy
    print(df.iloc[[1, 3, 5], 0: 3])
    print(df.iloc[[1, 3, 5], [0, 2, 3]])
    print(df.iloc[[1, 3, 5], :])

    # For getting a value explicitly
    print(df.iloc[1, 1])
    print(df.iat[1, 1])

    pass


def selection_by_boolean_indexing():
    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    # using a single column's values to select data
    print(df.A > 0)
    print(df[df.A > 0])
    # selecting values from a dataframe where a boolean condition is met
    print(df[df > 0])

    # using the isin() method for filtering
    df2 = df.copy()
    df2['B'] = ['1', '1', '2', '3', '3', '4']
    print(df2)
    print(df2[df2['B'].isin(['1', '2'])])

    # boolean list
    boolean = [True, False, False, True, True, True]
    print(df2[boolean])

    def iter(x):
        booleans = []
        for i in x.iloc[:, 1]:
            if i > 0:
                booleans.append(True)
            else:
                booleans.append(False)
        print(booleans)
        return booleans
    print(df2[lambda x: iter(x)])

    pass


def selection_by_setting():
    # DataFrame by numpy array
    dates = pd.date_range("20170518", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

    # setting a new column automatically aligns the data by the indexes
    s = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
    print(s)
    df['E'] = s
    print(df)
    df['D'] = s
    print(df)

    # setting values by label
    df.at[dates[2], 'B'] = 0
    print(df)

    # Setting values by position
    df.iat[3, 1] = 0
    print(df)

    # Setting by assigning with a numpy array
    df.loc[:, "C"] = np.array([5] * len(df))
    print(df)
    pass


def missing_data():

    pass


if __name__ == '__main__':

    selection_by_setting()

    pass
