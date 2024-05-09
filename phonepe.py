import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector 
import pandas as pd
import plotly.express as px
import json
import os
import requests
from PIL import Image


# aggregate transcation

path1 = "C:/Users/madhe/OneDrive/Desktop/Phonepe Project/pulse/data/aggregated/transaction/country/india/state/"
aggregate_transcation_list = os.listdir(path1)

columns1 = {"States":[], "Years":[], "Quarter":[], "Transaction_name":[], "Transaction_count":[] ,"Transaction_amount":[]}

for state in aggregate_transcation_list:
    current_state = path1 + state + "/"
    aggregate_year_list = os.listdir(current_state)

    for year in aggregate_year_list:
        current_year = current_state + year + "/"
        aggregate_file_list = os.listdir(current_year)
        
        for file in aggregate_file_list:
            current_file = current_year + file
            data = open(current_file,"r")
            json_file1 = json.load(data)

            for i in json_file1["data"]["transactionData"]:
                name = i["name"]
                count = i["paymentInstruments"][0]["count"]
                amount = i["paymentInstruments"][0]["amount"]
                columns1["States"].append(state)
                columns1["Years"].append(year)
                columns1["Quarter"].append(int(file.strip(".json")))
                columns1["Transaction_name"].append(name)
                columns1["Transaction_count"].append(count)
                columns1["Transaction_amount"].append(amount)

aggregate_transaction = pd.DataFrame(columns1)
# Replace the details
aggregate_transaction["States"] = aggregate_transaction["States"].str.replace("andaman-&-nicobar-islands", "Andaman & Nicobar")
aggregate_transaction["States"] = aggregate_transaction["States"].str.replace("-", " ")
aggregate_transaction["States"] = aggregate_transaction["States"].str.title()
aggregate_transaction["States"] = aggregate_transaction["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu" )
        


# Aggregate user details
path2 = "C:/Users/madhe/OneDrive/Desktop/Phonepe Project/pulse/data/aggregated/user/country/india/state/"
aggregate_user = os.listdir(path2)

columns2 = {"States":[], "Years":[], "Quarter":[], "Brands":[], "Transaction_count":[] ,"Percentage":[]}

for state in aggregate_transcation_list:
    current_state = path2 + state + "/"
    aggregate_year_list = os.listdir(current_state)

    for year in aggregate_year_list:
        current_year = current_state + year + "/"
        aggregate_file_list = os.listdir(current_year)
        
        for file in aggregate_file_list:
            current_file = current_year + file
            data = open(current_file,"r")
            json_file2 = json.load(data)
            
            try:
                for i in json_file2["data"]["usersByDevice"]:
                    brand = i["brand"]
                    count = i["count"]
                    percentage = i["percentage"]
                    columns2["States"].append(state)
                    columns2["Years"].append(year)
                    columns2["Quarter"].append(int(file.strip(".json")))
                    columns2["Brands"].append(brand)
                    columns2["Transaction_count"].append(count)
                    columns2["Percentage"].append(percentage)

            except:
                pass

aggregate_user = pd.DataFrame(columns2)

aggregate_user["States"] = aggregate_user["States"].str.replace("andaman-&-nicobar-islands", "Andaman & Nicobar")
aggregate_user["States"] = aggregate_user["States"].str.replace("-", " ")
aggregate_user["States"] = aggregate_user["States"].str.title()
aggregate_user["States"] = aggregate_user["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu" )                


# map transaction
path3 = "C:/Users/madhe/OneDrive/Desktop/Phonepe Project/pulse/data/map/transaction/hover/country/india/state/"
map_transaction_list = os.listdir(path3)

columns3 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "Transaction_count":[] ,"Transaction_amount":[]}

for state in map_transaction_list:
    current_state = path3 + state + "/"
    aggregate_year_list = os.listdir(current_state)

    for year in aggregate_year_list:
        current_year = current_state + year + "/"
        aggregate_file_list = os.listdir(current_year)
        
        for file in aggregate_file_list:
            current_file = current_year + file
            data = open(current_file,"r")
            json_file3 = json.load(data)

            for i in json_file3["data"]["hoverDataList"]:
                    name = i["name"]
                    count = i["metric"][0]["count"]
                    amount = i["metric"][0]["amount"]
                    columns3["States"].append(state)
                    columns3["Years"].append(year)
                    columns3["Quarter"].append(int(file.strip(".json")))
                    columns3["Districts"].append(name)
                    columns3["Transaction_count"].append(count)
                    columns3["Transaction_amount"].append(amount)

map_transaction = pd.DataFrame(columns3)

map_transaction["States"] = map_transaction["States"].str.replace("andaman-&-nicobar-islands", "Andaman & Nicobar")
map_transaction["States"] = map_transaction["States"].str.replace("-", " ")
map_transaction["States"] = map_transaction["States"].str.title()
map_transaction["States"] = map_transaction["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu" )                
                    

# map user

path4 = "C:/Users/madhe/OneDrive/Desktop/Phonepe Project/pulse/data/map/user/hover/country/india/state/"
map_user_list = os.listdir(path4)

columns4 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "Registered_users":[] ,"App_opens":[]}

for state in map_user_list:
    current_state = path4 + state + "/"
    aggregate_year_list = os.listdir(current_state)

    for year in aggregate_year_list:
        current_year = current_state + year + "/"
        aggregate_file_list = os.listdir(current_year)
        
        for file in aggregate_file_list:
            current_file = current_year + file
            data = open(current_file,"r")
            json_file4 = json.load(data)

            for i in json_file4["data"]["hoverData"].items():
                district = i[0]
                registeredUsers = i[1]["registeredUsers"]
                appOpens = i[1]["appOpens"]
                columns4["States"].append(state)
                columns4["Years"].append(year)
                columns4["Quarter"].append(int(file.strip(".json")))
                columns4["Districts"].append(district)
                columns4["Registered_users"].append(registeredUsers)
                columns4["App_opens"].append(appOpens)

map_user = pd.DataFrame(columns4)

map_user["States"] = map_user["States"].str.replace("andaman-&-nicobar-islands", "Andaman & Nicobar")
map_user["States"] = map_user["States"].str.replace("-", " ")
map_user["States"] = map_user["States"].str.title()
map_user["States"] = map_user["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu" )                


# top_transaction
path5 = "C:/Users/madhe/OneDrive/Desktop/Phonepe Project/pulse/data/top/transaction/country/india/state/"
top_transaction_list = os.listdir(path5)

columns5 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[] ,"Transaction_amount":[]}

for state in top_transaction_list:
    current_state = path5 + state + "/"
    aggregate_year_list = os.listdir(current_state)

    for year in aggregate_year_list:
        current_year = current_state + year + "/"
        aggregate_file_list = os.listdir(current_year)
        
        for file in aggregate_file_list:
            current_file = current_year + file
            data = open(current_file,"r")
            json_file5 = json.load(data)

            for i in json_file5["data"]["pincodes"]:
                name = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]
                columns5["States"].append(state)
                columns5["Years"].append(year)
                columns5["Quarter"].append(int(file.strip(".json")))
                columns5["Pincodes"].append(name)
                columns5["Transaction_count"].append(count)
                columns5["Transaction_amount"].append(amount)

top_transaction = pd.DataFrame(columns5)

