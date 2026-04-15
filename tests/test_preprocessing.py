# tests/test_preprocessing.py

import pandas as pd
import pytest

def test_sample_inbound_loads():
    """Sample inbound file must load and have expected columns"""
    df = pd.read_csv("data/sample/inbound_sample.csv")
    assert len(df) > 0
    assert "airport_A"  in df.columns
    assert "delayed"    in df.columns
    assert "Date"       in df.columns

def test_sample_outbound_loads():
    """Sample outbound file must load and have expected columns"""
    df = pd.read_csv("data/sample/outbound_sample.csv")
    assert len(df) > 0
    assert "airport_B"  in df.columns
    assert "Date"       in df.columns

def test_delayed_column_is_binary():
    """delayed column must only contain 0 and 1"""
    df = pd.read_csv("data/sample/inbound_sample.csv")
    assert df["delayed"].isin([0, 1]).all()

def test_no_null_airport():
    """airport_A must have no nulls in sample"""
    df = pd.read_csv("data/sample/inbound_sample.csv")
    assert df["airport_A"].isnull().sum() == 0