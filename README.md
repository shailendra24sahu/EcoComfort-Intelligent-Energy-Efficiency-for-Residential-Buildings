# EcoComfort-Intelligent-Energy-Efficiency-for-Residential-Buildings
![Screenshot (74)](https://github.com/shailendra24sahu/EcoComfort-Intelligent-Energy-Efficiency-for-Residential-Buildings/assets/101089059/37636c22-21e1-43c8-a698-3ee0ba59a2d7)


EcoComfort: Intelligent Energy Efficiency model is a machine learning
regression model. This project aims to leverage industrial automation techniques to enhance
energy efficiency in residential buildings by accurately predicting the heating load and cooling
load. The system, named "EcoComfort," combines advanced algorithms and data analysis to
optimize HVAC systems, leading to improved comfort and reduced energy consumption.
- HVAC stands for Heating, Ventilation, and Air Conditioning. An HVAC system refers to the
equipment and infrastructure used in buildings to control and regulate indoor environmental
conditions, including temperature, humidity, and air quality.
- The heating component of an HVAC system is responsible for generating and distributing heat
throughout a building, typically using methods such as furnaces, boilers, or heat pumps. It ensures
that the indoor temperature remains comfortable during colder periods.
- Ventilation is another critical aspect of an HVAC system. It involves the exchange of indoor and
outdoor air to maintain proper air circulation, remove contaminants, and control humidity levels.
Ventilation systems can include fans, ductwork, and air vents.
- Air conditioning, the third component of an HVAC system, involves cooling and dehumidifying
indoor air. Air conditioners use various methods, such as refrigeration cycles or evaporative
cooling, to lower the temperature and remove excess moisture from the air.


## Problem Statement
Inefficient heating, ventilation, and air conditioning (HVAC) systems in residential buildings lead
to excessive energy consumption and discomfort for occupants. The lack of accurate load
predictions and suboptimal HVAC operations contribute to increased energy costs and
environmental impact. There is a need for an industrial automation solution that accurately predicts
heating and cooling loads, optimizing HVAC systems for improved energy efficiency and
occupant comfort. The proposed "EcoComfort" system aims to address these challenges by
combining advanced algorithms and data analysis to dynamically adjust HVAC operations based
on real-time load requirements.
- Link : [Problem Statement](./Documentation/EcoComfort_Intelligent_Energy_Efficiency.pdf)

## Proposed Solution
To enhance energy efficiency in residential buildings and accurately predict the heating load and
cooling load, a machine learning regression model will be developed. The model will utilize
comprehensive data on various measurements within the building to accurately estimate the
specific heating and cooling requirements.
This approach will enable the optimization of HVAC systems to match the actual requirements,
resulting in reduced energy waste and improved comfort levels for occupants.

## Exploratory Data Analysis 
Link : [EDA Notebook](./EDA/notebook.ipynb)

## Architecture Design
Link : [Architecture Design](./Documentation/Architecture_Design.pdf)

# How to run?
### Steps to Run this project:

Clone the repository

```bash
https://github.com/shailendra24sahu/EcoComfort-Intelligent-Energy-Efficiency-for-Residential-Buildings 
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -p venv python==3.7
```
### Activate the environment
```bash
conda activate venv
```


### STEP 02- Install the requirements
```bash
pip install -r requirements.txt
```

### Finally run the following command
```bash
python main.py
```

Now,
```bash
open up your local host and port
```

# Demo-Preview
Link : [Demo-Video](./Documentation/Project_Demo_Video.mp4)

![prediction video](https://github.com/shailendra24sahu/EcoComfort-Intelligent-Energy-Efficiency-for-Residential-Buildings/assets/101089059/ceda3abc-16f3-4d5f-81cd-c4e0cbc05198)




## Model Training
Link : [Model Training file](train.py)


# Documentation

## Detailed Project Report
Link : [DPR](./Documentation/DPR.pdf)

## Low Level Design
Link : [LLD](./Documentation/Low_Level_Design_LLD.pdf)

## Hign Level Design
Link : [HLD](./Documentation/High_Level_Design_HLD.pdf)

## Wireframe Document
Link : [Wireframe Document](./Documentation/Wireframe_Document.pdf)
