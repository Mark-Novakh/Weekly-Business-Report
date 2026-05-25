import os
import pandas as pd 
from src.calculations import revenue_by_region
from datetime import datetime 

def generate_report(sales_df, expenses_df, ads_df, kpis):

    os.makedirs("output", exist_ok=True)

    file_name = f"output/report_{datetime.now().date()}.xlsx"

    with pd.ExcelWriter(file_name, engine="xlsxwriter") as writer:
        pd.DataFrame([kpis]).to_excel(writer, sheet_name="KPI", index=False)
        sales_df.to_excel(writer, sheet_name="Raw Sales", index=False)
        from src.calculations import revenue_by_product

        revenue_by_product(sales_df).to_excel(
            writer,
            sheet_name="Top Products"
        )


        revenue_by_region(sales_df).to_excel(
            writer,
            sheet_name="Regions"
        )

        from src.calculations import platform_performance

        platform_performance(ads_df).to_excel(
            writer,
            sheet_name="Ads"
        )

