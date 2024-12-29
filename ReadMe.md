# Analysis of BnB Demand and Strategies for Increasing Demand

## Project Overview
This project focuses on analyzing the demand for BnB (a hypothetical product) using multivariable calculus. The primary goal is to identify factors influencing the demand and propose strategies to increase it. The analysis is performed using mathematical modeling, Python, and MATLAB/NumPy tools, with demand and its sensitivity to pricing changes being a focal point.

---

## Table of Contents
1. [Objective](#objective)
2. [By Hand Solution](#by-hand-solution)
3. [Flowchart/Code Flow Diagram](#flowchartcode-flow-diagram)
4. [Key Features](#key-features)
5. [Example Run and Results](#example-run-and-results)
6. [Graphs and Plots](#graphs-and-plots)
7. [Conclusion and Analysis](#conclusion-and-analysis)
8. [How to Run the Program](#how-to-run-the-program)
9. [Contributions](#contributions)
10. [Challenges Faced](#challenges-faced)
11. [Annexure](#annexure)
    - [Code for Main Tasks](#code-for-main-tasks)
    - [Code for Graph Plotting](#code-for-graph-plotting)

---

## Objective
The objective is to:
1. Model the demand of BnB using a multivariable demand function.
2. Analyze the impact of price changes on demand using derivatives.
3. Propose actionable strategies for increasing BnB demand.

---

## By Hand Solution
A mathematical approach was taken to analyze the demand equation, calculate derivatives, and interpret the results. The findings helped to shape actionable insights, such as monitoring competitor prices and enhancing the product's value.

---

## Flowchart/Code Flow Diagram
A detailed flowchart outlines the logic:
1. Calculate initial demand.
2. Derive demand sensitivity to pricing.
3. Provide actionable strategies.
4. Offer user interaction for rerunning the program.

---

## Key Features
- **Demand Calculation**: Computes BnB demand based on pricing factors.
- **Automatic Differentiation**: Analyzes sensitivity to pricing changes.
- **Graphical Representation**: Visualizes demand relationships in 3D.
- **Interactive Execution**: Offers a user-friendly interface for multiple runs.

---

## Example Run and Results
Example output:

Task 1: Demand of BnB when all prices are $100 each: 9500.00

Task 2: Derivative of demand with respect to BnB price: -6.00 P_B

Task 3: Derivative of demand with respect to Product A price: 3.60

Task 4: To increase demand, consider reducing BnB's price or enhancing its features.
---

## Graphs and Plots
Generated using `matplotlib`:
- **3D Surface Plot**: Shows how demand changes with respect to prices of BnB and its competitors.

---

## Conclusion and Analysis
- **Key Insights**: 
  - Demand is highly sensitive to price changes.
  - Strategic pricing and product improvements can mitigate demand loss.
- **Limitations**: The model assumes price as the only factor, excluding variables like marketing and economic conditions.

---

## How to Run the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/username/bnb-demand-analysis.git
   cd bnb-demand-analysis
