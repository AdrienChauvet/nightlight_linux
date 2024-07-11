import subprocess
import time

def set_night_light(enabled, display_name="eDP", brightness_level=0.5):  # Default brightness is 50%
    # Adjust these values based on your preference
    night_light_color = (1.00, 0.85, 0.60)  # RGB values for a warm color with reduced blue component
    transition_duration = 1  # seconds

    if enabled:
        # Adjust the color temperature using xrandr
        command = f"xrandr --output {display_name} --gamma {night_light_color[0]}:{night_light_color[1]}:{night_light_color[2]}"
        subprocess.run(command, shell=True)

        # Adjust the brightness using xrandr
        command = f"xrandr --output {display_name} --brightness {brightness_level}"
        subprocess.run(command, shell=True)

        time.sleep(transition_duration)  # Wait for the transition

    else:
        # Reset to the default color temperature
        command = f"xrandr --output {display_name} --gamma 1:1:1"
        subprocess.run(command, shell=True)

        # Reset to the default brightness
        command = f"xrandr --output {display_name} --brightness 1.0"  # Default brightness is 100%
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    # set enable to False, save the file, then run the script again to disable it.
    set_night_light(enabled=True, brightness_level=0.3)  # Set brightness between 0.15 and 1.
