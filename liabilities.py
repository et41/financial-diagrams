def get_sankey_for_liabilities(nodes_proportion, data_total_liabilities):
    data2 = dict(
        type="sankey",
        valueformat=".4s",
        valuesuffix="B",
        arrangement="snap",
        domain={
            "x": [0.5, 0.99],
            "y": [0, 0.99],
        },
        node=dict(
            pad=5 * nodes_proportion[1],
            thickness=30,
            # x=[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.4, 0.4, 0],
            # y=[0.98, 0.9, 0.8, 0.7, 0.5, 0.3, 0.1, 0.2, 0.2, 0],
            line=dict(
                width=3,
                color="black"
            ),
            label=[
                "Long Term",
                "Other Payables",
                "Other Liabilities Non Current",
                "Accounts Payables",
                "Current Debt",
                "Current Deferred Liabilities",
                "Other Current Liabilities",
                "Non-Current",
                "Current",
                "Liabilities",
                ],
            color="rgb(43,160,45)"
        ),
        link=dict(
            # source=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            # target=[7, 7, 7, 8, 8, 8, 8, 9, 9],
            target=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            source=[7, 7, 7, 8, 8, 8, 8, 9, 9],
            value=data_total_liabilities,
            color="rgb(153,206,154)"
        )
    )
    return data2
