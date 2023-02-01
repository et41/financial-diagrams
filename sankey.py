from openbb_terminal.sdk import openbb
import plotly.graph_objects as go

balance_data = openbb.stocks.fa.balance("AAPL")["2022-09-30"]
cash_and_equivalents = balance_data["Cash and cash equivalents"]
other_shortterm_investments = balance_data["Other short-term investments"]
marketable_securities = balance_data["Other short-term investments"]
account_receviable = balance_data["Net receivables"]
inventory = balance_data["Inventory"]
other_current_assets = balance_data["Other current assets"]
total_current_assets = balance_data["Total current assets"]
# print(total_current_assets)

cash_and_shortterm_investment = cash_and_equivalents + other_shortterm_investments
receviables = total_current_assets - inventory - other_current_assets - cash_and_equivalents - other_shortterm_investments
current_assets = receviables + cash_and_equivalents + other_shortterm_investments + inventory + other_current_assets

gross_ppe = balance_data["Gross property, plant and equipment"]
accumulated_depreciation = balance_data["Accumulated depreciation"]
net_ppe = balance_data["Net property, plant and equipment"]

investment_and_advances = balance_data["Equity and other investments"]
other_non_current_assets = balance_data["Other long-term assets"]

total_non_current_assets = balance_data["Total non-current assets"]
total_assets = total_current_assets + total_non_current_assets

data = dict(
    type="sankey",
    valueformat=".4s",
    valuesuffix="B",
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
        value=[cash_and_shortterm_investment,
               receviables,
               inventory,
               other_current_assets,
               current_assets,
               net_ppe,
               investment_and_advances,
               other_non_current_assets,
               total_non_current_assets,
               total_assets,
               ],

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
fig = go.Figure(data=[data], layout=layout)
fig.update_traces(
        textfont_size=14,
        link=dict(line=dict(width=2)),
        link_color=color_for_lines)
fig.show()

