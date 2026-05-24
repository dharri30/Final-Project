
PRESIDENT_TERMS = [
    {"president": "George Washington", "party": "No Party", "start": 1789, "end": 1797},
    {"president": "John Adams", "party": "Federalist", "start": 1797, "end": 1801},
    {"president": "Thomas Jefferson", "party": "Democratic-Republican", "start": 1801, "end": 1809},
    {"president": "James Madison", "party": "Democratic-Republican", "start": 1809, "end": 1817},
    {"president": "James Monroe", "party": "Democratic-Republican", "start": 1817, "end": 1825},
    {"president": "John Quincy Adams", "party": "Democratic-Republican", "start": 1825, "end": 1829},
    {"president": "Andrew Jackson", "party": "Democrat", "start": 1829, "end": 1837},
    {"president": "Martin Van Buren", "party": "Democrat", "start": 1837, "end": 1841},
    {"president": "William Henry Harrison", "party": "Whig", "start": 1841, "end": 1841},
    {"president": "John Tyler", "party": "Whig", "start": 1841, "end": 1845},
    {"president": "James K. Polk", "party": "Democrat", "start": 1845, "end": 1849},
    {"president": "Zachary Taylor", "party": "Whig", "start": 1849, "end": 1850},
    {"president": "Millard Fillmore", "party": "Whig", "start": 1850, "end": 1853},
    {"president": "Franklin Pierce", "party": "Democrat", "start": 1853, "end": 1857},
    {"president": "James Buchanan", "party": "Democrat", "start": 1857, "end": 1861},
    {"president": "Abraham Lincoln", "party": "Republican", "start": 1861, "end": 1865},
    {"president": "Andrew Johnson", "party": "Democrat", "start": 1865, "end": 1869},
    {"president": "Ulysses S. Grant", "party": "Republican", "start": 1869, "end": 1877},
    {"president": "Rutherford B. Hayes", "party": "Republican", "start": 1877, "end": 1881},
    {"president": "James Garfield", "party": "Republican", "start": 1881, "end": 1881},
    {"president": "Chester Arthur", "party": "Republican", "start": 1881, "end": 1885},
    {"president": "Grover Cleveland", "party": "Democrat", "start": 1885, "end": 1889},
    {"president": "Benjamin Harrison", "party": "Republican", "start": 1889, "end": 1893},
    {"president": "Grover Cleveland", "party": "Democrat", "start": 1893, "end": 1897},
    {"president": "William McKinley", "party": "Republican", "start": 1897, "end": 1901},
    {"president": "Theodore Roosevelt", "party": "Republican", "start": 1901, "end": 1909},
    {"president": "William Howard Taft", "party": "Republican", "start": 1909, "end": 1913},
    {"president": "Woodrow Wilson", "party": "Democrat", "start": 1913, "end": 1921},
    {"president": "Warren Harding", "party": "Republican", "start": 1921, "end": 1923},
    {"president": "Calvin Coolidge", "party": "Republican", "start": 1923, "end": 1929},
    {"president": "Herbert Hoover", "party": "Republican", "start": 1929, "end": 1933},
    {"president": "Franklin D. Roosevelt", "party": "Democrat", "start": 1933, "end": 1945},
    {"president": "Harry Truman", "party": "Democrat", "start": 1945, "end": 1953},
    {"president": "Dwight Eisenhower", "party": "Republican", "start": 1953, "end": 1961},
    {"president": "John F. Kennedy", "party": "Democrat", "start": 1961, "end": 1963},
    {"president": "Lyndon Johnson", "party": "Democrat", "start": 1963, "end": 1969},
    {"president": "Richard Nixon", "party": "Republican", "start": 1969, "end": 1974},
    {"president": "Gerald Ford", "party": "Republican", "start": 1974, "end": 1977},
    {"president": "Jimmy Carter", "party": "Democrat", "start": 1977, "end": 1981},
    {"president": "Ronald Reagan", "party": "Republican", "start": 1981, "end": 1989},
    {"president": "George H. W. Bush", "party": "Republican", "start": 1989, "end": 1993},
    {"president": "Bill Clinton", "party": "Democrat", "start": 1993, "end": 2001},
    {"president": "George W. Bush", "party": "Republican", "start": 2001, "end": 2009},
    {"president": "Barack Obama", "party": "Democrat", "start": 2009, "end": 2017},
    {"president": "Donald Trump", "party": "Republican", "start": 2017, "end": 2021},
    {"president": "Joe Biden", "party": "Democrat", "start": 2021, "end": 2025},
    {"president": "Donald Trump", "party": "Republican", "start": 2025, "end": 2029},
]


def split_data_by_president(combined_df):
    
    if combined_df.empty:
        return {}

    president_data = {}

    
    combined_df["Year"] = pd.to_numeric(
        combined_df["Year"],
        errors="coerce"
    )

    # Remove rows with missing years
    combined_df = combined_df.dropna(subset=["Year"])

    # Convert Year to integer
    combined_df["Year"] = combined_df["Year"].astype(int)

    for term in PRESIDENT_TERMS:
        president = term["president"]
        start = term["start"]
        end = term["end"]

        president_df = combined_df[
            (combined_df["Year"] >= start) &
            (combined_df["Year"] <= end)
        ].copy()

        # Add president + party columns
        president_df["President"] = president
        president_df["Party"] = term["party"]

        # Store in dictionary
        key = f"{president} ({start}-{end})"

        president_data[key] = president_df

    return president_data