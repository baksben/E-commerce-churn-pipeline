'''Test Preprocessing pipeline
'''
import pandas as pd
import numpy as np
from pandas.testing import *
from dspipeline.processing.prep import DropNaNs, FillNaNs

def test_drop_nans():
    df = pd.DataFrame({'Col1': [1.0,2.0,3.0, None, 5.0], 'Col2': [10,20,30,40,50]}, index=[0,1,2,3,4])
    out_df = pd.DataFrame({'Col1': [1.0,2.0,3.0, 5.0], 'Col2': [10,20,30,50]}, index=[0,1,2,4])
    na_dropped_df = DropNaNs(df, ['Col1']).drop()

    assert_frame_equal(out_df, na_dropped_df)

def test_fill_nans():
    df = pd.DataFrame({'Col1': [1.0,2.0,3.0, None, 5.0], 'Col2': [10.0,20.0,30.0,40.0,50.0]}, index=[0,1,2,3,4])
    out_df = pd.DataFrame({'Col1': [1.0,2.0,3.0, 2.75, 5.0], 'Col2': [10.0,20.0,30.0,40.0,50.0]}, index=[0,1,2,3,4])
    na_filled_df = FillNaNs(df, ['Col1']).fill()

    assert_frame_equal(out_df, na_filled_df)
