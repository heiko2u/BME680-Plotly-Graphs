# BME680-Plotly-Graphs

![2021-08-27 (2)](https://user-images.githubusercontent.com/20467384/131172948-378c8cc3-acf2-42db-a2bf-b1ad0e55960c.png)


Use plotly to display graphs for Temperature and Pressure using the BME680 sensor.



temperature-pressure-humidity.py --> file is used for Data Aquisition. All the data is store as  CSV. ( Run in background & and use nohup)

tempandhumiditygraph.py  --> Plotly scatter plot with range slider to display the data in a single page.

status.sh --> A simple error detection script to check if the file is running in the background.


