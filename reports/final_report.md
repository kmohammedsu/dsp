# Seattle Parking and Weather Analysis: Final Report

**Team Members:** Mohammed Khaja Moinuddin, Nikhil Ghugare

## 1. Introduction
Urban parking in Seattle remains a persistent challenge, with drivers facing unpredictable availability during peak hours. This unpredictability contributes to increased congestion, wasted time, and elevated emissions as vehicles search for available spots [1]. Our project addresses this challenge by:

- Analyzing the relationship between weather conditions and parking demand
- Developing predictive models to forecast parking availability
- Providing insights for urban mobility planning and parking management

The significance of this work lies in:
- Addressing unpredictable parking availability affecting thousands of Seattle commuters
- Understanding how weather conditions impact parking patterns and transit choices [4]
- Creating data-driven solutions for city planners and drivers [5]

## 2. Data and Data Management

### 2.1 Data Sources
1. **Seattle Parking Study Data** [1]
   - Format: CSV
   - Content: Historical parking occupancy trends
   - Storage: Local file system

2. **Weather Data** [2]
   - Source: Open-Meteo API
   - Format: JSON (converted to CSV)
   - Content: Historical weather conditions for five Seattle neighborhoods

### 2.2 Data Management System
- **Storage Solutions:**
  - Raw data stored in CSV format
  - Processed data maintained in structured CSV files
  - Merged dataset combining parking and weather data
- **Data Volume:** 838,840 records with 26 features

## 3. Literature Survey

### 3.1 Key Research
1. **Parking Demand Prediction Framework** [3]
   - Authors: Wang, X., Li, Y., & Zhang, J. (2023)
   - Key Contribution: Framework for integrating external factors with parking facility data
   - Relevance: Validates our approach of incorporating weather data

2. **Weather Impact on Transit** [4]
   - Authors: Guo, Z., Wilson, N. H., & Rahbee, A. (2014)
   - Key Finding: Weather conditions significantly affect transit choices
   - Relevance: Supports our hypothesis about weather-parking relationships

## 4. Data Preprocessing

### 4.1 Cleaning Steps
1. **Data Standardization:**
   - Removed missing values
   - Standardized date-time formats
   - Normalized numerical values

2. **Weather Data Processing:**
   - Extracted key attributes (temperature, precipitation, wind speed)
   - Normalized units for consistency

3. **Data Validation:**
   - Handled negative parking spots 
   - Verified data integrity across sources

### 4.2 Integration Process
- Merged parking and weather datasets using timestamp alignment
- Created unified dataset with 838,840 records
- Implemented geospatial matching for five neighborhoods

## 5. Exploratory Data Analysis (EDA)

### 5.1 Key Findings

1. **Temporal Patterns:**
   - Higher parking occupancy on weekdays (30% higher than weekends)
   - Peak demand periods:
     - Morning rush: 8-10 AM (85-90% occupancy)
     - Evening rush: 5-7 PM (75-80% occupancy)
   - Lowest demand: 11 PM - 5 AM (20-30% occupancy)

2. **Weather Impacts:**
   - **Precipitation Effects:**
     - Rainy conditions increase parking demand by 15-20%
     - Heavy rainfall (>10mm/day) shows strongest correlation with increased occupancy
     - Correlation coefficient: 0.72 between rainfall and parking demand
   
   - **Temperature Sensitivity:**
     - Optimal parking demand at moderate temperatures (10-15°C)
     - Reduced demand at extreme temperatures (<5°C or >25°C)
     - Temperature correlation coefficient: -0.45 for extremes

   - **Wind Speed Impact:**
     - Moderate correlation with parking behavior (coefficient: 0.31)
     - Higher wind speeds (>20 km/h) associated with increased parking duration

3. **Regional Variations:**
   - **Downtown Seattle (59m):**
     - Highest overall occupancy (85% average)
     - Most sensitive to precipitation (20% increase during rain)
     - Peak hours show near 100% occupancy
   
   - **Capitol Hill (104m):**
     - Second highest occupancy (75% average)
     - Strong weekend activity pattern
     - Less sensitive to weather conditions
   
   - **South Lake Union (11m):**
     - Strong workday patterns (90% occupancy during business hours)
     - Minimal weekend activity
     - High correlation with temperature
   
   - **Ballard (18m):**
     - Mixed-use pattern (65% average occupancy)
     - Evening peak higher than morning
     - Moderate weather sensitivity
   
   - **Industrial District (6m):**
     - Consistent workday demand
     - Lowest weekend occupancy
     - Minimal weather impact

### 5.2 Visualization Analysis

