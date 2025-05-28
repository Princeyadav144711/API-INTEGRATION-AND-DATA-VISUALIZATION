import pandas as pd
from fpdf import FPDF

# Load weather_data from CSV file
def load_data(file_name):
    try:
        data = pd.read_csv(file_name)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

# Analyze weather patterns
def analyze_weather(data):
    try:
        # Calculate average temperature and humidity
        avg_temp = data['Temperature'].mean()
        avg_humidity = data['Humidity'].mean()
        
        # Calculate highest and lowest temperature
        max_temp = data['Temperature'].max()
        min_temp = data['Temperature'].min()
        
        # Calculate most common weather condition
        most_common_condition = data['Condition'].mode()[0]
        
        print("Weather patterns analyzed successfully.")
        return avg_temp, avg_humidity, max_temp, min_temp, most_common_condition
    except Exception as e:
        print(f"Error analyzing weather patterns: {str(e)}")
        return None

# Generate PDF report
def generate_report(file_name, avg_temp, avg_humidity, max_temp, min_temp, most_common_condition):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=24)
        pdf.cell(200, 10, txt="Weather Patterns Analysis Report", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Average Temperature: {avg_temp:.2f}°C", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Average Humidity: {avg_humidity:.2f}%", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Highest Temperature: {max_temp:.2f}°C", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Lowest Temperature: {min_temp:.2f}°C", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Most Common Weather Condition: {most_common_condition}", ln=True, align='L')
        pdf.output(file_name)
        print("PDF report generated successfully.")
    except Exception as e:
        print(f"Error generating PDF report: {str(e)}")

# Main function
def main():
    data_file = "weather_data.csv"
    report_file = "weather_report.pdf"
    
    # Load weather data
    data = load_data(data_file)
    
    if data is not None:
        # Analyze weather patterns
        result = analyze_weather(data)
        
        if result is not None:
            avg_temp, avg_humidity, max_temp, min_temp, most_common_condition = result
            
            # Generate PDF report
            generate_report(report_file, avg_temp, avg_humidity, max_temp, min_temp, most_common_condition)

if __name__ == "__main__":
    main()