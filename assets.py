def get_sankey_for_assets(nodes_proportion, data_total_assets):
    data = dict(
        type="sankey",
        valueformat=".4s",
        valuesuffix="B",
        domain={
            "x": [0, 0.5],
            "y": [0, 0.99],
        },
        node=dict(
            pad=5 * nodes_proportion[0],
            thickness=30,
            # x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            # y=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            line=dict(
                width=3,
                color="black"
            ),
            label=["Cash and Short Term Inv.",
                "Receivables",
                "Inventory",
                "Other Current Assets",
                "Current Assets",
                "Net PPE",
                "Investment And Advances",
                "Other Non-current Assets",
                "Total Non-current Assets",
                "Total Assets"],
            color="rgb(43,160,45)"
        ),
        link=dict(
            source=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            target=[4, 4, 4, 4, 9, 8, 8, 8, 9],
            value=data_total_assets,
            color="rgb(153,206,154)"
        )
    )

    return data