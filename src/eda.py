# %% Imports and setup
import os

import plotly.express as px
import plotly.graph_objects as go
import polars as pl

pl.Config.set_tbl_rows(50)

targets = pl.read_csv("sensingabstraction/dataset/v0/target_table.csv")
detect = pl.read_csv("sensingabstraction/dataset/v0/detection_table.csv")
error = pl.read_csv("sensingabstraction/dataset/v0/error_table.csv")


def save(name: str | list[str]) -> None:
    match name:
        case str():
            files = {
                "targets": lambda: targets.write_csv("data/targets.csv"),
                "detect": lambda: detect.write_csv("data/detect.csv"),
                "error": lambda: error.write_csv("data/error.csv"),
            }
            files[name]()
        case [first, *rest]:
            save(first)
            save(rest)
        case []:
            return


# %% Main scripts
targets, detect, error = (
    df.filter(pl.col("scenario_id") == "uma_trp1_h38901_isac_Datasetv0")
    for df in [targets, detect, error]
)


# %%
false_positives = detect.filter(pl.col("associated_target_id").is_nan()).height

false_negatives = targets.filter(
    ~pl.col("target_id").is_in(detect["associated_target_id"].to_list())
)


x = targets["target_x_m"]
y = targets["target_y_m"]
z = targets["target_z_m"]

fig = go.Figure(
    data=[
        go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode="markers",
            marker=dict(
                size=5,
                color=z,  # color by z value
                colorscale="Viridis",
                opacity=0.8,
            ),
        )
    ]
)
fig.write_html("plot.html")


save(["error", "targets", "detect"])
