# Wikipedia Poland Analysis (2001–2026)

## 📌 Project Overview
In celebration of the **25th anniversary of Polish Wikipedia**, this project analyzes historical data from the world's largest online encyclopedia. Developed as part of the 3rd edition of the **#BI_NGO** initiative (Business Intelligence for NGOs), it supports **Wikimedia Poland Association** in understanding and sharing insights about Wikipedia's growth.

> 🌐 **Note on Language:** While this repository documentation is written in English to support global accessibility, the **interactive Power BI report itself is published in Polish** to best serve the Wikimedia Poland Association and its local community.

This project delivers an end-to-end analysis of Polish Wikipedia's activity over a 25-year period (2001–2026). Using Wikimedia datasets, I built an interactive Power BI dashboard structured around three core pillars:
1. **Articles & Content (Artykuły i treść):** Evaluating the pace of content expansion and extracting rankings of the most popular articles.
2. **Community & Editors (Społeczność i edytorzy):** Analyzing new user registrations, tracking editor activity levels, and breaking down edits performed by human contributors vs. automated bots.
3. **Readership & Pageviews (Czytelnicy i wyświetlenia):** Checking overall pageview counts and breaking them down by user types and the types of devices used to browse Wikipedia.

## 📊 Interactive Dashboard Preview

**Live Report:** You can explore the fully interactive Power BI report directly in your browser:  
> 👉 **[Open Interactive Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiYTBhZjZjMmQtNDMzNC00NWFkLWEyZTktOWU0OTAyZWE4ZTM5IiwidCI6ImQwMzYzN2RmLTdiM2EtNDU2NC04NzBiLTA2MjJhODFhNzY0ZCJ9)**
>
> *(If the live preview is unavailable or loading, watch the quick feature walkthrough video below)*
>
> The video above demonstrates the interactive features of the dashboard. Detailed descriptions of the charts and pages can be found below.
> 

https://github.com/user-attachments/assets/6c9abcb8-ee0c-49fa-b8c2-b79d26f59a64

>
### 📊 Page 1: Home page
![Artykuły i treść](dashboard-views/Report_Wikipedia_1.png)
> 
### 📊 Page 2: Articles & Content (Artykuły i treść)

![Artykuły i treść](dashboard-views/Report_Wikipedia_2_2025.png)

### 📊 Page 3: Community & Editors (Społeczność i edytorzy)

![Artykuły i treść](dashboard-views/Report_Wikipedia_3_2025.png)

### 📊 Page 4: Readership & Pageviews (Czytelnicy i wyświetlenia)

![Artykuły i treść](dashboard-views/Report_Wikipedia_4_2025.png)


## 🛠️ Tech Stack & Tools

* **Power BI Desktop** – Data modeling, interactive visualization, and dashboard building.
* **Python (Pandas)** – Automated data exploration, cleaning, date standardization, and structural transformation of CSV files.
* **DAX (Data Analysis Expressions)** – Created calculated measures.
* **Power Query** – Additional data transformation.
* **GitHub** – Documentation, version control, and project hosting.

## ⚙️ Data Pipeline & ETL Process

Before building the dashboard in Power BI, I developed a Python-based data pipeline to explore, validate, and transform multi-source Wikimedia datasets into a clean, analytics-ready format:

1. **Data Inspection & EDA:** Checked data quality, structure, and missing values in raw CSV files.
2. **Standardization & Translation:** Renamed columns and translated source data/values into Polish for consistent reporting.
3. **Data Reshaping & Date Alignment:** Cleaned date formats and unpivoted a specific wide-format dataset into a long-format table to optimize data modeling and measure creation in Power BI.
4. **Export:** Exported clean CSV files ready to load into Power BI.

The complete Python source scripts are located in the [data-processing](./data-processing) directory.

## 🧮 Data Modeling & DAX Measures

To drive interactive analytics and dynamic report navigation, I designed a relational Data Model and developed a custom collection of DAX measures:

* **Core Measures:** Dynamic calculations for total pageviews, edits, user registrations, and editor activity.
* **Traffic Analytics & Rankings:** Measures calculating bot activity share (%) and mobile traffic share (%) for scorecard display, alongside logic to identify the most popular articles.
* **Dynamic Titles & UX:** Context-aware headers that update dynamically based on slicer selections.

> 💡 **Explore the Code:** The complete list of DAX measures and formulas can be inspected directly inside the Power BI report file (`Raport_Wikipedia.pbix`) in this repository.
