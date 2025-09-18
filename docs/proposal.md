# Air Quality & Pollution Prediction

**Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang  
**Author Name:** KASIREDDY SAI NITHIN REDDY
**GitHub Repo:**   https://github.com/ksainithin/UMBC-DATA606-Capstone  
**PowerPoint Presentation:**   to be added later


---

## 1. Background

**What is it about?**  
Air pollution is a major environmental and public health issue, causing respiratory and cardiovascular diseases and contributing to premature deaths worldwide. This project aims to **predict air pollutant levels (PM2.5, PM10, NO2, O3) in European cities** based on historical air quality and environmental data.

**Why does it matter?**  
Forecasting pollution levels allows governments, cities, and citizens to:  
- Take proactive measures to reduce exposure  
- Develop policies for urban planning and pollution control  
- Provide timely alerts for public health  

**Research Questions:**  
1. Can we accurately predict pollutant levels in European cities using historical air quality and weather data?  
2. Which factors (weather, city, season, time of day) have the most influence on pollutant levels?  
3. Can we create an interactive tool to forecast air pollution in real time?  

---

## 2. Data

**Data Sources:**  
- **Primary Dataset:** Urban Air Quality Dataset (Europe) – [Kaggle Link](https://www.kaggle.com/datasets/sogun3/uspollution)  
- **Optional Supplementary Dataset:** WHO or EEA health datasets for linking pollution to health outcomes  

**Data Size:** ~400 MB  
**Data Shape:** Tens of thousands of rows, ~10–15 columns  
**Time Period:** Varies by city (dataset contains hourly air quality measurements over multiple years)  
**Row Representation:** Each row represents an hourly measurement of air quality and weather parameters in a specific European city.

### Data Dictionary

| Column Name   | Data Type    | Definition                                   | Potential Values / Notes       | Use in ML Model |
|---------------|-------------|---------------------------------------------|--------------------------------|----------------|
| city          | Categorical | Name of the city                             | e.g., Paris, Berlin, London    | Feature        |
| datetime      | Datetime    | Timestamp of measurement                     | YYYY-MM-DD HH:MM               | Feature        |
| PM2.5         | Numeric     | Fine particulate matter                       | μg/m³                          | Target         |
| PM10          | Numeric     | Coarse particulate matter                     | μg/m³                          | Target         |
| NO2           | Numeric     | Nitrogen Dioxide concentration               | μg/m³                          | Target         |
| O3            | Numeric     | Ozone concentration                           | μg/m³                          | Target         |
| CO            | Numeric     | Carbon Monoxide concentration                | mg/m³                          | Feature        |
| SO2           | Numeric     | Sulfur Dioxide concentration                 | μg/m³                          | Feature        |
| temperature   | Numeric     | Air temperature                               | °C                             | Feature        |
| humidity      | Numeric     | Relative humidity                             | %                              | Feature        |
| wind_speed    | Numeric     | Wind speed                                    | m/s                            | Feature        |
| pressure      | Numeric     | Atmospheric pressure                          | hPa                            | Feature        |

**Target Variables:** PM2.5, PM10, NO2, O3  
**Feature Variables / Predictors:** city, datetime (converted to hour/day/month), temperature, humidity, wind_speed, pressure, CO, SO2  