top_transaction["States"] = top_transaction["States"].str.replace("andaman-&-nicobar-islands", "Andaman & Nicobar")
top_transaction["States"] = top_transaction["States"].str.replace("-", " ")
top_transaction["States"] = top_transaction["States"].str.title()
top_transaction["States"] = top_transaction["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu" )                


# top_user
path6 = "C:/Users/madhe/OneDrive/Desktop/Phonepe Project/pulse/data/top/user/country/india/state/"
top_user_list = os.listdir(path6)

columns6 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Registered_users":[]}

for state in top_user_list:
    current_state = path6 + state + "/"
    aggregate_year_list = os.listdir(current_state)

    for year in aggregate_year_list:
        current_year = current_state + year + "/"
        aggregate_file_list = os.listdir(current_year)
        
        for file in aggregate_file_list:
            current_file = current_year + file
            data = open(current_file,"r")
            json_file6 = json.load(data)

            for i in json_file6["data"]["pincodes"]:
                name = i["name"]
                registeredusers = i["registeredUsers"]
                columns6["States"].append(state)
                columns6["Years"].append(year)
                columns6["Quarter"].append(int(file.strip(".json")))
                columns6["Pincodes"].append(name)
                columns6["Registered_users"].append(registeredusers)

top_user = pd.DataFrame(columns6)

top_user["States"] = top_user["States"].str.replace("andaman-&-nicobar-islands", "Andaman & Nicobar")
top_user["States"] = top_user["States"].str.replace("-", " ")
top_user["States"] = top_user["States"].str.title()
top_user["States"] = top_user["States"].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu" )                

                

# connect with sql localhost server
import mysql.connector                  
mydb = mysql.connector.connect(        
 host="localhost",
 user="root",
 password="",
 )

print(mydb)
mycursor = mydb.cursor(buffered=True)


# database create
mycursor.execute("create database if not exists PhonePe_Project")
mydb.commit()

# Table Creation for aggregated transcation
create_aggregated_transcation = """create table if not exists PhonePe_Project.aggregated_transaction(States varchar(250),
                                                                                                    Years int,
                                                                                                    Quarter int,
                                                                                                    Transaction_name varchar(250),
                                                                                                    Transaction_count int,
                                                                                                    Transaction_amount int)"""
mycursor.execute(create_aggregated_transcation)
mydb.commit()

insert_aggregated_transcation = """insert into PhonePe_Project.aggregated_transaction(States,
                                                                                      Years,
                                                                                      Quarter,
                                                                                      Transaction_name,
                                                                                      Transaction_count,
                                                                                      Transaction_amount) values(%s,%s,%s,%s,%s,%s)"""

data = aggregate_transaction.values.tolist()
mycursor.executemany(insert_aggregated_transcation,data)
mydb.commit()


# Table Creation for aggregated user
create_aggregated_user = """create table if not exists PhonePe_Project.aggregated_user(States varchar(250),
                                                                                                    Years int,
                                                                                                    Quarter int,
                                                                                                    Brands varchar(250),
                                                                                                    Transaction_count int,
                                                                                                    Percentage float)"""
mycursor.execute(create_aggregated_user)
mydb.commit()

insert_aggregated_user = """insert into PhonePe_Project.aggregated_user(States,
                                                                        Years,
                                                                        Quarter,
                                                                        Brands,
                                                                        Transaction_count,
                                                                        Percentage) values(%s,%s,%s,%s,%s,%s)"""

data = aggregate_user.values.tolist()
mycursor.executemany(insert_aggregated_user,data)
mydb.commit()


# Table Creation for map transaction 
create_map_transaction = """create table if not exists PhonePe_Project.map_transaction(States varchar(250),
                                                                                        Years int,
                                                                                        Quarter int,
                                                                                        Districts varchar(250),
                                                                                        Transaction_count int,
                                                                                        Transaction_amount int)"""
mycursor.execute(create_map_transaction)
mydb.commit()

insert_map_transaction = """insert into PhonePe_Project.map_transaction(States,
                                                                        Years,
                                                                        Quarter,
                                                                        Districts,
                                                                        Transaction_count,
                                                                        Transaction_amount) values(%s,%s,%s,%s,%s,%s)"""

data = map_transaction.values.tolist()
mycursor.executemany(insert_map_transaction,data)
mydb.commit()
                                 

#Table Creation for map user 
create_map_user = """create table if not exists PhonePe_Project.map_user(States varchar(250),
                                                                        Years int,
                                                                        Quarter int,
                                                                        Districts varchar(250),
                                                                        Registered_users int,
                                                                        App_opens int)"""
mycursor.execute(create_map_user)
mydb.commit()

insert_map_user = """insert into PhonePe_Project.map_user(States,
                                                            Years,
                                                            Quarter,
                                                            Districts,
                                                            Registered_users,
                                                            App_opens) values(%s,%s,%s,%s,%s,%s)"""

data = map_user.values.tolist()
mycursor.executemany(insert_map_user,data)
mydb.commit()


#Table Creation for top transaction
create_top_transaction = """create table if not exists PhonePe_Project.top_transaction(States varchar(250),
                                                                                        Years int,
                                                                                        Quarter int,
                                                                                        Pincodes int,
                                                                                        Transaction_count int,
                                                                                        Transaction_amount int)"""
mycursor.execute(create_top_transaction)
mydb.commit()

insert_top_transaction = """insert into PhonePe_Project.top_transaction(States,
                                                                        Years,
                                                                        Quarter,
                                                                        Pincodes,
                                                                        Transaction_count,
                                                                        Transaction_amount) values(%s,%s,%s,%s,%s,%s)"""

data = top_transaction.values.tolist()
mycursor.executemany(insert_top_transaction,data)
mydb.commit()
                                 

#Table Creation for top user
create_top_user = """create table if not exists PhonePe_Project.top_user(States varchar(250),
                                                                        Years int,
                                                                        Quarter int,
                                                                        Pincodes int,
                                                                        Registered_users int)"""
mycursor.execute(create_top_user)
mydb.commit()

insert_top_user = """insert into PhonePe_Project.top_user(States,
                                                        Years,
                                                        Quarter,
                                                        Pincodes,
                                                        Registered_users)
                                                        values(%s,%s,%s,%s,%s)"""

data = top_user.values.tolist()
mycursor.executemany(insert_top_user,data)
mydb.commit()



# DataFrame Creation for aggregated transcation
mycursor.execute("select * from phonepe_project.aggregated_transaction") 
table1 = mycursor.fetchall()
mydb.commit()
aggregated_transcation_DataFrame = pd.DataFrame(table1, columns= ("States","Years","Quarter","Transaction_name","Transaction_count","Transaction_amount"))

# DataFrame Creation for aggregated user
mycursor.execute("select * from phonepe_project.aggregated_user") 
table2 = mycursor.fetchall()
mydb.commit()
aggregated_user_DataFrame = pd.DataFrame(table2, columns= ("States","Years","Quarter","Brands","Transaction_count","Percentage"))

# DataFrame Creation for map transaction
mycursor.execute("select * from phonepe_project.map_transaction") 
table3 = mycursor.fetchall()
mydb.commit()
map_transaction_DataFrame = pd.DataFrame(table3, columns= ("States","Years","Quarter","Districts","Transaction_count","Transaction_amount"))

