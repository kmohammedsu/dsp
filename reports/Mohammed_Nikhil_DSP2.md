# Seattle Parking and Weather Analysis: Correlating Weather Conditions with Parking Demand

**Team Members:** Mohammed Khaja Moinuddin, Nikhil Ghugare

## 1. Problem Statement

Urban parking in Seattle remains a persistent challenge, with drivers facing unpredictable availability during peak hours. This unpredictability contributes to increased congestion, wasted time, and elevated emissions as vehicles search for available spots [1]. Moreover, external factors—especially weather conditions such as rain or extreme temperatures—can further influence parking occupancy and usage patterns [6]. Despite various municipal initiatives, there is no integrated platform that correlates real-time parking data with weather conditions to inform both the public and city planners [6]. Addressing this issue is crucial to improving urban mobility, reducing congestion, and promoting environmental sustainability.

## 2. Data Acquisition & Preprocessing

### 2.1. Data Sources

| Data Source | Format | Storage Solution | Description |
|-------------|--------|------------------|-------------|
| Seattle Parking Study Data | CSV | File Storage | Provides historical parking occupancy trends. |
| Open-Meteo API | JSON | Stored in CSV | Captures historical weather conditions in Seattle. |

### 2.2. Extract, Clean, Process (ECP) Approach

#### 2.2.1. Extract
- **Data Sources:**
  - CSV parking data downloaded from the Seattle Open Data Portal [1]
  - Historical weather data retrieved from Open-Meteo API for five specific Seattle neighborhoods

#### 2.2.2. Clean
- **Data Standardization:** Removed missing values, standardized date-time formats, and normalized numerical values
- **Weather Processing:** Extracted key weather attributes (temperature, precipitation, wind speed)
- **Data Validation:** Handled negative available parking spots by setting them to zero (125,570 instances found and corrected)

#### 2.2.3. Process
- **Parking Data:** Stored in structured CSV format for local analysis
- **Weather Data:** Processed JSON data into CSV format for integration with parking data
- **Data Integration:** Merged datasets on timestamps for unified analysis, resulting in a dataset of 838,840 records with 26 features

## 3. Literature Survey

### 3.1. A Short-Term Parking Demand Prediction Framework Integrating Overall and Internal Information

**Citation:**  
Wang, X., Li, Y., & Zhang, J. (2023). A short-term parking demand prediction framework integrating overall and internal information. Sustainability, 15(9), 7096. https://doi.org/10.3390/su15097096 [3]

**Summary:**  
This study proposes a framework for short-term parking demand prediction by integrating external factors (traffic, weather) and internal parking facility characteristics. The authors demonstrate that machine learning models utilizing spatial and temporal dependencies significantly improve forecasting accuracy.

**Relevance to Project:**  
This paper supports our project by validating our approach of incorporating weather data into parking demand forecasting models [3].

### 3.2. Impact of Weather on Urban Transit Ridership

**Citation:**  
Guo, Z., Wilson, N. H., & Rahbee, A. (2014). Impact of weather on urban transit ridership. Transportation Research Part A: Policy and Practice, 64, 154-164. https://doi.org/10.1016/j.tra.2014.09.008 [4]

**Summary:**  
This research analyzes how different weather conditions impact urban transit usage by studying data from New York City Transit. The study finds that rain, snow, and extreme temperatures reduce public transit ridership, causing more people to switch to personal vehicles, which in turn increases parking demand.

**Relevance to Project:**  
This paper helps us understand how weather-driven transit behavior influences parking occupancy trends, strengthening our hypothesis that parking demand is weather-dependent [4].

## 4. Data Management System Design

### 4.1. Storage & Retrieval Mechanisms

| Data Source | Format | Storage Solution | Purpose |
|-------------|--------|------------------|---------|
| Seattle Parking Data | CSV | File Storage | Stores historical parking occupancy data. |
| Weather Data | JSON | Processed to CSV | Stores historical weather data for analysis. |
| Merged Dataset | CSV | File Storage | Combines parking and weather data for modeling. |

## 5. Preliminary Exploratory Data Analysis (EDA)

### 5.1. Findings So Far

- **Weekday vs. Weekend Trends:** Parking occupancy is higher on weekdays, with reduced demand on weekends
- **Weather Influence:** Rainy conditions increase parking demand, likely due to decreased public transit usage
- **Time-of-Day Variation:** Peak demand occurs between 8 AM – 10 AM (morning rush) and 5 PM – 7 PM (evening rush)
- **Temperature Impact:** Moderate temperatures (10-15°C) show different parking patterns compared to higher temperatures
- **Regional Variations:** Different Seattle neighborhoods show varying sensitivity to weather conditions, with elevation differences across regions:
  - **Downtown Seattle:** 59m
  - **Capitol Hill:** 104m
  - **South Lake Union:** 11m
  - **Ballard:** 18m
  - **Industrial District:** 6m

### 5.2. Visualizations Created

#### 5.2.1. Parking Data Visualizations
- **Time Series Analysis:** Plotted parking occupancy trends over time to identify patterns and seasonality
- **Correlation Heatmap:** Visualized relationships between different parking metrics
- **Scatter Plot:** Examined relationships between parking spaces and vehicle counts
- **Weekday/Weekend Analysis:** Compared parking patterns between weekdays and weekends
- **Time of Day Analysis:** Analyzed how parking demand fluctuates throughout the day

