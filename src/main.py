def main():
    import polars as pl

    error_table = pl.read_csv("../sensingabstraction/dataset/v0/error_table.csv")
    detection_table = pl.read_csv(
        "../sensingabstraction/dataset/v0/detection_table.csv"
    )

    count = detection_table["associated_target_id"].is_nan().sum()
    print(count)

    filtered = detection_table.drop_nans()
    print(detection_table.shape)
    print(filtered.shape)

    """
    filtered = detection_table.drop_nans()
    print(detection_table.shape)
    print(filtered.shape)
    """


if __name__ == "__main__":
    main()
