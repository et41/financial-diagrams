import plotly.graph_objects as go
from assets import get_sankey_for_assets
from liabilities import get_sankey_for_liabilities
from financial_data import get_balance_sheet_total_assets, get_balance_sheet_total_liabilities, get_balance_sheet_equity
from node_proportion import node_arrangement

data_total_assets = get_balance_sheet_total_assets("AAPL")
data_total_liabilities = get_balance_sheet_total_liabilities("AAPL")
data_total_equities = get_balance_sheet_equity("AAPL")
print(data_total_assets, data_total_equities)
data_for_nodes = [data_total_assets[9], data_total_liabilities[9]]
nodes_proportion = node_arrangement(data_for_nodes)
data_total_assets.append(data_total_equities[0])
data_total_assets.append(data_total_equities[1])
print(data_total_assets)
data_obj = {
    "Cash and Short Term Inv.": data_total_assets[0],
    "Receivables": data_total_assets[1],
    "Inventory": data_total_assets[2],
    "Other Current Assets": data_total_assets[3],
    "Current Assets": data_total_assets[4],
    "Net PPE": data_total_assets[5],
    "Investment And Advances": data_total_assets[6],
    "Other Non-current Assets": data_total_assets[7],
    "Total Non-current Assets": data_total_assets[8],
    "Total Assets": data_total_assets[9],
    "Equities": data_total_assets[10],
    "Liabilities": data_total_assets[11],
}
print(data_obj)
#data = get_sankey_for_assets(nodes_proportion, data_total_assets)
data = dict(
        type="sankey",
        valueformat=".4s",
        valuesuffix="B",
        node=dict(
            #pad=5 * nodes_proportion[0],
            pad = 10,
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
                "Total Assets",
                "Liabilities",
                "Equities"],
            color="rgb(43,160,45)"
        ),
        link=dict(
            source=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9],
            target=[4, 4, 4, 4, 9, 8, 8, 8, 9, 10, 11],
            value=data_total_assets,
            color="rgb(153,206,154)"
        )
    )

layout = dict(
    title="Apple's Cash Flow Statement",
    width=1200,
    height=800,
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
                   "rgb(153,206,154)",   "rgb(153,206,154)",
                    "rgb(153,206,154)",
                   ]

fig = go.Figure(data=data, layout=layout)
fig.update_traces(
        textfont_size=14,
        link=dict(line=dict(width=2)),
        link_color=color_for_lines)
fig.show()