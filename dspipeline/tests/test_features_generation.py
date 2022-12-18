'''Test Feature Generation pipeline
'''
import pandas as pd
import numpy as np
from pandas.testing import *
from dspipeline.processing.transformer import Dummifier, Binarizer, Logger


def test_dummy_generator():
    df = pd.DataFrame({'Col1': ['Type 1', 'Type 2', 'Type 3', 'Type 1', 'Type 3'], 'Col2': [10,20,30,40,50]}, index=[0,1,2,3,4])
    out_df = pd.DataFrame({ 'Col2': [10,20,30,40,50], 'Col1_Type 1': [1.0,0,0,1,0], 'Col1_Type 2': [0.0,1,0,0,0], 'Col1_Type 3': [0,0,1,0,1.0]}, index=[0,1,2,3,4])
    df_dummified = Dummifier(df, ['Col1']).generate()

    assert_frame_equal(out_df, df_dummified, check_dtype=False)

def test_binary_generator():
    df = pd.DataFrame({'Col1': ['Type 1', 'Type 2', 'Type 1', 'Type 1', 'Type 2'], 'Col2': [10,20,30,40,50]}, index=[0,1,2,3,4])
    out_df = pd.DataFrame({ 'Col2': [10,20,30,40,50], 'T1/T2': [0,1,0,0,1]}, index=[0,1,2,3,4])
    df_binarized = Binarizer(df, 'Col1', 'T1/T2').generate()

    assert_frame_equal(out_df, df_binarized, check_dtype=False)

def test_log_generator():
    df = pd.DataFrame({'Col1': [1.0,2.0,3.0, 4.0, 5.0], 'Col2': [10.0,20.0,30.0,40.0,50.0]}, index=[0,1,2,3,4])
    out_df = pd.DataFrame({'Col1': [1.0,2.0,3.0, 4, 5.0], 'Col2': [10.0,20.0,30.0,40.0,50.0], 'Col1_logged': [0.000000, 0.693147, 1.098612, 1.386294, 1.609438]}, index=[0,1,2,3,4])
    df_logged = Logger(df, 'Col1').generate()

    assert_frame_equal(out_df, df_logged, check_dtype=False)