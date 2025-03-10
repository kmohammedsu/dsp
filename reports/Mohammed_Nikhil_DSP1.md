# Seattle Parking and Weather Analysis: Correlating Weather Conditions with Parking Demand

**Team Members:** Mohammed Khaja Moinuddin, Nikhil Ghugare

## 1. Problem Statement

Urban parking in Seattle remains a persistent challenge, with drivers facing unpredictable availability during peak hours. This unpredictability contributes to increased congestion, wasted time, and elevated emissions as vehicles search for available spots [1]. Moreover, external factors—especially weather conditions such as rain or extreme temperatures—can further influence parking occupancy and usage patterns [6]. Despite various municipal initiatives, there is no integrated platform that correlates real-time parking data with weather conditions to inform both the public and city planners [6]. Addressing this issue is crucial to improving urban mobility, reducing congestion, and promoting environmental sustainability.

## 2. Significance of Problem Statement

- Thousands of drivers and commuters in Seattle are affected by unpredictable parking availability in a densely populated urban environment.
- Adverse weather conditions exacerbate parking challenges, increasing travel times and contributing to congestion [4].
- A data-driven solution combining parking data with real-time weather insights could empower city planners and drivers to make informed decisions, ultimately improving urban mobility and sustainability [6].

## 3. Data Sets

### 3.1. Seattle Annual Parking Study Data (CSV)
- **Source:** Seattle Open Data Portal [1]
- **Relevance:** Provides historical insights into parking occupancy, revenue, and usage patterns across Seattle.
- **Preprocessing Needs:**
  - Clean and standardize column names
  - Handle missing or inconsistent values
  - Transform date fields and normalize numerical metrics (e.g., occupancy rates)

### 3.2. Open-Meteo API (JSON)
- **Source:** Open-Meteo API [2]
- **Relevance:** Delivers historical weather conditions (temperature, precipitation, wind speed) which can be correlated with parking behavior.
- **Preprocessing Needs:**
  - Extract key weather variables from the JSON response
  - Normalize units as needed (e.g., Fahrenheit vs. Celsius)
  - Synchronize weather data with parking data based on time and location

## 4. Algorithms and Technologies

### 4.1. Potential Algorithms
- **Random Forest Regression:** May be suitable for predicting available parking spots based on weather conditions and temporal features. This ensemble learning method could handle non-linear relationships and feature interactions [3].
- **XGBoost:** Could be implemented as a comparison model, utilizing gradient boosting techniques to predict parking availability.
- **Gradient Boosting Regression:** Might be tested as an alternative approach for prediction tasks.
- **K-means Clustering:** Could potentially group areas of Seattle by parking occupancy patterns and weather impact to identify high- and low-performing zones [3].
- **Cross-Validation:** Will likely implement k-fold cross-validation to ensure model robustness and prevent overfitting.

### 4.2. Potential Feature Engineering
- **Temporal Features:** Extract hour of day, day of week, month, weekend flags, and peak hour indicators from datetime information.
- **Weather Variables:** Utilize temperature, precipitation, wind speed, and elevation as key predictors.
- **Categorical Encoding:** Apply appropriate encoding to categorical variables such as location information and event indicators.
- **Feature Scaling:** Standardize numerical features to improve model performance and convergence.

### 4.3. Tools and Technologies
- **Programming:** Python
- **Libraries:** Pandas, NumPy, scikit-learn, Matplotlib, Seaborn
- **APIs:** Open-Meteo for historical weather data [2]; HTTP access to the Seattle Open Data Portal for parking study CSV data [1]
- **Visualization:** Matplotlib and Seaborn for static visualizations and analysis
- **Development Environment:** Jupyter Notebook for exploration and development

## 5. Risks

### 5.1. API Limitations
- **API Rate Limits:** Open-Meteo's API may have rate limits or occasional downtime that could delay data collection [2].

### 5.2. Data Quality and Availability
- **Data Inconsistencies:** The parking study dataset might contain incomplete records or inconsistencies that can affect the reliability of the analysis [1].

### 5.3. Integration Complexity
- **Data Synchronization:** Aligning historical parking data with weather data requires precise temporal and geospatial synchronization, which may prove challenging [3].

### 5.4. Scope Creep
- **Project Scope:** The effort to develop a comprehensive composite scoring system for parking performance could lead to overcomplicating the project if not managed carefully.

## 6. Challenges

### 6.1. Composite Metric Development
- **Metric Creation:** Creating a unified, actionable metric that balances parking occupancy, weather conditions, and temporal factors is nontrivial [3].
- **Scoring Formula:** Score = (Parking Occupancy × 0.5) + (Weather Impact × 0.3) + (Time of Day Factor × 0.2)

### 6.2. Geospatial and Temporal Alignment
- **Data Integration:** Accurately merging data from two distinct sources—historical CSV parking data and JSON weather data—by synchronizing timestamps and geolocating records poses significant challenges [6].

## 7. References

[1] City of Seattle. (2023). "Annual Parking Study Data." Seattle Open Data Portal. Available at: https://data.seattle.gov/Transportation/Annual-Parking-Study-Data/7jzm-ucez/about_data [Accessed December 15, 2023]

[2] Open-Meteo.com. (2023). "Historical Weather API Documentation - Open-Meteo.com." Available at: https://open-meteo.com/ [Accessed December 20, 2023]

[3] Wang, X., Li, Y., & Zhang, J. (2023). "A short-term parking demand prediction framework integrating overall and internal information." Sustainability, 15(9), 7096. DOI: 10.3390/su15097096

[4] Guo, Z., Wilson, N. H., & Rahbee, A. (2014). "Impact of weather on urban transit ridership." Transportation Research Part A: Policy and Practice, 64, 154-164. DOI: 10.1016/j.tra.2014.09.008

[5] City of Seattle. (2023). "Seattle Transportation Plan - Parking Management Reports." Seattle Department of Transportation. Available at: https://www.seattle.gov/transportation/document-library/citywide-plans/modal-plans/seattle-transportation-plan [Accessed January 5, 2024] 