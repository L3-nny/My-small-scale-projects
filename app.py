import streamlit as st

# Define power consumption in watts for different appliances
power_consumption = {
    "shower": 5400,  # watts
    "bulbs": 20,     # watts total for two bulbs
    "speaker": 120,  # watts
    "shower_bulb": 10  # watts (used during shower)
}

# Initialize a list to store power usage over time
power_usage_history = []

# Function to calculate power usage in watts
def calculate_power_usage(time_in_shower, time_with_bulbs, time_with_speaker):
    total_shower_power = calculate_shower_power_usage(time_in_shower)
    total_power = (total_shower_power +
                   time_with_bulbs * power_consumption["bulbs"] +
                   time_with_speaker * power_consumption["speaker"])
    return total_power

# Function to calculate shower power usage, including shower bulb
def calculate_shower_power_usage(time_in_shower):
    shower_power = time_in_shower * power_consumption["shower"]
    shower_bulb_power = time_in_shower * power_consumption["shower_bulb"]
    total_shower_power = shower_power + shower_bulb_power
    return total_shower_power

# Function to convert power usage from watts to kilowatt-hours
def watts_to_kwh(watts):
    return watts * (1 / 1000)  # Convert watts to kWh

# Function to update remaining power in kWh
def update_remaining_power(used_power_kwh, initial_power):
    remaining_power = initial_power - used_power_kwh
    return remaining_power

# Streamlit App
def main():
    st.title("Power Usage Tracking System")

    # Input for time spent using each appliance (in minutes, converted to hours)
    time_in_shower = st.number_input("Enter time spent in the shower (minutes):", min_value=0.0, step=1.0) / 60
    time_with_bulbs = st.number_input("Enter time when bulbs are used (minutes):", min_value=0.0, step=1.0) / 60
    time_with_speaker = st.number_input("Enter time when speaker is used (minutes):", min_value=0.0, step=1.0) / 60

    # Initial power in kWh
    initial_power = st.number_input("Enter initial power available (kWh):", min_value=0.0, step=1.0, value=6.0)

    # Calculate total power usage in watts
    total_power_used_watts = calculate_power_usage(time_in_shower, time_with_bulbs, time_with_speaker)
    
    # Convert total power usage to kWh
    total_power_used_kwh = watts_to_kwh(total_power_used_watts)
    
    # Update remaining power
    remaining_power = update_remaining_power(total_power_used_kwh, initial_power)
    
    # Display total power used and remaining power
    st.write(f"Total power used: {total_power_used_kwh:.2f} kWh")
    
    # Remove the graph plotting section
    # Store the power usage and update initial power for tracking over time
    power_usage_history.append(total_power_used_kwh)

    # Add the colorful and elegant display for remaining power
    st.markdown(f"""
        <style>
            .remaining-power {{
                font-size: 36px;
                font-weight: bold;
                color: white;
                background-color: #4CAF50; /* Green background */
                padding: 20px;
                border-radius: 10px;
                text-align: center;
            }}
        </style>
        <div class="remaining-power">
            Remaining power: {remaining_power:.2f} kWh
        </div>
    """, unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
