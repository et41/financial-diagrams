import plotly.graph_objects as go
from assets import get_sankey_for_assets
from liabilities import get_sankey_for_liabilities
from financial_data import get_balance_sheet_total_assets, get_balance_sheet_total_liabilities, get_balance_sheet_equity, get_all_data
from node_proportion import node_arrangement
"""
data_total_assets = get_balance_sheet_total_assets("AAPL")
data_total_liabilities = get_balance_sheet_total_liabilities("AAPL")
data_total_equities = get_balance_sheet_equity("AAPL")
data_total_assets.append(data_total_equities[0])
data_total_assets.append(data_total_equities[1])
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
"""

all_data = get_all_data("AAPL")
headers = ["Assets", "Liabilities", "Equities"]
label_and_color = {
    "Cash and Short Term Inv.": "rgb(43,160,45)",
    "Receivables": "rgb(43,160,45)",
    "Inventory": "rgb(43,160,45)",
    "Other Current Assets":"rgb(43,160,45)",
    "Current Assets": "rgb(43,160,45)",
    "Net PPE" :"rgb(43,160,45)",
    "Investment And Advances": "rgb(43,160,45)",
    "Other Non-current Assets": "rgb(43,160,45)",
    "Total Non-current Assets": "rgb(43,160,45)",
    "Total Assets": "rgb(43,160,45)",
    "Equities": "rgb(255,0,0)",
    "Liabilities": "rgb(255,0,0)",
}

#data = get_sankey_for_assets(nodes_proportion, data_total_assets)
data = dict(
        type="sankey",
        valueformat=".4s",
  
        valuesuffix="B",
        arrangement="snap",
        node=dict(
            pad = 1,
            thickness=20,
            x = [0.1, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1, 0.3 , 0.5 , 0.52 , 0.52], # specify x positions
            y = [ .8 , .8 , .6 , .6 , .4 , .4 , .3 , .3 , .2 , .2 , .1 , .1] ,# specify y positions
            line=dict(
                width=3,
                color="black"
            ),
            label= list(label_and_color.keys()),
            #color=["rgb(43,160,45)" if i < len(all_data) - 1 else "rgb(255,0,0)" for i in range(0,len(all_data) + 1)]
            color = list(label_and_color.values()),
        ),
        link=dict(
            #source=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9],
            #target=[4, 4, 4, 4, 9, 8, 8, 8, 9, 10, 11],
            source=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9],
            target=[4, 4, 4, 4, 9, 8, 8, 8, 9, 10, 11],
            #value=list(data_obj.values()),
            value = all_data,
            color=["rgb(155,206,154)" if i < len(all_data) - 2 else "rgb(255,255,255)" for i in range(0,len(all_data)) ]
        )
    )
print(data)
"""
layout = dict(
    title="Apple's Cash Flow Statement",
    #width=1200,
    #height=800,
    font=dict(
        size=10
    ),
    autosize=True,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
)
"""

layout = dict(
    title = dict(
        text = "Apple's Balance Sheet",
        font = dict(
            color = "rgb(0,0,0)",
            family = "Times New Roman",
            size = 18
        )
    ),
    font = dict(
        size = 10
    ), 
  
    

    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    margin = dict(t=50,r=50,b=100,l=100)
)

fig = go.Figure(data=data, layout=layout)
fig.update_traces(
        textfont_size=14,
        link=dict(line=dict(width=2)),
        )
fig.show()