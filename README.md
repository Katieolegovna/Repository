<!-- README.md - English Version -->
<div align="center">

# 🛫 Airport Passenger Flow Analysis
### *Interactive dashboard with tables and charts based on passenger data*

<br>

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50%2B-FF4B4B?logo=streamlit)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-2.3%2B-150458?logo=pandas)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-6.3%2B-2962FF?logo=plotly)](https://plotly.com/python/)
[![Docker](https://img.shields.io/badge/Docker-2.2%2B-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

<br>

<div align="center">
  <a href="https://katiekurenkova.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo">
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/yourusername/airport-dashboard/blob/main/README_RU.md">
    <img src="https://img.shields.io/badge/🇷🇺_Русская_версия-README_RU.md-0077B5?style=for-the-badge" alt="Russian Version">
  </a>
</div>

<br>

<p align="center">
  <a href="#project-description">📋 Description</a> •
  <a href="#technologies-used">⚙️ Technologies</a> •
  <a href="#key-features">🔍 Features</a> •
  <a href="#screenshots">🖼️ Screenshots</a> •
  <a href="#how-to-run">🚀 Run</a> •
  <a href="#license">📝 License</a>
</p>

</div>

---

## 📋 Project Description
> **Demonstration of various table and chart variations for airport passenger flow analysis**

This project provides an interactive dashboard for analyzing synthetic airport passenger data. It includes multiple visualization options and filtering capabilities to explore passenger flow patterns, processing times, and airline performance.

**Project includes:**
- ✅ Synthetic passenger data generation (dates, destinations, airlines, terminals, processing times)
- ✅ Streamlit application with five tabs for different data display formats
- ✅ Interactive filters and Excel export functionality
- ✅ Comprehensive visualizations including charts and pivot tables

---

## ⚙️ Technologies Used

<div align="center">

| Component | Library/Tool | Purpose |
|-----------|--------------|---------|
| **Programming Language** | <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" height="20"> | Project foundation |
| **Data Generation** | <img src="https://img.shields.io/badge/Pandas-2.3%2B-150458?logo=pandas" height="20"> <img src="https://img.shields.io/badge/NumPy-1.24%2B-013243?logo=numpy" height="20"> | Synthetic data creation |
| **Data Processing** | <img src="https://img.shields.io/badge/Pandas-2.3%2B-150458?logo=pandas" height="20"> <img src="https://img.shields.io/badge/Openpyxl-3.1%2B-green" height="20"> | Excel read/write, data aggregation |
| **Visualization** | <img src="https://img.shields.io/badge/Plotly-6.3%2B-2962FF?logo=plotly" height="20"> | Interactive charts and graphs |
| **Interface** | <img src="https://img.shields.io/badge/Streamlit-1.50%2B-FF4B4B?logo=streamlit" height="20"> | Web application with tables and filters |
| **Containerization** | <img src="https://img.shields.io/badge/Docker-2.2%2B-2496ED?logo=docker" height="20"> | Container deployment |

</div>

---

## 🔍 Key Features

### 📊 **Data Generation & Management**
- **Synthetic Data**: Realistic passenger data with 10,000+ records
- **Dynamic Generation**: Script-based data creation with customizable parameters
- **Excel Export**: Save filtered results for external analysis

### 🎨 **Table Variations**
| Table Type | Description | Use Case |
|------------|-------------|----------|
| **Default Table** | Raw data display | Quick data inspection |
| **Filtered Table** | Interactive filtering | Focused data analysis |
| **Styled Table** | CSS-enhanced formatting | Presentation-ready views |
| **Pivot Table** | Aggregated statistics | Summary analysis |

### 📈 **Visualizations**
- **Line Charts**: Passenger flow trends over time
- **Heatmaps**: Passenger density by hour and day
- **Histograms**: Distribution analysis by airline
- **Bar Charts**: Comparative analysis of terminals

### ⚡ **Interactive Features**
- **Real-time Filtering**: Instant data filtering by multiple criteria
- **Theme Toggle**: Light/dark mode support
- **Responsive Design**: Works on different screen sizes
- **Export Options**: Data export in Excel format

---

## 🖼️ Screenshots

<div align="center">

### 📱 Dashboard Overview
<img src="assets/dashboard_main.png" alt="Dashboard Main Page" width="800" style="border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin: 10px;">
*Main dashboard interface with navigation tabs*

### 📊 Data Tables
<table>
<tr>
<td><img src="assets/Default.png" alt="Regular Table" width="380" style="border-radius: 8px;"></td>
<td><img src="assets/Filter.png" alt="Filtered Table" width="380" style="border-radius: 8px;"></td>
</tr>
<tr>
<td align="center"><i>Regular data table</i></td>
<td align="center"><i>Filtered table view</i></td>
</tr>
</table>

<table>
<tr>
<td><img src="assets/Stylistic.png" alt="Styled Table" width="380" style="border-radius: 8px;"></td>
<td><img src="assets/Summary.png" alt="Pivot Table" width="380" style="border-radius: 8px;"></td>
</tr>
<tr>
<td align="center"><i>Styled table with CSS</i></td>
<td align="center"><i>Pivot table analysis</i></td>
</tr>
</table>

### 📈 Charts & Visualizations
<img src="assets/dashboard_charts.png" alt="Charts Dashboard" width="800" style="border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin: 10px;">
*Interactive charts: line, heatmap, and histogram*

</div>

---

## 🚀 How to Run

### 📦 Local Installation

#### 1. Clone Repository
```bash
git clone https://github.com/yourusername/airport-dashboard.git
cd airport-dashboard