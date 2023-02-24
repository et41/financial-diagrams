# from openbb_terminal.sdk import openbb
import plotly.graph_objects as go
from assets import get_sankey_for_assets
from liabilities import get_sankey_for_liabilities
from financial_data import get_balance_sheet_total_assets, get_balance_sheet_total_liabilities, get_balance_sheet_equity
from node_proportion import node_arrangement

data_total_assets = get_balance_sheet_total_assets("AAPL")
data_total_liabilities = get_balance_sheet_total_liabilities("AAPL")
data_total_equities = get_balance_sheet_equity("AAPL")
print(data_total_liabilities, data_total_equities)
data_for_nodes = [data_total_assets[9], data_total_liabilities[9]]
nodes_proportion = node_arrangement(data_for_nodes)

data = get_sankey_for_assets(nodes_proportion, data_total_assets)
data2 = get_sankey_for_liabilities(nodes_proportion, data_total_liabilities)
# I have two input data and data2, i want you to write me code that will show two different sankey diagram
# that will show balance sheet asset and liabilities side.

"""
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
                   "rgb(153,206,154)",
                   ]

fig = go.Figure(data=data, layout=layout)
fig.update_traces(
        textfont_size=14,
        link=dict(line=dict(width=2)),
        link_color=color_for_lines)
fig.show()
"""
