# Weather-Data-Processing
## Table of Content

- [Project Overview](#project-overview)
- [Challenges](#challenges)
- [Visualization](#visualization)





### Project Overview
This data processing pipeline is written to clean, process and analyze the weather.csv data source and get insights like average temperature in different cities and to visualize relation like temperature vs date.

 ### Prerequisties
 - python
     - **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
 - pip
    - **pip** (comes bundled with Python, but you can reinstall it if needed)
 - After installing check using this lines of code on command line 
       ```bash
         python --version
         pip --version```
     - If pip doesn't exist on your system
         - Run
       ```
       python -m ensurepip --upgrade
       ```
 ### Challenges 
I struggled a lot on standardizing my date column after trying different approaches I succeeded 
 1. Remove rows which null date values 
     ```python
            df=df[df['date'].notna()].reset_index(drop=True)
    ```
2. change the date format to the standard one which is YYYY-MM-DD which reduces ambiguity and uncertainity unlike the date formats DD-MM-YYYY and MM-DD-YYYY. Personally Ihate these two formats becasue unless we are not given dates like this 13-01-2005 You can not be sure which one is date which one is month
     ```python
        df['date'] = df['date'].astype(str)
        df.replace(r'[/.]','-', regex=True, inplace=True)
        df['date']=pd.to_datetime(df['date'],format='mixed')
  ### Visualization
    
  I made a bar chart using matplotlib 
   the bar chart is about average temperature vs Cities 
    ```python
            avg_temp_per_city = (
            df.groupby('city')['temperature_celsius'].mean()
         )
    ```
    
    plt.figure(figsize=(10, 6))
    avg_temp_per_city.sort_values(ascending=False).plot(kind='bar', color='skyblue')
    plt.title('Average Temperature per City (°C)')
    plt.xlabel('City')
    plt.ylabel('Temperature (°C)')
    plt.tight_layout()
    plt.savefig('output/avg_temperature_per_city.png')
    plt.close()
    
