# Heart Failure Prediction
<div align= "center">
    <img src= "https://i.imgur.com/qJYdHpX.png" alt= "Heart Disease Prediction">
</div>
## Overview
Heart Failure Prediction is a data-driven project aiming to predict heart failure based on a diverse set of health indicators. The dataset encompasses key factors, including age, gender, chest pain type, blood pressure, cholesterol levels, and more.

## Dataset Features
- Age: Age of the patient (in years)
- Sex: Gender of the patient
    - M: Male
    - F: Female
- ChestPainType: Chest pain type
    - TA: Typical Angina
    - ATA: Atypical Angina
    - NAP: Non-Anginal Pain
    - ASY: Asymptomatic
- RestingBP: Resting blood pressure (in mm Hg)
- Cholesterol: Serum cholesterol levels (in mm/dl)
- FastingBS: Fasting blood sugar
    - 1: if FastingBS > 120 mg/dl
    - 0: otherwise
- RestingECG: Resting electrocardiogram results
    - Normal: Normal
    - ST: Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
    - LVH: Showing probable or definite left ventricular hypertrophy by Estes' criteria
- MaxHR: Maximum heart rate achieved (numeric value between 60 and 202)
- ExerciseAngina: Exercise-induced angina
    - Y: Yes
    - N: No
- Oldpeak: Oldpeak = ST (numeric value measured in depression)
- ST_Slope: The slope of the peak exercise ST segment
    - Up: Upsloping
    - Flat: Flat
    - Down: Downsloping
- HeartDisease: Output class
    - 1: Heart disease
    - 0: Normal

## Getting Started
### Prerequisites
Ensure you have Python and the required dependencies installed. You can install them using:
```bash
pip install -r requirements.txt
```

### Usage
1. Clone the repository:
```bash
git clone https://github.com/AKA-SSH/Heart-Failure-Prediction.git
```
2. Navigate to the project directory:
```bash
cd ingestion.py
```
3. Run the prediction script
