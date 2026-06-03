def main():
    print("Hello from twizzle!")
    import polars as pl

    error_table = pl.read_csv("../sensingabstraction/dataset/v0/error_table.csv")
    detection_table = pl.read_csv(
        "../sensingabstraction/dataset/v0/detection_table.csv"
    )


if __name__ == "__main__":
    main()