#### 5.2.2. Weather Data Visualizations
- **Temperature Trends:** Visualized temperature patterns across different Seattle neighborhoods
- **Precipitation Distribution:** Analyzed rainfall patterns and their distribution
- **Wind Speed Distribution:** Examined wind speed variations across the dataset
- **Elevation by Region:** Compared elevation differences between the five Seattle neighborhoods

#### 5.2.3. Merged Data Visualizations
- **Weather-Parking Correlation:** Identified correlations between weather variables and parking metrics
- **Precipitation Analysis:** Analyzed how rainfall affects parking demand
- **Temperature Impact:** Examined the relationship between temperature and parking occupancy
- **Wind Speed Effects:** Investigated how wind speed influences parking behavior

## 6. Algorithms & Technologies Used

### 6.1. Machine Learning Models Implemented

- **Random Forest Regression:** Our primary model for predicting available parking spots based on weather conditions and temporal features. This ensemble learning method was selected for its ability to handle non-linear relationships and feature interactions. The model achieved an R² score of 0.8343 on the test set, RMSE of 1.4675, and relative error of 0.3970 [3, 5].

- **XGBoost:** Implemented as a comparison model, utilizing gradient boosting techniques to predict parking availability. Achieved an R² score of 0.7389 on validation data.

- **Gradient Boosting Regression:** Tested as an alternative approach, but demonstrated lower performance metrics (R² of 0.5475) compared to Random Forest.

### 6.2. Feature Engineering Applied

- **Temporal Features:** Extracted hour of day, day of week, month, weekend flags, and peak hour indicators from datetime information
- **Weather Variables:** Utilized temperature, precipitation, wind speed, and elevation as key predictors
- **Categorical Encoding:** Applied label encoding to categorical variables such as Study_Area, Sub_Area, Side, and other location information
- **Feature Scaling:** Standardized numerical features using StandardScaler to improve model performance and convergence

### 6.3. Tools & Platforms

| Category | Technology Used |
|----------|----------------|
| **Programming** | Python |
| **API Integration** | Requests, JSON |
| **Data Processing** | Pandas, NumPy |
| **Storage** | CSV (Local) |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn, XGBoost |

## 7. Challenges Faced

- **API Limitations:** Open-Meteo API required careful handling to retrieve historical weather data for multiple locations [2]
- **Data Integration:** Aligning timestamps and merging CSV (structured) parking data with JSON (semi-structured) weather data required additional preprocessing
- **Feature Engineering:** Identifying which weather factors impact parking demand the most was challenging
- **Data Cleaning:** The dataset contained 125,570 instances where available parking spots were negative, requiring data cleaning decisions
- **Model Selection:** Balancing model complexity with performance required extensive cross-validation testing

## 8. Plan for Completion (DSP3 - Due March 10, 2025)

### 8.1. Remaining Tasks

1. **Model Optimization:** Select the best performing model between Random Forest, XGBoost, or Gradient Boosting and fine-tune hyperparameters
2. **Visualization Development:** Create additional visualizations to display parking trends and forecasts
3. **Model Evaluation:** Conduct comprehensive evaluation using R², RMSE, and relative error metrics
4. **Final Documentation:** Prepare final report and presentation summarizing methodologies and results

## 9. Conclusion & Next Steps

This project successfully integrates historical weather data with parking occupancy data to analyze and predict parking availability trends. Our key accomplishments include:

- **Data Processing:** Successfully merged and preprocessed large datasets (838,840 records with 26 features)
- **Pattern Discovery:** Identified strong correlations between weather conditions and parking demand
- **Model Performance:** Developed a Random Forest model with strong predictive performance (R² of 0.8343)

Our final steps involve model optimization, visualization refinement, and preparing for the final presentation. The insights gained from this project will contribute to improved urban mobility planning and more efficient parking management in Seattle.

## 10. References

[1] City of Seattle. (2023). "Annual Parking Study Data." Seattle Open Data Portal. Available at: https://data.seattle.gov/Transportation/Annual-Parking-Study-Data/7jzm-ucez/about_data [Accessed December 15, 2023]

[2] Open-Meteo.com. (2023). "Historical Weather API Documentation - Open-Meteo.com." Available at: https://open-meteo.com/ [Accessed December 20, 2023]

[3] Wang, X., Li, Y., & Zhang, J. (2023). "A short-term parking demand prediction framework integrating overall and internal information." Sustainability, 15(9), 7096. DOI: 10.3390/su15097096

[4] Guo, Z., Wilson, N. H., & Rahbee, A. (2014). "Impact of weather on urban transit ridership." Transportation Research Part A: Policy and Practice, 64, 154-164. DOI: 10.1016/j.tra.2014.09.008

[5] Chen, P., et al. (2023). "Machine learning applications in urban parking management: A systematic review." Transportation Research Part C: Emerging Technologies, 146, 103997. DOI: 10.1016/j.trc.2023.103997

[6] City of Seattle. (2023). "Seattle Transportation Plan - Parking Management Reports." Seattle Department of Transportation. Available at: https://www.seattle.gov/transportation/document-library/citywide-plans/modal-plans/seattle-transportation-plan [Accessed January 5, 2024] 