# DataFrame Creation for map user
mycursor.execute("select * from phonepe_project.map_user") 
table4 = mycursor.fetchall()
mydb.commit()
map_user_DataFrame = pd.DataFrame(table4, columns= ("States","Years","Quarter","Districts","Registered_users","App_opens"))

# DataFrame Creation for top transaction
mycursor.execute("select * from phonepe_project.top_transaction") 
table5 = mycursor.fetchall()
mydb.commit()
top_transaction_DataFrame = pd.DataFrame(table5, columns= ("States","Years","Quarter","Pincodes","Transaction_count","Transaction_amount"))

# DataFrame Creation for top user
mycursor.execute("select * from phonepe_project.top_user") 
table6 = mycursor.fetchall()
mydb.commit()
top_user_DataFrame = pd.DataFrame(table6, columns= ("States","Years","Quarter","Pincodes","Registered_users"))


#Aggregated_Transaction_year_based
def Transaction_amount_count_year(df,year):
    tnca = df[df["Years"] == year]
    tnca.reset_index(drop = True,inplace=True)

    tncag = tnca.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
    tncag.reset_index(inplace=True)
     #columns sprit 
    col1,col2 = st.columns(2)
    with col1:
        fig_amount = px.bar(tncag, x ="States",y="Transaction_amount", title=f"{year} YEAR TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.Agsunset,height=700,width=650)
        st.plotly_chart(fig_amount)
    with col2:
        fig_count = px.bar(tncag, x ="States",y="Transaction_count", title=f"{year} YEAR TRANSACTION COUNT",
                            color_discrete_sequence=px.colors.sequential.Redor_r,height=700,width=650)
        st.plotly_chart(fig_count)

        #India_Map_Link
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    responce = requests.get(url)
    data1 = json.loads(responce.content)
    states_name = []
    for feature in data1["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort() 
    # columns sprit
    col1,col2 = st.columns(2)
    with col1:
        fig_india_1 = px.choropleth(tncag, geojson=data1, locations="States", featureidkey= "properties.ST_NM",
                                    color="Transaction_amount",color_continuous_scale= "Rainbow",
                                    range_color= (tncag["Transaction_amount"].min(),tncag["Transaction_amount"].max()),
                                    hover_name="States",title = f"{year} YEAR TRANSACTION AMOUNT",fitbounds = "locations",
                                    height = 650, width = 650)
        
        fig_india_1.update_geos(visible = False)
        st.plotly_chart(fig_india_1)
    with col2:
        fig_india_2 = px.choropleth(tncag, geojson=data1, locations="States", featureidkey= "properties.ST_NM",
                                    color="Transaction_count",color_continuous_scale= "Rainbow",
                                    range_color= (tncag["Transaction_count"].min(),tncag["Transaction_count"].max()),
                                    hover_name="States",title = f"{year} YEAR TRANSACTION COUNT",fitbounds = "locations",
                                    height = 650, width = 650)
        
        fig_india_2.update_geos(visible = False)
        st.plotly_chart(fig_india_2) 

    return tnca       


#Aggregated_Transaction_quarter_based
def Transaction_amount_count_quarter(df,quarter):
    tnca = df[df["Quarter"] == quarter]
    tnca.reset_index(drop = True,inplace=True)

    tncag = tnca.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
    tncag.reset_index(inplace=True)
    
    col1,col2 = st.columns(2)
    with col1:
        fig_amount = px.bar(tncag, x ="States",y="Transaction_amount", title=f"{tnca["Years"].min()} YEAR {quarter} QUARTER TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.Agsunset,height= 700, width= 650)
        st.plotly_chart(fig_amount)
    with col2:
        fig_count = px.bar(tncag, x ="States",y="Transaction_count", title=f"{tnca["Years"].min()} YEAR {quarter} QUARTER TRANSACTION COUNT",
                            color_discrete_sequence=px.colors.sequential.Redor_r,height= 700,width= 650)
        st.plotly_chart(fig_count)


    #India_Map_Link
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    responce = requests.get(url)
    data1 = json.loads(responce.content)
    states_name = []
    for feature in data1["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort() 
    
    col1,col2 = st.columns(2)
    with col1:
        fig_india_1 = px.choropleth(tncag, geojson=data1, locations="States", featureidkey= "properties.ST_NM",
                                    color="Transaction_amount",color_continuous_scale= "Rainbow",
                                    range_color= (tncag["Transaction_amount"].min(),tncag["Transaction_amount"].max()),
                                    hover_name="States",title = f"{tnca["Years"].min()} YEAR {quarter} QUARTER TRANSACTION AMOUNT",fitbounds = "locations",
                                    height = 650, width = 650)
        
        fig_india_1.update_geos(visible = False)
        st.plotly_chart(fig_india_1)

    with col2:
        fig_india_2 = px.choropleth(tncag, geojson=data1, locations="States", featureidkey= "properties.ST_NM",
                                    color="Transaction_count",color_continuous_scale= "Rainbow",
                                    range_color= (tncag["Transaction_count"].min(),tncag["Transaction_count"].max()),
                                    hover_name="States",title = f"{tnca["Years"].min()} YEAR {quarter} QUARTER TRANSACTION COUNT",fitbounds = "locations",
                                    height = 650, width = 650)
        
        fig_india_2.update_geos(visible = False)
        st.plotly_chart(fig_india_2)
    return tnca


#Aggregated_Transaction_name_based
def aggre_tran_name(df,state):

    tnca = df[df["States"] == state]
    tnca.reset_index(drop = True,inplace=True)

    tncag = tnca.groupby("Transaction_name")[["Transaction_count","Transaction_amount"]].sum()
    tncag.reset_index(inplace=True)
    
    col1,col2 = st.columns(2)
    with col1:
        fig_pie_chart1 = px.pie(data_frame=tncag, names="Transaction_name", values= "Transaction_amount",  
                                width= 600, title=f"{state.upper()} TRANSACTION AMOUNT", hole= 0.5)
        st.plotly_chart(fig_pie_chart1)
    with col2:
        fig_pie_chart2 = px.pie(data_frame=tncag, names="Transaction_name", values= "Transaction_count",  
                                width= 600, title=f"{state.upper()} TRANSACTION COUNT", hole= 0.5)
        st.plotly_chart(fig_pie_chart2)


# Aggregated_user_Analysis_Year
def aggregated_user(df,year):
    aggregated_user_year =df[df["Years"] == year]
    aggregated_user_year.reset_index(drop= True , inplace=True)
    aggregated_user_year_group =pd.DataFrame(aggregated_user_year.groupby("Brands")["Transaction_count"].sum())
    aggregated_user_year_group.reset_index(inplace=True)


    fig_bar_auy = px.bar(aggregated_user_year_group, x ="Brands", y = "Transaction_count" , title=f"{year} BRANDS AND TRANSACTION COUNT", 
                        width= 900,color_discrete_sequence=px.colors.sequential.Rainbow,hover_name="Brands") 
    st.plotly_chart(fig_bar_auy)                    
                    
    return aggregated_user_year  


# Aggregated_user_Analysis_year_quarter
def Aggre_user_YandQ(df,quarter):
    aggregated_user_year_quarter =df[df["Quarter"] == quarter]
    aggregated_user_year_quarter.reset_index(drop= True , inplace=True)
    aggregated_user_year_quarter_g =aggregated_user_year_quarter.groupby("Brands")["Transaction_count"].sum()
    aggregated_user_year_quarter_g_df = pd.DataFrame(aggregated_user_year_quarter_g)
    aggregated_user_year_quarter_g_df.reset_index(inplace=True)


    fig_bar_auyq = px.bar(aggregated_user_year_quarter_g_df, x ="Brands", y = "Transaction_count" , title=f"{aggregated_user_year_quarter["Years"].min()} YEAR {quarter} QUARTER BRANDS AND TRANSACTION COUNT", 
                        width= 900,color_discrete_sequence=px.colors.sequential.RdBu_r, hover_name= "Brands") 
    st.plotly_chart(fig_bar_auyq) 

    return aggregated_user_year_quarter


# Aggregated_user_Analysis_year_quarter_state
def Aggre_user_Year_quarter_state(df,state):
    Aggregated_user_year_quarter_state = df[df["States"] == state]
    Aggregated_user_year_quarter_state.reset_index(drop=True,inplace=True)

    fig_line_au = px.line(Aggregated_user_year_quarter_state, x = "Brands" , y ="Transaction_count", hover_data= "Percentage",
                            title=f"{state.upper()} - BRANDS, TRANSACTION COUNT, PERCENTAGE", width=950, markers=True, 
                            hover_name="Brands", color_discrete_sequence=px.colors.sequential.Magenta_r,
                            line_shape="linear"
                            )
    st.plotly_chart(fig_line_au)


# Map_transaction_districts
def map_transaction_districts(df,state):

    mtcad = df[df["States"] == state]
    mtcad.reset_index(drop = True,inplace=True)

    mtcad = mtcad.groupby("Districts")[["Transaction_count","Transaction_amount"]].sum()
    mtcad.reset_index(inplace=True)

    col1, col2 = st.columns(2)
    with col1:
        fig_bar_chart1 = px.bar(data_frame=mtcad, x = "Transaction_amount", y = "Districts",orientation="h",
                                title= f"{state.upper()} DISTRICTS AND TRANSACTION AMOUNT",height=600,
                                color_discrete_sequence= px.colors.sequential.Greens_r)
        st.plotly_chart(fig_bar_chart1)

    with col2:
        fig_bar_chart2 = px.bar(data_frame=mtcad, x = "Transaction_count", y = "Districts",orientation="h",
                                title= f"{state.upper()} DISTRICTS AND TRANSACTION COUNT",height=600,
                                color_discrete_sequence= px.colors.sequential.RdBu_r)
        st.plotly_chart(fig_bar_chart2)  


# map_user_year_Registered_users_and_App_opens year_Analysis
def map_user_YRA(df,year):
    map_user_year =df[df["Years"] == year]
    map_user_year.reset_index(drop= True , inplace=True)

    map_user_year_group =map_user_year.groupby("States")[["Registered_users","App_opens"]].sum()
    map_user_year_group.reset_index(inplace=True)

    fig_line_map_user = px.line(map_user_year_group, x = "States" , y =["Registered_users","App_opens"],
                        title=f"{year} YEAR REGISTERED USER AND APP OPENS", width=950,height=800, markers=True, 
                        hover_name="States", color_discrete_sequence=px.colors.sequential.Bluered_r)
    st.plotly_chart(fig_line_map_user)

    return map_user_year


# map user year and quarter Registered_users and App_opens quarter_Analysis
def map_user_YQRA(df,quarter):
    map_user_year_quarter =df[df["Quarter"] == quarter]
    map_user_year_quarter.reset_index(drop= True , inplace=True)

    map_user_year_quarter_group =map_user_year_quarter.groupby("States")[["Registered_users","App_opens"]].sum()
    map_user_year_quarter_group.reset_index(inplace=True)

    fig_line_map_user = px.line(map_user_year_quarter_group, x = "States" , y =["Registered_users","App_opens"],
                        title=f"{map_user_year_quarter["Years"].min()} YEAR {quarter} QUARTER REGISTERED USER AND APP OPENS", width=950,height=800, markers=True, 
                        hover_name="States", color_discrete_sequence=px.colors.sequential.Rainbow_r)
    st.plotly_chart(fig_line_map_user)

    return map_user_year_quarter


# map_user_year_quarter_Registered_users and App_opens State_Analysis
def map_user_YQSRA(df, state):
    map_user_year_quarter_state =df[df["States"] == state]
    map_user_year_quarter_state.reset_index(drop= True , inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        fig_chart_user_bar1 = px.bar(map_user_year_quarter_state, x ="Registered_users" , y ="Districts", orientation="h",
                                    title=f"{state.upper()} REGISTERED USER", height= 800,color_discrete_sequence=px.colors.sequential.Greens_r )

        st.plotly_chart(fig_chart_user_bar1)
    with col2:
        fig_chart_user_bar2 = px.bar(map_user_year_quarter_state, x ="App_opens" , y ="Districts", orientation="h",
                                    title=f"{state.upper()} APP OPENS", height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r )

        st.plotly_chart(fig_chart_user_bar2)


# top_transaction_amount_count_pincode_state_Analysis
def top_transaction_acpq(df,state):
    top_transaction_year_state_Analysis =df[df["States"] == state]
    top_transaction_year_state_Analysis.reset_index(drop= True , inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        fig_top_transaction_user_bar1 = px.line(top_transaction_year_state_Analysis, x ="Quarter" , y ="Transaction_amount",
                                                hover_data="Pincodes",title=f"{state.upper()} STATE - QUARTER, TRANSACTION AMOUNT, PINCODE" ,width=650, height= 650,
                                                color_discrete_sequence=px.colors.sequential.YlGnBu_r,markers=True,line_shape="linear" )

        st.plotly_chart(fig_top_transaction_user_bar1)
    with col2:
        fig_top_transaction_user_bar2 = px.line(top_transaction_year_state_Analysis, x ="Quarter" , y ="Transaction_count",
                                                hover_data="Pincodes",title=f"{state.upper()} STATE - QUARTER, TRANSACTION COUNT, PINCODE",width=650, height= 650,
                                                color_discrete_sequence=px.colors.sequential.Bluered,markers=True,line_shape="linear" )

        st.plotly_chart(fig_top_transaction_user_bar2)


# top user year state quarter Registered users Analysis
def top_user_ysqr(df,year):
    top_user_year =df[df["Years"] == year]
    top_user_year.reset_index(drop= True , inplace=True)

    top_user_year_group =pd.DataFrame(top_user_year.groupby(["States","Quarter"])["Registered_users"].sum())
    top_user_year_group.reset_index(inplace=True)

    fig_top_user_1 = px.bar(top_user_year_group, x ="States" , y= "Registered_users",hover_name="States",color="Quarter",
                            title= f"{year} YEAR REGISTERED USERS" ,width= 950,height=800, color_discrete_sequence=px.colors.sequential.Rainbow) 
    st.plotly_chart(fig_top_user_1)

    return top_user_year


# top user state quarter pincode Registered users Analysis
def top_user_sqpr(df,state):
    top_user_year_state = df[df["States"] == state]
    top_user_year_state.reset_index(drop= True , inplace=True)

    fig_top_user_2= px.bar(top_user_year_state, x ="Quarter", y= "Registered_users",width=1000,height=850,
                            title= "QUARTER, PINCODES, REGISTERED_USERS", color="Registered_users",hover_data="Pincodes",
                            hover_name= "States", color_continuous_scale=px.colors.sequential.Rainbow )

    st.plotly_chart(fig_top_user_2)



# fig_chart_transcation_amount

def fig_chart_transcation_amount(table_name):

    # Top 10 Transaction_amount
    query1 = f"""SELECT States,SUM(Transaction_amount) As Transaction_amount
                FROM phonepe_project.{table_name}
                GROUP BY States
                ORDER BY Transaction_amount DESC
                LIMIT 10;"""

    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()

    df_1 = pd.DataFrame(table1,columns= ("States","Transaction_amount"))
     
    col1,col2 = st.columns(2)
    with col1:
        fig_amount_1 = px.bar(df_1, x ="States",y="Transaction_amount", title= "TOP 10 OF TRANSACTION AMOUNT",hover_name="States",
                            color_discrete_sequence=px.colors.sequential.Agsunset,height= 600, width= 550)
        
        st.plotly_chart(fig_amount_1)
    
    # Last 10 Transaction_amount
    query2 = f"""SELECT States,SUM(Transaction_amount) As Transaction_amount
                FROM phonepe_project.{table_name}
                GROUP BY States
                ORDER BY Transaction_amount
                LIMIT 10;"""

    mycursor.execute(query2)
    table2 = mycursor.fetchall()
    mydb.commit()

    df_2 = pd.DataFrame(table2,columns= ("States","Transaction_amount"))

    with col2:
        fig_amount_2 = px.bar(df_2, x ="States",y="Transaction_amount", title= "LAST 10 OF TRANSACTION AMOUNT",hover_name="States",
                            color_discrete_sequence=px.colors.sequential.Agsunset_r, height= 600, width= 550)
        st.plotly_chart(fig_amount_2)


    # AVG of Transaction_amount
    query3 = f"""SELECT States,AVG(Transaction_amount) As Transaction_amount
                FROM phonepe_project.{table_name}
                GROUP BY States
                ORDER BY Transaction_amount ;"""
                

    mycursor.execute(query3)
    table3 = mycursor.fetchall()
    mydb.commit()

    df_3 = pd.DataFrame(table3,columns= ("States","Transaction_amount"))


    fig_amount_3 = px.bar(df_3, x ="Transaction_amount",y="States", title= "AVERAGE OF TRANSACTION AMOUNT",hover_name="States",orientation="h",
                        color_discrete_sequence=px.colors.sequential.Blugrn_r, height= 800, width= 900)
    st.plotly_chart(fig_amount_3)



# fig_chart_transcation_count
def fig_chart_transcation_count(table_name):

    # Top 10 Transaction_count
    query1 = f"""SELECT States,SUM(Transaction_count) As Transaction_count
                FROM phonepe_project.{table_name}
                GROUP BY States
                ORDER BY Transaction_count DESC
                LIMIT 10;"""

    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()

    df_1 = pd.DataFrame(table1,columns= ("States","Transaction_count"))

    col1,col2 = st.columns(2)
    with col1:
        fig_amount_1 = px.bar(df_1, x ="States",y="Transaction_count", title= "TOP 10 OF TRANSACTION COUNT",hover_name="States",
                            color_discrete_sequence=px.colors.sequential.Agsunset,height= 600, width= 550)
        st.plotly_chart(fig_amount_1)


    # Last 10 Transaction_count
    query2 = f"""SELECT States,SUM(Transaction_count) As Transaction_count
                FROM phonepe_project.{table_name}
                GROUP BY States
                ORDER BY Transaction_count
                LIMIT 10;"""

    mycursor.execute(query2)
    table2 = mycursor.fetchall()
    mydb.commit()

    df_2 = pd.DataFrame(table2,columns= ("States","Transaction_count"))

    with col2:
        fig_amount_2 = px.bar(df_2, x ="States",y="Transaction_count", title= "LAST 10 OF TRANSACTION COUNT",hover_name="States",
                            color_discrete_sequence=px.colors.sequential.Agsunset_r, height= 600, width= 550)
        st.plotly_chart(fig_amount_2)


    # AVG of Transaction_count
    query3 = f"""SELECT States,AVG(Transaction_count) As Transaction_count
                FROM phonepe_project.{table_name}
                GROUP BY States
                ORDER BY Transaction_count ;"""
                

    mycursor.execute(query3)
    table3 = mycursor.fetchall()
    mydb.commit()

    df_3 = pd.DataFrame(table3,columns= ("States","Transaction_count"))


    fig_amount_3 = px.bar(df_3, x ="Transaction_count",y="States", title= "AVERAGE OF TRANSACTION COUNT",hover_name="States",orientation="h",
                        color_discrete_sequence=px.colors.sequential.Blugrn_r, height= 800, width= 900)
    st.plotly_chart(fig_amount_3)



# fig_chart_map_user_in_Registered_users
def fig_chart_Registered_users(table_name,state):

    # Top 10 Registered_users
    query1 = f"""SELECT Districts,SUM(Registered_users) AS Registered_users
                FROM phonepe_project.{table_name} 
                where States = "{state}"
                GROUP BY Districts
                ORDER BY Registered_users DESC
                LIMIT 10;"""

    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()

    df_1 = pd.DataFrame(table1,columns= ("Districts","Registered_users"))

    col1,col2 = st.columns(2)

    with col1:
        fig_amount_1 = px.bar(df_1, x ="Districts",y="Registered_users", title= "TOP 10 OF REGISTERED USER",hover_name="Districts",
                            color_discrete_sequence=px.colors.sequential.Agsunset,height= 600, width= 550)
        st.plotly_chart(fig_amount_1)


    # Last 10 Registered_users
    query2 = f"""SELECT Districts,SUM(Registered_users) AS Registered_users
                FROM phonepe_project.{table_name} 
                where States = "{state}"
                GROUP BY Districts
                ORDER BY Registered_users
                LIMIT 10;"""

    mycursor.execute(query2)
    table2 = mycursor.fetchall()
    mydb.commit()

    df_2 = pd.DataFrame(table2,columns= ("Districts","Registered_users"))

    with col2:
        fig_amount_2 = px.bar(df_2, x ="Districts",y="Registered_users", title= "LAST 10 OF REGISTERED USER",hover_name="Districts",
                            color_discrete_sequence=px.colors.sequential.Agsunset_r, height= 600, width= 550)
        st.plotly_chart(fig_amount_2)

    # AVG of Registered_users
    query3 = f"""SELECT Districts,AVG(Registered_users) AS Registered_users
                FROM phonepe_project.{table_name}
                where States ="{state}"
                GROUP BY Districts
                ORDER BY Registered_users;"""
                

    mycursor.execute(query3)
    table3 = mycursor.fetchall()
    mydb.commit()

    df_3 = pd.DataFrame(table3,columns= ("Districts","Registered_users"))


    fig_amount_3 = px.bar(df_3, x ="Registered_users",y="Districts", title= "AVERAGE OF REGISTERED USER",hover_name="Districts",orientation="h",
                        color_discrete_sequence=px.colors.sequential.Blugrn_r, height= 800, width= 900)
    st.plotly_chart(fig_amount_3)




# fig_chart_map_user_in_App_opens
def fig_chart_App_opens(table_name,state):

    # Top 10 App_opens
    query1 = f"""SELECT Districts,SUM(App_opens) AS App_opens
                FROM phonepe_project.{table_name} 
                where States = "{state}"
                GROUP BY Districts
                ORDER BY App_opens DESC
                LIMIT 10;"""

    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()

    df_1 = pd.DataFrame(table1,columns= ("Districts","App_opens"))

    col1,col2 = st.columns(2)
    with col1:
        fig_amount_1 = px.bar(df_1, x ="Districts",y="App_opens", title= "TOP 10 OF APP OPENS",hover_name="Districts",
                            color_discrete_sequence=px.colors.sequential.Agsunset,height= 600, width= 550)
        st.plotly_chart(fig_amount_1)


    # Last 10 App_opens
    query2 = f"""SELECT Districts,SUM(App_opens) AS App_opens
                FROM phonepe_project.{table_name} 
                where States = "{state}"
                GROUP BY Districts
                ORDER BY App_opens
                LIMIT 10;"""

    mycursor.execute(query2)
    table2 = mycursor.fetchall()
    mydb.commit()

    df_2 = pd.DataFrame(table2,columns= ("Districts","App_opens"))

    with col2:
        fig_amount_2 = px.bar(df_2, x ="Districts",y="App_opens", title= "LAST 10 OF APP OPENS",hover_name="Districts",
                            color_discrete_sequence=px.colors.sequential.Agsunset_r, height= 600, width= 550)
        st.plotly_chart(fig_amount_2)


    # AVG of App_opens
    query3 = f"""SELECT Districts,AVG(App_opens) AS App_opens
                FROM phonepe_project.{table_name}
                where States ="{state}"
                GROUP BY Districts
                ORDER BY App_opens;"""
                

    mycursor.execute(query3)
    table3 = mycursor.fetchall()
    mydb.commit()

    df_3 = pd.DataFrame(table3,columns= ("Districts","App_opens"))


    fig_amount_3 = px.bar(df_3, x ="App_opens",y="Districts", title= "AVERAGE OF APP OPENS",hover_name="Districts",orientation="h",
                        color_discrete_sequence=px.colors.sequential.Blugrn_r, height= 800, width= 900)
    st.plotly_chart(fig_amount_3)    



# fig_chart_top_user_in_Registered_users
def fig_chart_topuser_Registered_users(table_name):

    # Top 10 Registered_users
    query1 = f"""SELECT states,SUM(registered_users) AS Registered_users
                FROM phonepe_project.{table_name}
                GROUP BY States
                ORDER BY Registered_users DESC
                LIMIT 10;"""

    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()

    df_1 = pd.DataFrame(table1,columns= ("States","Registered_users"))

    col1,col2 = st.columns(2)
    with col1:
        fig_amount_1 = px.bar(df_1, x ="States",y="Registered_users", title= "TOP 10 OF REGISTERED USERS",hover_name="States",
                            color_discrete_sequence=px.colors.sequential.Agsunset,height= 600, width= 550)
        st.plotly_chart(fig_amount_1)


    # Last 10 Registered_users
    query2 = f"""SELECT states,SUM(registered_users) AS Registered_users
                FROM phonepe_project.{table_name}
                GROUP BY States
                ORDER BY Registered_users 
                LIMIT 10;"""

    mycursor.execute(query2)
    table2 = mycursor.fetchall()
    mydb.commit()

    df_2 = pd.DataFrame(table2,columns= ("States","Registered_users"))

    with col2:
        fig_amount_2 = px.bar(df_2, x ="States",y="Registered_users", title= "LAST 10 OF REGISTERED USER",hover_name="States",
                            color_discrete_sequence=px.colors.sequential.Agsunset_r, height= 600, width= 550)
        st.plotly_chart(fig_amount_2)


    # AVG of Registered_users
    query3 = f"""SELECT states,AVG(registered_users) AS Registered_users
                FROM phonepe_project.{table_name}
                GROUP BY States
                ORDER BY Registered_users;"""
                

    mycursor.execute(query3)
    table3 = mycursor.fetchall()
    mydb.commit()

    df_3 = pd.DataFrame(table3,columns= ("States","Registered_users"))


    fig_amount_3 = px.bar(df_3, x ="Registered_users",y="States", title= "AVERAGE OF REGISTERED USER",hover_name="States",orientation="h",
                        color_discrete_sequence=px.colors.sequential.Blugrn_r, height= 800, width= 900)
    st.plotly_chart(fig_amount_3)


# fig_chart_transcation_name_in_aggregated_transaction
def fig_chart_transcation_name_amount_count(table_name):

    # transaction name of total transaction amount
    query1 = f"""SELECT Transaction_name,SUM(Transaction_amount) AS Transaction_amount
                FROM phonepe_project.{table_name}
                GROUP BY Transaction_name
                ORDER BY Transaction_amount DESC;"""

    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()

    df_1 = pd.DataFrame(table1,columns= ("Transaction_name","Transaction_amount"))

    col1,col2 = st.columns(2)
    with col1:
        fig_amount_1 = px.bar(df_1, x ="Transaction_amount",y="Transaction_name", title= "TRANSACTION NAME IN TOTAL TRANSACTION AMOUNT",hover_name="Transaction_name",orientation="h",
                            color_discrete_sequence=px.colors.sequential.Agsunset,height= 600, width= 550)
        st.plotly_chart(fig_amount_1)

    
    # transaction name of total transaction count
    query1 = f"""SELECT Transaction_name,SUM(Transaction_count) AS Transaction_count
                FROM phonepe_project.{table_name}
                GROUP BY Transaction_name
                ORDER BY Transaction_count DESC;"""

    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()

    df_1 = pd.DataFrame(table1,columns= ("Transaction_name","Transaction_count"))

    with col2:
        fig_amount_1 = px.bar(df_1, x ="Transaction_count",y="Transaction_name", title= "TRANSACTION NAME IN TOTAL TRANSACTION COUNT",hover_name="Transaction_name",orientation="h",
                            color_discrete_sequence=px.colors.sequential.Agsunset,height= 600, width= 550)
        st.plotly_chart(fig_amount_1)



# fig_chart_Brands_in_total_transaction_count
def fig_chart_Brands_in_total_transaction_count(table_name):

    # Top 10 BRANDS in Transaction count
    query1 = f"""SELECT Brands,SUM(Transaction_count) AS Transaction_count
                FROM phonepe_project.{table_name}
                GROUP BY Brands
                ORDER BY Transaction_count DESC
                LIMIT 10;"""

    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()

    df_1 = pd.DataFrame(table1,columns= ("Brands","Transaction_count"))

    col1,col2 = st.columns(2)
    with col1:
        fig_amount_1 = px.bar(df_1, x ="Brands",y="Transaction_count", title= "TOP 10 BRANDS IN TRANSACTION COUNT",hover_name="Brands",
                            color_discrete_sequence=px.colors.sequential.Agsunset,height= 600, width= 550)
        st.plotly_chart(fig_amount_1)

    # Last 10 BRANDS in Transaction count
    query2 = f"""SELECT Brands,SUM(Transaction_count) AS Transaction_count
                FROM phonepe_project.{table_name}
                GROUP BY Brands
                ORDER BY Transaction_count
                LIMIT 10;"""

    mycursor.execute(query2)
    table2 = mycursor.fetchall()
    mydb.commit()

    df_2 = pd.DataFrame(table2,columns= ("Brands","Transaction_count"))

    with col2:
        fig_amount_2 = px.bar(df_2, x ="Brands",y="Transaction_count", title= "LAST 10 BRANDS IN TRANSACTION COUNT",hover_name="Brands",
                            color_discrete_sequence=px.colors.sequential.Agsunset_r, height= 600, width= 550)
        st.plotly_chart(fig_amount_2)


    # AVG of BRANDS in Transaction count
    query3 = f"""SELECT Brands,AVG(Transaction_count) AS Transaction_count
                FROM phonepe_project.{table_name}
                GROUP BY Brands
                ORDER BY Transaction_count"""
                

    mycursor.execute(query3)
    table3 = mycursor.fetchall()
    mydb.commit()

    df_3 = pd.DataFrame(table3,columns= ("Brands","Transaction_count"))


    fig_amount_3 = px.bar(df_3, x ="Transaction_count",y="Brands", title= "AVERAGE OF BRANDS IN TRANSACTION COUNT",hover_name="Brands",orientation="h",
                        color_discrete_sequence=px.colors.sequential.Blugrn_r, height= 800, width= 900)
    st.plotly_chart(fig_amount_3)



# fig_chart_Brands_in_total_Percentage
def fig_chart_Brands_in_total_Percentage(table_name):

    # Top 10 BRANDS in Percentage
    query1 = f"""SELECT Brands,SUM(Percentage) AS Percentage
                FROM phonepe_project.{table_name}
                GROUP BY Brands
                ORDER BY Percentage DESC
                LIMIT 10;"""

    mycursor.execute(query1)
    table1 = mycursor.fetchall()
    mydb.commit()

    df_1 = pd.DataFrame(table1,columns= ("Brands","Percentage"))

    col1,col2 = st.columns(2)
    with col1:
        fig_amount_1 = px.bar(df_1, x ="Brands",y="Percentage", title= "TOP 10 BRANDS IN PERCENTAGE",hover_name="Brands",
                            color_discrete_sequence=px.colors.sequential.Agsunset,height= 600, width= 550)
        st.plotly_chart(fig_amount_1)


    # Last 10 BRANDS in Percentage
    query2 = f"""SELECT Brands,SUM(Percentage) AS Percentage
                FROM phonepe_project.{table_name}
                GROUP BY Brands
                ORDER BY Percentage
                LIMIT 10;"""

    mycursor.execute(query2)
    table2 = mycursor.fetchall()
    mydb.commit()

    df_2 = pd.DataFrame(table2,columns= ("Brands","Percentage"))

    with col2:
        fig_amount_2 = px.bar(df_2, x ="Brands",y="Percentage", title= "LAST 10 BRANDS IN PERCENTAGE",hover_name="Brands",
                            color_discrete_sequence=px.colors.sequential.Agsunset_r, height= 600, width= 550)
        st.plotly_chart(fig_amount_2)


    # AVG of BRANDS in Percentage
    query3 = f"""SELECT Brands,AVG(Percentage) AS Percentage
                FROM phonepe_project.{table_name}
                GROUP BY Brands
                ORDER BY Percentage"""
                

    mycursor.execute(query3)
    table3 = mycursor.fetchall()
    mydb.commit()

    df_3 = pd.DataFrame(table3,columns= ("Brands","Percentage"))


    fig_amount_3 = px.bar(df_3, x ="Percentage",y="Brands", title= "AVERAGE OF BRANDS IN PERCENTAGE",hover_name="Brands",orientation="h",
                        color_discrete_sequence=px.colors.sequential.Blugrn_r, height= 800, width= 900)
    st.plotly_chart(fig_amount_3)



# Streamlit Details
st.set_page_config(layout="wide")
st.title(":red[PHONEPE DATA VISUALIZATION AND EXPLORATION]")

st.header("Introduction")
st.write("""PhonePe allows users to make payments for a wide range of services, including mobile recharges, utility bill payments, DTH recharges, and more. Users can also pay for goods and services at online and offline merchants through the app using QR code scanning or through PhonePe's payment gateway.
         Through PhonePe's user-friendly interface and integration with the Unified Payments Interface (UPI), the project seeks to extend banking and payment services to underserved populations, including rural communities and those without traditional bank accounts.""")


st.header("Technologies Used")
st.write("1) Python - The project is implemented using the Python programming language.")
st.write("2) GitHub - Phonepe data details collected in GitHub Phonepe pulse account.")
st.write("3) Plotly - Plotly is a powerful Python library used for creating interactive data visualizations.")
st.write("4) Pandas - A Powerfull data manipulation in pandas. providing functionalities such as data filtering, dataframe create, transformation, and aggregation.")
st.write("5) MySQL - A Powerfull Open Source Relational database management system used to store and manage the retrieved data.")
st.write("6) Streamlit - The user interface and visualization are created using the Streamlit framework.")
st.write("7) OS Module - The OS Module in Python provides a way to interact with the operating system.")
st.write("8) JSON(JavaScript Object Notation) -The json module in Python provides functions for Reading and Writing JSON data.")


with st.sidebar:
    
    select = option_menu("PHONEPE DATA", ["DATA VISUALIZATION AND EXPLORATION", "CREATED 10 QUESTIONS AND ANSWERD IN CHARTS"])

if select == "DATA VISUALIZATION AND EXPLORATION":
    st.header("DATA VISUALIZATION AND EXPLORATION")
    tab1, tab2, tab3 = st.tabs(["Aggregated Data Analysis", "Map Data Analysis", "Top Data Analysis"])

    with tab1:
        
        method1 = st.radio("Select The Method",["Aggregated Transaction","Aggregated User"])
        
        if method1 == "Aggregated Transaction":
            # columns sprit
            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("Select The Year",aggregated_transcation_DataFrame["Years"].min(),aggregated_transcation_DataFrame["Years"].max(),aggregated_transcation_DataFrame["Years"].min())
            agg_tran_nac_y = Transaction_amount_count_year(aggregated_transcation_DataFrame, years)

            col1,col2 = st.columns(2)
            with col1:
                states = st.selectbox("Select The State", agg_tran_nac_y["States"].unique())

            aggre_tran_name(agg_tran_nac_y,states)

            col1,col2 = st.columns(2)
            with col1:    
                 quarters = st.slider("Select The Quarter",agg_tran_nac_y["Quarter"].min(),agg_tran_nac_y["Quarter"].max(),agg_tran_nac_y["Quarter"].min())
            agg_tran_nac_q = Transaction_amount_count_quarter(agg_tran_nac_y, quarters)
            
            col1,col2 = st.columns(2)
            with col1:
                states = st.selectbox("Select The State_", agg_tran_nac_q["States"].unique())

            aggre_tran_name(agg_tran_nac_q,states)



        elif method1 == "Aggregated User":
            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("Select The Year",aggregated_user_DataFrame["Years"].min(),aggregated_user_DataFrame["Years"].max(),aggregated_user_DataFrame["Years"].min())
            Aggregated_user_year = aggregated_user(aggregated_user_DataFrame, years)
    
            col1,col2 = st.columns(2)
            with col1:    
                 quarters = st.slider("Select The Quarter",Aggregated_user_year["Quarter"].min(),Aggregated_user_year["Quarter"].max(),Aggregated_user_year["Quarter"].min())
            Aggregated_user_year_quarter = Aggre_user_YandQ(Aggregated_user_year, quarters)
            
            col1,col2 = st.columns(2)
            with col1:
                states = st.selectbox("Select The State", Aggregated_user_year_quarter["States"].unique())

            Aggre_user_Year_quarter_state(Aggregated_user_year_quarter,states)



    with tab2:
        method2 = st.radio("Select The Method",["Map Transaction","Map User"])
        if method2 == "Map Transaction":

            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("Select The Year Map Transaction",map_transaction_DataFrame["Years"].min(),map_transaction_DataFrame["Years"].max(),map_transaction_DataFrame["Years"].min())
            map_transaction_year = Transaction_amount_count_year(map_transaction_DataFrame, years)

            col1,col2 = st.columns(2)
            with col1:    
                 quarters = st.slider("Select The Quarter Map Transaction",map_transaction_year["Quarter"].min(),map_transaction_year["Quarter"].max(),map_transaction_year["Quarter"].min())
            map_tran_ac_y_q = Transaction_amount_count_quarter(map_transaction_year, quarters)

            col1,col2 = st.columns(2)
            with col1:
                district = st.selectbox("Select The State Map Transaction ", map_transaction_year["States"].unique())
            map_transaction_districts(map_transaction_year,district)

            col1,col2 = st.columns(2)
            with col1:
                states = st.selectbox("Select The State quarter Analysis ", map_tran_ac_y_q["States"].unique())
            map_transaction_districts(map_tran_ac_y_q,states)

     

        elif method2 == "Map User":

            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("Select The Year Map User",map_user_DataFrame["Years"].min(),map_user_DataFrame["Years"].max(),map_user_DataFrame["Years"].min())
            map_user_year = map_user_YRA(map_user_DataFrame, years)

            col1,col2 = st.columns(2)
            with col1:    
                 quarters = st.slider("Select The Quarter Map User",map_user_year["Quarter"].min(),map_user_year["Quarter"].max(),map_user_year["Quarter"].min())
            map_user_year_quarter = map_user_YQRA(map_user_year,quarters)

            col1,col2 = st.columns(2)
            with col1:
                states = st.selectbox("Select The State Map User ", map_user_year_quarter["States"].unique())
            map_user_YQSRA(map_user_year_quarter, states)
            


    with tab3:

        method3 = st.radio("Select The Method",["Top Transaction","Top User"])

        if method3 == "Top Transaction":
            
            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("Select The Year Top Transaction",top_transaction_DataFrame["Years"].min(),top_transaction_DataFrame["Years"].max(),top_transaction_DataFrame["Years"].min())
            top_transaction_year_amount_count = Transaction_amount_count_year(top_transaction_DataFrame, years)
            
            col1,col2 = st.columns(2)
            with col1:    
                 quarters = st.slider("Select The Quarter Top Transaction",top_transaction_year_amount_count["Quarter"].min(),top_transaction_year_amount_count["Quarter"].max(),top_transaction_year_amount_count["Quarter"].min())
            top_transaction_year_quarter = Transaction_amount_count_quarter(top_transaction_year_amount_count,quarters)

            col1,col2 = st.columns(2)
            with col1:
                states = st.selectbox("Select The State Top Transaction", top_transaction_year_amount_count["States"].unique())
            top_transaction_acpq(top_transaction_year_amount_count,states)
 

        elif method3 == "Top User":

            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("Select The Year Top user",top_user_DataFrame["Years"].min(),top_user_DataFrame["Years"].max(),top_user_DataFrame["Years"].min())
            top_user_year = top_user_ysqr(top_user_DataFrame, years)
            

            col1,col2 = st.columns(2)
            with col1:
                states = st.selectbox("Select The State Top user", top_user_year["States"].unique())
            top_user_sqpr(top_user_year,states)
 

elif select == "CREATED 10 QUESTIONS AND ANSWERD IN CHARTS":

    st.header("CREATED 10 QUESTIONS AND ANSWERD IN CHARTS")
    question = st.selectbox("Select the Question",["1.Transaction name of total Transaction_amount and transaction count in Aggregated Transaction",
                                                   "2.Brands of Transaction count in Aggregated User",
                                                   "3.Brands of Percentage in Aggregated User",
                                                   "4.Transaction Count of Aggregated User",
                                                   "5.Registered Users of Map User",
                                                   "6.App opens of Map User",
                                                   "7.Registered Users of Top User",
                                                   "8.Transaction Amount and Count of Aggregated Transaction",
                                                   "9.Transaction Amount and Count of Map Transaction",
                                                   "10.Transaction Amount and Count of Top Transaction"]) 
                                       

    if question == "1.Transaction name of total Transaction_amount and transaction count in Aggregated Transaction":
        
        st.subheader("TRANSACTION NAME IN TOTAL TRANSACTION AMOUNT AND TRANSACTION COUNT")
        fig_chart_transcation_name_amount_count("aggregated_transaction")  

    elif question == "2.Brands of Transaction count in Aggregated User":
        
        st.subheader("TOP 10 BRANDS IN TRANSACTION COUNT AND LAST 10 BRANDS IN TRANSACTION COUNT AND AVERAGE OF BRANDS IN TRANSACTION COUNT")
        fig_chart_Brands_in_total_transaction_count("aggregated_user")

    elif question == "3.Brands of Percentage in Aggregated User":
        
        st.subheader("TOP 10 BRANDS IN PERCENTAGE AND LAST 10 BRANDS IN PERCENTAGE AND AVERAGE OF BRANDS IN PERCENTAGE")
        fig_chart_Brands_in_total_Percentage("aggregated_user")  

    elif question == "4.Transaction Count of Aggregated User":
        
        st.subheader("TRANSACTION COUNT")
        fig_chart_transcation_count("aggregated_user")   

    elif question == "5.Registered Users of Map User":
        
        st.subheader("REGISTERED USERS")

        states =st.selectbox("Select The State", map_user_DataFrame["States"].unique())
        fig_chart_Registered_users("map_user",states)       

    elif question == "6.App opens of Map User":
        
        st.subheader("APP OPENS")

        states =st.selectbox("Select The State", map_user_DataFrame["States"].unique())
        fig_chart_App_opens("map_user",states)  

    elif question == "7.Registered Users of Top User":
        
        st.subheader("REGISTERED USERS")
        fig_chart_topuser_Registered_users("top_user")

    elif question == "8.Transaction Amount and Count of Aggregated Transaction":
        
        st.subheader("TRANSACTION AMOUNT")
        fig_chart_transcation_amount("aggregated_transaction")

        st.subheader("TRANSACTION COUNT")
        fig_chart_transcation_count("aggregated_transaction")
        
        
    elif question == "9.Transaction Amount and Count of Map Transaction":

        st.subheader("TRANSACTION AMOUNT")
        fig_chart_transcation_amount("Map_transaction")

        st.subheader("TRANSACTION COUNT")
        fig_chart_transcation_count("Map_transaction")  
        
        
    elif question == "10.Transaction Amount and Count of Top Transaction":

        st.subheader("TRANSACTION AMOUNT")
        fig_chart_transcation_amount("top_transaction")

        st.subheader("TRANSACTION COUNT")
        fig_chart_transcation_count("top_transaction")  
        
               
     
