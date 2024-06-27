# python-weather-cli

A command line weather app. 

This project uses a Python virtual environment to manage its dependencies and integrates with the OpenWeather API.

## Features
- Fetch current weather information for a specified location (with longitude and latitude coordinates)
- Display low, high, and current temperatures
- Support for multiple locations

## Planned Features
- Display weather forecasts for the next few days.
- Allow users to set and save their preferred locations.
- Implement error handling for network issues and invalid API responses (current only assumes the former).

## Prerequisites

- Python installed on your machine. [Download Python](https://www.python.org/downloads/)
- Visual Studio Code installed. [Download VSCode](https://code.visualstudio.com/)
- An OpenWeather API key. [OpenWeather](https://openweathermap.org/)
    - Note: the API key may take a few hours to get approved

## Setting Up the Virtual Environment

1. **Clone the Repository**

   ```sh
   git clone https://github.com/notexploiting/python-weather-cli
   cd python-weather-cli
   ```
2. **Create a Virtual Environment**
Open the terminal in VSCode. Run the following command to create a virtual environment:

    ```sh
    python -m venv weather_venv
    ```

    `weather_venv` can be any names you desire for the virtual environment

3. **Activate the virtual environment**

    *On Windows*

    ```sh
    myenv\Scripts\activate
    ```

    *On macOS and Linux*
    
    ```sh
    source myenv/bin/activate
    ```

4. **Install Required Packages**

    With the virtual environment activated, install the required packages using pip:

    ```sh
    pip install -r requirements.txt
    ```

    If `requirements.txt` does not exist, you can install packages individually, e.g., `pip install requests`, and then generate `requirements.txt` by running:

    ```sh
    pip freeze > requirements.txt
    ```

To deactivate the virtual environment, simply run:

```sh
deactivate
```

## Usage Example
Here's an example of how to fetch the temperatures for Toronto:

Add this line to the end of `weather.py`:

```py
my_city = City("New York City", 40.7128, -74.0060, "imperial")
my_city.temp_print()
```

Then run the file with the 'Run and Debug' button.

Note: when running your file, you may notice that sometimes the temperatures are all the same. This is an error raised by an invalid coordinate set. To fix this, double-check with [LatLong.net](https://www.latlong.net/).

## Acknowledgements

- The weather data in this project is provided by the OpenWeather API.
- Special thanks to [Nick Walter's 'Intermediate Python for Non-Programmers' course on Linkedin Learning](https://www.linkedin.com/learning/instructors/nick-walter?u=76812730) for teaching some cool Python tools.

## Contact

For questions, suggestions, or support, you can reach out to me at [notexploiting@gmail.com](mailto:notexploiting@gmail.com)

Feel free to contribute to this project by creating issues or pull requests.