# Import Pkg
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Interactive Sales Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
    )

# Read the xlsx file
@st.cache_data           # we can store the datafreame and all the changes in the cache memory
def get_data():
    df = pd.read_excel(r"data\supermarkt_sales.xlsx")
    df["hour"] = pd.to_datetime(df["Time"],format="%H:%M:%S").dt.hour
    return df
#   print(df.head())
df = get_data()


# ---- SideBar------
st.sidebar.header("Filter Here")

city = st.sidebar.multiselect(
    "Select City",
    options=df["City"].unique(),
    default=df["City"].unique()
)
customer_type = st.sidebar.multiselect(
    "Select Customer_type",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)
gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

data_select = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)
st.dataframe(data_select)

# -------Main Page-------
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# Top KPIs
total_sale = int(data_select["Total"].sum())
avg_rating = round(data_select["Rating"].mean(),1)
star_rating = ":star:"*int(round(avg_rating,0))
avd_sales_by_tra = round(data_select["Total"].mean(),2)

left_col,mid_col,right_col = st.columns(3)

with left_col:
    st.subheader("Total_sales")
    st.subheader(f"US ${total_sale:,}")
with mid_col:
    st.subheader("Avarage_Rating")
    st.subheader(f"{avg_rating} {star_rating}")
with right_col:
    st.subheader("Avarage Sales By Transaction")
    st.subheader(f"US ${avd_sales_by_tra}")

st.markdown("---")

# --------try code --------------------
# data_select_2 = data_select[["Product line","Total"]]
# gro = data_select_2.groupby(by=["Product line"]).sum().reset_index()
# gro1 = pd.DataFrame(gro)

# po_fig = px.bar(gro1,x='Total',y='Product line')
# st.plotly_chart(po_fig)
#----------code-----------------------

# Sales by product line [Bar Chart]
sales_by_pro = (
    data_select.groupby(by=['Product line']).sum()[['Total']].sort_values(by='Total')
)

fig_pro_sale = px.bar(
    sales_by_pro,
    x='Total',
    y=sales_by_pro.index,
    orientation='h',
    title="<b>Sales by Probuct Line</b>",
    template="plotly_white",
)

# Sales By Hour [Bar Chart]
data_select_2 = data_select[["hour","Total"]]
gro = data_select_2.groupby(by=["hour"]).sum().reset_index()
gro1 = pd.DataFrame(gro)

po_fig = px.bar(
    gro1,
    y='Total',
    x='hour',
    title="<b>Sales By Hour</b>",
    template="plotly_white",
    )

left_col, right_col = st.columns(2)
with left_col:
    st.plotly_chart(po_fig,use_container_width=True)
with right_col:
    st.plotly_chart(fig_pro_sale,use_container_width=True)
