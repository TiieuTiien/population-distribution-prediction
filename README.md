# Analysis and Prediction of Population Distribution Based on Linear Regression Model.

This project involves analyzing a dataset of global population distribution from 1950 to 2021, utilizing a linear regression model for predictive insights. The dataset contains various numeric fields, and the analysis includes calculating essential statistical measures such as minimum, maximum, mean, standard deviation, and quantiles for the cleaned data.

The table outlines key features crucial for global population distribution analysis providing a foundational dataset for geographical and demographic research.

| Feature           | Description                                                                            |
|-------------------|----------------------------------------------------------------------------------------|
| Location          | Provides the name of the place or region, crucial for geographic analysis.             |
| Time              | Captures the specific year of the data, essential for time series analysis.            |
| PopMale           | Represents the male population count.                                                  |
| PopFemale         | Represents the female population count.                                                |
| PopTotal          | Represents the total population, can simplify analysis by providing total counts.      |
| AgeGrp (Optional) | Useful for age-specific population analysis, adds granularity to demographic analysis. |

*Important Features to Retain for Global Population Distribution Analysis*

| Data types | Columns                                                                                |
|------------|----------------------------------------------------------------------------------------|
| int64      | SortOrder, LocID, LocTypeID, ParentID, VarID, Time, MidPeriod, AgeGrpStart, AgeGrpSpan |
| float64    | Notes, SDMX_code, PopMale, PopFemale, PopTotal                                         |
| object     | ISO3_code, ISO2_code, LocTypeName, Location, Variant, AgeGrp                           |

*Categorization of WPP2022_PopulationBySingleAgeSex_Medium_1950-2021.csv columns by Data Type*

| Time   | AgeGrp | Location | PopTotal | Location_encoded |
|--------|--------|----------|----------|------------------|
| 1980   | 15     | CityA    | 2500     | 2600.0           |
| 1990   | 20     | CityB    | 3000     | 3100.0           |
| 2000   | 25     | CityA    | 2700     | 2600.0           |
| 2010   | 30     | CityC    | 4000     | 4000.0           |
| 2020   | 35     | CityB    | 3200     | 3100.0           |
