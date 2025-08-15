# Grafana Website Traffic Dashboard

This project contains a Grafana dashboard to demonstrate how to visualize website user activity from a remote CSV file.

## Prerequisites

Before you begin, ensure you have the following:

1.  A running Grafana instance (version 10.0.0 or later).
2.  The **Infinity** data source plugin (`yesoreyeram-infinity-datasource`) installed in your Grafana instance. You can install it from the Grafana plugin catalog.

## Files

*   `dashboard.json`: The Grafana dashboard file.
*   `website_traffic_with_time.csv`: The sample data file (for reference).

## Setup Instructions

### Step 1: Import the Dashboard

1.  Open your Grafana instance in a web browser.
2.  Navigate to **Dashboards** -> **Import**.
3.  Click on **Upload JSON file** and select the `dashboard.json` file from this project.
4.  On the next screen, you will be prompted to select a data source for `DS_INFINITY`. Choose your pre-configured Infinity data source.
5.  Click **Import**.

The dashboard should now load and display the visualizations by fetching the data directly from GitHub.

Enjoy your demo!
