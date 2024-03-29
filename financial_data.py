from openbb_terminal.sdk import openbb

class DataBalanceSheet:
    def __init__(self, ticker):
        self.data = openbb.stocks.fa.balance(ticker)["2022-09-30"]

def get_balance_sheet_total_assets(ticker: str):
    print(ticker)
    balance_data = openbb.stocks.fa.balance(ticker)["2022-09-30"]
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
    return [cash_and_shortterm_investment,
            receviables,
            inventory,
            other_current_assets,
            current_assets,
            net_ppe,
            investment_and_advances,
            other_non_current_assets,
            total_non_current_assets,
            total_assets,
            ]


def get_balance_sheet_total_liabilities(ticker: str):
    print(openbb.stocks.fa.balance(ticker))
    balance_data = openbb.stocks.fa.balance(ticker)["2022-09-30"]
    total_liabilities = balance_data["Total liabilities"]
    total_current_liabilities = balance_data["Total current liabilities"]
    total_non_current_liabilities = balance_data["Total non-current liabilities"]

    accounts_payables = balance_data["Accounts payable"]
    current_debt = balance_data["Current debt"]
    current_deferred_liabilities = balance_data["Deferred revenues"]
    other_current_liabilities = balance_data["Other current liabilities"]

    long_term_debt = balance_data["Long-term debt"]
    other_liabilities_non_current = balance_data["Other long-term liabilities"]
    other_payables_non_current = total_non_current_liabilities - long_term_debt - other_liabilities_non_current

    return [
            long_term_debt,
            other_payables_non_current,
            other_liabilities_non_current,
            accounts_payables,
            current_debt,
            current_deferred_liabilities,
            other_current_liabilities,
            total_non_current_liabilities,
            total_current_liabilities,
            total_liabilities,
            ]

def get_balance_sheet_equity(ticker: str):
    balance_data = openbb.stocks.fa.balance(ticker)["2022-09-30"]
    return [
        balance_data["Total stockholders' equity"],
        ]

def get_all_data(ticker: str):
    balance_data = openbb.stocks.fa.balance(ticker)["2022-09-30"]
    cash_and_equivalents = balance_data["Cash and cash equivalents"]
    other_shortterm_investments = balance_data["Other short-term investments"]
    cash_and_shortterm_investment = cash_and_equivalents + other_shortterm_investments

    total_current_assets = balance_data["Total current assets"]
    inventory = balance_data["Inventory"]
    other_current_assets = balance_data["Other current assets"]

    receviables = total_current_assets - inventory - other_current_assets - cash_and_equivalents - other_shortterm_investments
    inventory = balance_data["Inventory"]

    other_current_assets = balance_data["Other current assets"]
    current_assets = receviables + cash_and_equivalents + other_shortterm_investments + inventory + other_current_assets
    gross_ppe = balance_data["Net property, plant and equipment"]
    investment_and_advances = balance_data["Equity and other investments"]
    other_non_current_assets = balance_data["Other long-term assets"]

    total_non_current_assets = balance_data["Total non-current assets"]
    total_assets = total_current_assets + total_non_current_assets
    return [
        cash_and_shortterm_investment,
        receviables,
        inventory,
        other_current_assets,
        current_assets,
        gross_ppe,
        investment_and_advances,
        other_non_current_assets,
        total_non_current_assets,
        balance_data["Total stockholders' equity"],
        balance_data["Total liabilities"]
    ]
