def split_data_by_president(combined_data):
   
    if combined_data.empty:
        return pd.DataFrame()

    # Make sure Year is numeric
    combined_data["Year"] = pd.to_numeric(
        combined_data["Year"],
        errors="coerce"
    )

    combined_data = combined_data.dropna(subset=["Year"])
    combined_data["Year"] = combined_data["Year"].astype(int)

    combined_data["President"] = np.nan
    combined_data["Party"] = np.nan

    for term in PRESIDENT_TERMS:

        president = term["president"]
        party = term["party"]
        start = term["start"]
        end = term["end"]

        mask = (
            (combined_data["Year"] >= start) &
            (combined_data["Year"] <= end)
        )

        combined_data.loc[mask, "President"] = president
        combined_data.loc[mask, "Party"] = party

    return combined_data




def make_line_chart(data):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=data, x="Year", y="Value", hue="Indicator", marker="o", ax=ax)
    ax.set_title("Economic Indicators Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Value")
    st.pyplot(fig)


def make_bar_chart(data):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=data, x="Year", y="Value", hue="Indicator", ax=ax)
    ax.set_title("Economic Indicators by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Value")
    plt.xticks(rotation=45)
    st.pyplot(fig)


def main():
    st.title("Economic Indicators by U.S. President")

    st.write(
        "This app separates scraped economic data by president. "
        "Use the dropdowns to choose a presidency and compare different visuals."
    )
    cleaned_tables = prepare_all_data()
    combined_tables = combine_tables(cleaned_tables)

    combined_data = split_data_by_president(combined_tables)
    if combined_data.empty:
        st.error("No data was loaded. Check your project_cache folder or scraped data.")
        return

    president_options = sorted(combined_data["President"].dropna().unique())

    selected_president = st.selectbox(
        "Choose a president:",
        president_options
    )

    president_data = combined_data[
        combined_data["President"] == selected_president
    ]

    indicator_options = sorted(president_data["Indicator"].dropna().unique())

    selected_indicators = st.multiselect(
        "Choose economic indicators to compare:",
        indicator_options,
        default=indicator_options
    )

    visual_choice = st.selectbox(
        "Choose a visual:",
        ["Line Chart", "Bar Chart", "Data Table"]
    )

    filtered_data = president_data[
        president_data["Indicator"].isin(selected_indicators)
    ]

    st.subheader(f"Data for {selected_president}")

    if filtered_data.empty:
        st.warning("No data available for this selection.")
        return

    party = filtered_data["Party"].iloc[0]
    start_year = filtered_data["Year"].min()
    end_year = filtered_data["Year"].max()

    st.write(f"Party: {party}")
    st.write(f"Years in dataset: {start_year} - {end_year}")

    if visual_choice == "Line Chart":
        make_line_chart(filtered_data)

    elif visual_choice == "Bar Chart":
        make_bar_chart(filtered_data)

    elif visual_choice == "Data Table":
        st.dataframe(filtered_data)

    st.subheader("Summary Statistics")
    summary = (
        filtered_data
        .groupby("Indicator")["Value"]
        .agg(["mean", "min", "max"])
        .reset_index())

    st.dataframe(summary)


if __name__ == "__main__":
    main()
