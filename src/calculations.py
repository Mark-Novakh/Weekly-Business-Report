import pandas as pd


# =========================
# BASIC KPI CALCULATIONS
# =========================

def revenue(sales_df):
    return sales_df["total_amount"].sum()


def total_expenses(expenses_df):
    return expenses_df["amount"].sum()


def ad_spend(ads_df):
    return ads_df["spend"].sum()


def ad_revenue(ads_df):
    return ads_df["revenue"].sum()


def profit(sales_df, expenses_df):
    return revenue(sales_df) - total_expenses(expenses_df)


def roi(sales_df, expenses_df):
    expenses = total_expenses(expenses_df)

    if expenses == 0:
        return 0

    return round((profit(sales_df, expenses_df) / expenses) * 100, 2)


def roas(ads_df):
    spend = ad_spend(ads_df)

    if spend == 0:
        return 0

    return round(ad_revenue(ads_df) / spend, 2)


def margin(sales_df, expenses_df):
    rev = revenue(sales_df)

    if rev == 0:
        return 0

    return round((profit(sales_df, expenses_df) / rev) * 100, 2)


# =========================
# PRODUCT ANALYTICS
# =========================

def revenue_by_product(sales_df):
    return (
        sales_df.groupby("product_name")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )


def quantity_by_product(sales_df):
    return (
        sales_df.groupby("product_name")["quantity"]
        .sum()
        .sort_values(ascending=False)
    )


def revenue_by_category(sales_df):
    return (
        sales_df.groupby("category")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )


# =========================
# REGION ANALYTICS
# =========================

def revenue_by_region(sales_df):
    return (
        sales_df.groupby("region")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )


def orders_by_region(sales_df):
    return (
        sales_df.groupby("region")["order_id"]
        .count()
        .sort_values(ascending=False)
    )


# =========================
# WEEKLY ANALYTICS
# =========================

def weekly_sales(sales_df):
    sales_df = sales_df.copy()

    sales_df["date"] = pd.to_datetime(sales_df["date"])

    sales_df["week"] = sales_df["date"].dt.isocalendar().week

    return (
        sales_df.groupby("week")["total_amount"]
        .sum()
        .sort_index()
    )


def weekly_orders(sales_df):
    sales_df = sales_df.copy()

    sales_df["date"] = pd.to_datetime(sales_df["date"])

    sales_df["week"] = sales_df["date"].dt.isocalendar().week

    return (
        sales_df.groupby("week")["order_id"]
        .count()
        .sort_index()
    )


# =========================
# AD PLATFORM ANALYTICS
# =========================

def platform_performance(ads_df):
    grouped = ads_df.groupby("platform").agg({
        "spend": "sum",
        "revenue": "sum",
        "clicks": "sum",
        "orders": "sum",
        "impressions": "sum"
    })

    grouped["ROAS"] = grouped["revenue"] / grouped["spend"]

    grouped["CTR"] = (
        grouped["clicks"] / grouped["impressions"]
    ) * 100

    grouped["Conversion Rate"] = (
        grouped["orders"] / grouped["clicks"]
    ) * 100

    return grouped.sort_values("ROAS", ascending=False)


# =========================
# MAIN KPI SUMMARY
# =========================

def compute_kpis(sales_df, expenses_df, ads_df):
    return {
        "Revenue": round(revenue(sales_df), 2),

        "Expenses": round(total_expenses(expenses_df), 2),

        "Profit": round(
            profit(sales_df, expenses_df), 2
        ),

        "ROI (%)": roi(sales_df, expenses_df),

        "ROAS": roas(ads_df),

        "Margin (%)": margin(
            sales_df,
            expenses_df
        ),

        "Ad Spend": round(
            ad_spend(ads_df), 2
        ),

        "Ad Revenue": round(
            ad_revenue(ads_df), 2
        )
    }