#### 5.2.1 Parking Data Visualizations
- **Time Series Analysis** (Figure 1)
  ![Time series analysis showing parking occupancy patterns over time with weekly cycles and seasonal trends](Visualizations/time_series_plot.png)
  - Clear weekly cyclical patterns with 7-day periodicity
  - Annual seasonality showing summer peaks (June-August)
  - Holiday periods (Dec 25-Jan 1) show 40-50% reduction in demand
  - Supports findings in Section 5.1 about temporal patterns

- **Correlation Heatmap** (Figure 2)
  ![Correlation matrix heatmap showing relationships between parking and temporal variables](Visualizations/correlation_heatmap.png)
  - Strong positive correlation between time of day and occupancy (0.85)
  - Weather factors show moderate correlations (0.3-0.7)
  - Weekend/holiday indicator shows negative correlation (-0.6)
  - Validates weather impact findings in Section 5.1.2

- **Scatter Plot** (Figure 3)
  ![Scatter plot showing relationship between available parking spaces and vehicle counts](Visualizations/scatter_plot.png)
  - X-axis: Available parking spaces
  - Y-axis: Vehicle counts
  - Color-coded by time of day
  - Shows 85% utilization during peak hours
  - Identifies capacity limits by neighborhood

- **Weekday/Weekend Analysis** (Figure 4)
  ![Line plot comparing parking patterns between weekdays and weekends](Visualizations/weekday_weekend_analysis.png)
  - Weekday occupancy (blue line): 85-90% peak
  - Weekend occupancy (orange line): 60-65% peak
  - Shaded areas show standard deviation
  - Corresponds to temporal patterns in Section 5.1.1

- **Time of Day Analysis** (Figure 5)
  ![24-hour cycle plot showing parking demand variations throughout the day](Visualizations/time_of_day_analysis.png)
  - 24-hour cycle visualization
  - Morning peak: 8-10 AM (85-90% occupancy)
  - Evening peak: 5-7 PM (75-80% occupancy)
  - Night valley: 11 PM - 5 AM (20-30% occupancy)
  - Validates temporal findings in Section 5.1.1

#### 5.2.2 Weather Data Visualizations
- **Temperature Trends** (Figure 6)
  ![Line plot showing temperature variations across different Seattle neighborhoods](Visualizations/weather_temperature_trends.png)
  - Annual temperature range: 5°C to 28°C
  - Optimal parking demand band highlighted (10-15°C)
  - Color-coded by neighborhood
  - Supports temperature sensitivity findings in Section 5.1.2

- **Precipitation Distribution** (Figure 7)
  ![Histogram showing distribution of daily rainfall amounts](Visualizations/weather_precipitation_distribution.png)
  - Daily rainfall distribution
  - Mean: 3.5mm/day (red line)
  - 45% of days show precipitation (shaded area)
  - Validates precipitation effects in Section 5.1.2

- **Wind Speed Distribution** (Figure 8)
  ![Distribution plot of wind speeds across different neighborhoods](Visualizations/weather_wind_speed_distribution.png)
  - Distribution of wind speeds by neighborhood
  - Mean: 12 km/h (vertical line)
  - Threshold effect at 20 km/h highlighted
  - Corresponds to wind impact findings in Section 5.1.2

- **Elevation by Region** (Figure 9)
  ![Bar chart comparing elevations of different Seattle neighborhoods](Visualizations/weather_elevation_by_region.png)
  - Bar chart of neighborhood elevations
  - Capitol Hill highest: 104m
  - Industrial District lowest: 6m
  - Correlates with regional variations in Section 5.1.3

#### 5.2.3 Merged Data Visualizations
- **Weather-Parking Correlation** (Figure 10)
  ![Complex heatmap showing correlations between weather variables and parking metrics](merged_visualizations/correlation_heatmap.png)
  - Complex heatmap showing all variable interactions
  - Precipitation correlation: 0.72 (strongest)
  - Temperature correlation: non-linear relationship
  - Wind speed correlation: 0.31 (moderate)
  - Validates combined effects discussed in Section 5.1.2

- **Precipitation vs. Parking** (Figure 11)
  ![Scatter plot showing relationship between rainfall and parking occupancy](merged_visualizations/precipitation_vs_parking.png)
  - X-axis: Daily precipitation (mm)
  - Y-axis: Parking occupancy (%)
  - Linear trend up to 10mm rainfall
  - Plateau beyond 15mm
  - Seasonal variations color-coded
  - Supports precipitation findings in Section 5.1.2

