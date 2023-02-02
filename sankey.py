# from openbb_terminal.sdk import openbb
import plotly.graph_objects as go
from financial_data import get_balance_sheet_total_assets, get_balance_sheet_total_liabilities

data_total_assets = get_balance_sheet_total_assets("AAPL")

data = dict(
    type="sankey",
    valueformat=".4s",
    valuesuffix="B",
    domain={
        "x": [0, 0.45],
        "y": [0.55, 1],
    },
    node=dict(
        pad=20,
        thickness=30,
        x=[0, 0, 0, 0, 0, 0, 0, 0, 0],
        y=[0, 0, 0, 0, 0, 0, 0, 0, 0],
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

data_total_liabilities = get_balance_sheet_total_liabilities("AAPL")
print(data_total_liabilities)
print(data_total_liabilities[1] + data_total_liabilities[2])
label_liabilities = ["Liabilities",
                     "Non-Current",
                     "Current",
                     "Long Term",
                     "Other Payables",
                     "Other Liabilities Non Current",
                     "Accounts Payables",
                     "Current Debt",
                     "Current Deferred Liabilities",
                     "Other Current Liabilities",
                     ],
print(label_liabilities)

data2 = dict(
    type="sankey",
    valueformat=".4s",
    valuesuffix="B",
    domain={
        "x": [0.45, 1],
        "y": [0.55, 1],
    },
    node=dict(
        pad=20,
        thickness=30,
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

layout = dict(
    title="Apple's Cash Flow Statement",
    font=dict(
        size=10
    ),
    autosize=True,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
)

color_for_lines = ["rgb(153,206,154)", "rgb(153,206,154)",
                   "rgb(153,206,154)", "rgb(153,206,154)",
                   "rgb(153,206,154)", "rgb(153,206,154)",
                   "rgb(153,206,154)", "rgb(153,206,154)",
                   "rgb(153,206,154)",
                   ]
fig = go.Figure(data=[data, data2], layout=layout)
fig.update_traces(
        textfont_size=14,
        link=dict(line=dict(width=2)),
        link_color=color_for_lines)
fig.show()
