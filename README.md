# Grafana Website Traffic Dashboard

This project contains a Grafana dashboard and a sample CSV file to demonstrate how to visualize website user activity.

## Prerequisites

Before you begin, ensure you have the following:

1.  A running Grafana instance (version 10.0.0 or later).
2.  The **Infinity** data source plugin (`yesoreyeram-infinity-datasource`) installed in your Grafana instance. You can install it from the Grafana plugin catalog.

## Files

*   `dashboard.json`: The Grafana dashboard file.
*   `website_traffic_with_time.csv`: The sample data file.

## Setup Instructions

Follow these steps to get the dashboard up and running:

### Step 1: Place the CSV file

Place the `website_traffic_with_time.csv` file in a directory on your local machine.

### Step 2: Start a local web server

The Grafana dashboard is configured to fetch the data from a local web server. Open a terminal, navigate to the directory where you placed the CSV file, and run the following command:

```bash
python3 -m http.server 8000
```

This will start a simple web server on port 8000. Keep this terminal window open.

### Step 3: Import the Dashboard

1.  Open your Grafana instance in a web browser.
2.  Navigate to **Dashboards** -> **Import**.
3.  Click on **Upload JSON file** and select the `dashboard.json` file from this project.
4.  On the next screen, you will be prompted to select a data source for `DS_INFINITY`. Choose your pre-configured Infinity data source.
5.  Click **Import**.

The dashboard should now load and display the visualizations based on the data from the CSV file.

Enjoy your demo!