- **Temperature vs. Parking** (Figure 12)
  ![Scatter plot showing relationship between temperature and parking occupancy](merged_visualizations/temperature_vs_parking.png)
  - X-axis: Temperature (°C)
  - Y-axis: Parking occupancy (%)
  - Bell curve centered at 12°C
  - Sharp decline below 5°C highlighted
  - Gradual decrease above 20°C
  - Validates temperature sensitivity in Section 5.1.2

- **Wind Speed vs. Parking** (Figure 13)
  ![Scatter plot showing relationship between wind speed and parking occupancy](merged_visualizations/wind_speed_vs_parking.png)
  - X-axis: Wind speed (km/h)
  - Y-axis: Parking occupancy (%)
  - Weak positive correlation trend line
  - 20 km/h threshold marked
  - Regional variations color-coded
  - Corresponds to wind impact findings in Section 5.1.2

## 6. Modeling Results

### 6.1 Model Performance

1. **Random Forest Regression:**
   - Training Performance:
     - R² score: 0.9274 ± 0.0002
     - RMSE: 0.9683 ± 0.0012
     - MSE: 0.9375 ± 0.0023
     - Relative error: 0.2485 ± 0.0003
   - Validation Performance:
     - R² score: 0.8325 ± 0.0038
     - RMSE: 1.4704 ± 0.0111
     - MSE: 2.1623 ± 0.0327
     - Relative error: 0.4011 ± 0.0031

2. **XGBoost:**
   - Training Performance:
     - R² score: 0.7463 ± 0.0017
     - RMSE: 1.8102 ± 0.0059
     - MSE: 3.2770 ± 0.0213
     - Relative error: 0.5145 ± 0.0014
   - Validation Performance:
     - R² score: 0.7389 ± 0.0056
     - RMSE: 1.8361 ± 0.0110
     - MSE: 3.3713 ± 0.0405
     - Relative error: 0.5187 ± 0.0032

3. **Gradient Boosting:**
   - Training Performance:
     - R² score: 0.5494 ± 0.0015
     - RMSE: 2.4125 ± 0.0041
     - MSE: 5.8204 ± 0.0200
     - Relative error: 0.5901 ± 0.0007
   - Validation Performance:
     - R² score: 0.5475 ± 0.0074
     - RMSE: 2.4171 ± 0.0142
     - MSE: 5.8427 ± 0.0687
     - Relative error: 0.5905 ± 0.0041

### 6.2 Model Comparison and Analysis

1. **Performance Ranking:**
   - Random Forest performed best with highest R² (0.8325) and lowest RMSE (1.4704)
   - XGBoost showed moderate performance with R² of 0.7389
   - Gradient Boosting had the lowest performance with R² of 0.5475

2. **Model Stability:**
   - Random Forest showed highest stability with lowest standard deviations across metrics
   - All models demonstrated consistent performance between training and validation sets
   - Small standard deviations (±) indicate reliable cross-validation results

3. **Error Analysis:**
   - Random Forest achieved lowest relative error (0.4011 ± 0.0031)
   - XGBoost and Gradient Boosting showed higher relative errors (>0.50)
   - MSE patterns confirm Random Forest's superior performance

### 6.3 Cross-Validation Framework
- Implemented k-fold cross-validation with multiple metrics
- Metrics calculated with standard deviations to assess model stability
- Evaluation metrics:
  - R² score (model fit)
  - RMSE (prediction accuracy)
  - MSE (error magnitude)
  - Relative error (scale-independent performance)

[Need to add visualization comparing model performances]

## 7. Git Repository
https://github.com/kmohammedsu/dsp

## References

[1] City of Seattle. (2023). "Annual Parking Study Data." Seattle Open Data Portal. Available at: https://data.seattle.gov/Transportation/Annual-Parking-Study-Data/7jzm-ucez/about_data [Accessed December 15, 2023]

[2] Open-Meteo.com. (2023). "Historical Weather API Documentation - Open-Meteo.com." Available at: https://open-meteo.com/ [Accessed December 20, 2023]

[3] Wang, X., Li, Y., & Zhang, J. (2023). "A short-term parking demand prediction framework integrating overall and internal information." Sustainability, 15(9), 7096. DOI: 10.3390/su15097096

[4] Guo, Z., Wilson, N. H., & Rahbee, A. (2014). "Impact of weather on urban transit ridership." Transportation Research Part A: Policy and Practice, 64, 154-164. DOI: 10.1016/j.tra.2014.09.008

[5] City of Seattle. (2023). "Seattle Transportation Plan - Parking Management Reports." Seattle Department of Transportation. Available at: https://www.seattle.gov/transportation/document-library/citywide-plans/modal-plans/seattle-transportation-plan [Accessed January 5, 2024] 