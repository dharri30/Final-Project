def test_split_data_by_president():
    fake_df = pd.DataFrame({
        "Year": [2008, 2010, 2012, 2018, 2022],
        "Value": [1, 2, 3, 4, 5],
        "Indicator": [
            "GDP",
            "GDP",
            "Inflation",
            "Unemployment",
            "GDP"
        ]
    })

    result = split_data_by_president(fake_df)

    # Check dictionary returned
    assert isinstance(result, dict)

    assert "Barack Obama (2009-2017)" in result

    obama_df = result["Barack Obama (2009-2017)"]

    
    assert isinstance(obama_df, pd.DataFrame)

    assert len(obama_df) == 2

    assert all(obama_df["President"] == "Barack Obama")

    # Check party column added
    assert all(obama_df["Party"] == "Democrat")

    # Check years are within range
    assert obama_df["Year"].min() >= 2009
    assert obama_df["Year"].max() <= 2017