# 🚗 Stopping Sight Distance Calculator

This Python script calculates the Stopping Sight Distance (SSD) for a vehicle based on its speed, the road's grade and friction, and the driver's reaction time. It is designed to be a practical tool for civil engineering students, transportation planners, or anyone interested in road safety and design principles.

# ✨ Features

Comprehensive Calculation: Uses the standard engineering formula for calculating SSD, which combines braking distance and reaction distance.

Grade Adjustment: Accounts for both uphill (+) and downhill (-) road grades, as grade significantly impacts braking performance.

Input Validation: Includes basic validation to ensure realistic inputs for speed, friction, and grade.

User-Friendly Interface: Prompts the user for all necessary variables via the command line.

# 📐 Usage

To run the script, open your terminal or command prompt, navigate to the directory where the file is saved, and execute the Python interpreter:

    python Stopping_distance.py



The script will then prompt you to enter the required values:

<img width="767" height="258" alt="image" src="https://github.com/user-attachments/assets/752a0cfa-f438-4427-a48b-c38efc986140" />

# Calculation Details

The script calculates the Stopping Sight Distance (S) in feet (ft) using the standard formula, which is the sum of the Braking Distance and the Reaction Distance:

S=Braking Distance+Reaction Distance

# Python Code Implementation:

  Uphill Grade (+):

  <img width="390" height="71" alt="image" src="https://github.com/user-attachments/assets/f9d15acd-cbcc-4627-ae87-a6e72a5dffc4" />

In this case, the positive grade assists in braking, reducing the required stopping distance.

  Downhill Grade (-):

  <img width="378" height="74" alt="image" src="https://github.com/user-attachments/assets/80ed1dd8-65fb-419d-8903-c3adb64d2ba4" />

In this case, the negative grade opposes braking, increasing the required stopping distance.

The constant 1.4678 is a unit conversion factor for converting speed from mph to ft/s. The constant 29.84 is derived from the gravitational constant (g=32.2 ft/s2) and converts units for the braking term: 29.84≈2⋅g/1.4678.



