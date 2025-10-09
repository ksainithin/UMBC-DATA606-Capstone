# Air Quality & Pollution Prediction  

**Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang  
**Author:** Sai Nithin Reddy Kasireddy  
**GitHub Repo:** [UMBC-DATA606-Capstone](https://github.com/ksainithin/UMBC-DATA606-Capstone/tree/main)  
**LinkedIn Profile:** [Sai Nithin Reddy Kasireddy](https://www.linkedin.com/in/sai-nithin-reddy-1405b2220/)  
**PowerPoint Presentation:** [to be added later]  
**YouTube Video:** [to be added later]  

---

## 1. Background  

### What is it about?  
Air pollution is a critical global issue, impacting both **environmental sustainability** and **public health**. Pollutants like **PM2.5, PM10, NO2, and O3** are linked to respiratory illnesses, cardiovascular diseases, and premature deaths. This project aims to **predict pollutant levels in European cities** using historical air quality and weather data.  

### Why does it matter?  
Accurate predictions of air pollution can:  
- Enable governments and organizations to **issue health alerts** and protect vulnerable populations.  
- Help **urban planners and policymakers** design strategies to reduce emissions.  
- Provide **citizens with real-time insights** to make safer choices (e.g., outdoor activities).  

### Research Questions  
1. Can we accurately predict pollutant levels in European cities using historical air quality and weather data?  
2. Which environmental and meteorological factors most influence air pollution?  
3. Can we build an **interactive visualization tool** to forecast pollution levels in real time?  

---

## 2. Data  

### Data Sources  
- **Primary Dataset:** https://drive.google.com/file/d/15MnMJKjqzyWBcMvy1iBaxUspl_s4_-be/view?usp=sharing  
  

### Data Size  
- ~400 MB (compressed CSV files)  

### Data Shape  
- **Rows:** ~1048576 records  
- **Columns:** 28
  


### Row Representation  
Each row represents an **daily measurement** of air quality and meteorological factors in a specific city.  

---

## Data Dictionary  

| Column Name  | Data Type   | Definition                          | Potential Values / Notes       | Use in ML Model |
|--------------|------------|-------------------------------------|--------------------------------|-----------------|
| city         | Categorical | Name of the city                   | e.g., Paris, Berlin, London    | Feature         |
| datetime     | Datetime    | Timestamp of measurement           | YYYY-MM-DD HH:MM               | Feature         |
| PM2.5        | Numeric     | Fine particulate matter (µg/m³)     | Continuous values              | Target          |
| PM10         | Numeric     | Coarse particulate matter (µg/m³)   | Continuous values              | Target          |
| NO2          | Numeric     | Nitrogen Dioxide (µg/m³)           | Continuous values              | Target          |
| O3           | Numeric     | Ozone (µg/m³)                      | Continuous values              | Target          |
| CO           | Numeric     | Carbon Monoxide (mg/m³)            | Continuous values              | Feature         |
| SO2          | Numeric     | Sulfur Dioxide (µg/m³)             | Continuous values              | Feature         |
| temperature  | Numeric     | Air temperature (°C)               | Continuous values              | Feature         |
| humidity     | Numeric     | Relative humidity (%)              | Continuous values              | Feature         |
| wind_speed   | Numeric     | Wind speed (m/s)                   | Continuous values              | Feature         |
| pressure     | Numeric     | Atmospheric pressure (hPa)         | Continuous values              | Feature         |

---

### Target Variables  
- **PM2.5, PM10, NO2, O3**  

### Feature Variables / Predictors  
- **city, datetime (converted to hour/day/month), temperature, humidity, wind_speed, pressure, CO, SO2**  


