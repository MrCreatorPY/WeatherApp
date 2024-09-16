import requests  # type: ignore
import streamlit as st

key = st.secrets["api_key"][0]



def GetWeather(city):
    url = f"http://api.weatherapi.com/v1/current.json?q={city}&key={key}"
    response = requests.get(url)

    if response.status_code == 200:
        print(response.json())
        data = response.json()
        region = data["location"]["region"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        condt = data["current"]["condition"]["text"]
        wind = data["current"]["wind_kph"]
        humidity = data["current"]["humidity"]
        rain = data["current"]["precip_in"]

        img = data["current"]["condition"]["icon"]
        img_url = f'https:{img}?'

        image = requests.get(img_url)

        if image.status_code != 200:
            print("Failed to download image!")
            exit()

        filename = "gg.png" # You can name the file as you want
        with open(filename, 'wb') as file:
            file.write(image.content)

        print("Image downloaded successfull")

        return [temp, wind, humidity, rain, condt, country, region]

    else:
        print("Error fetching weather data")
        return None




st.title("Weather App!")

st.markdown(
    """
<style>
.big-font {
    font-size:35px !important;
}
</style>
""",
    unsafe_allow_html=True,
)


(
    col1,
    col2,
) = st.columns(2)

city = col1.text_input("ENTER A CITY NAME", key="city")

data_list = GetWeather(city)
if data_list:
    temp = data_list[0]
    wind = data_list[1]
    humidity = data_list[2]
    rain = data_list[3]
    condt = data_list[4]
    country = data_list[5]
    region = data_list[6]

    col2.write(f"Country -: {country}")
    col2.write(f"Region -: {region}")

    col1.markdown(f'<p class="big-font">Weather</p>', unsafe_allow_html=True)
    col2.markdown(f'<p class="big-font">{condt}</p>', unsafe_allow_html=True)

    col1.markdown(f'<p class="big-font">Temperature</p>', unsafe_allow_html=True)
    col2.markdown(f'<p class="big-font">{temp}°C</p>', unsafe_allow_html=True)

    col1.markdown(f'<p class="big-font">Wind Speed</p>', unsafe_allow_html=True)
    col2.markdown(f'<p class="big-font">{wind} KPH</p>', unsafe_allow_html=True)

    col1.markdown(f'<p class="big-font">Humidity</p>', unsafe_allow_html=True)
    col2.markdown(f'<p class="big-font">{humidity} %</p>', unsafe_allow_html=True)

    col1.markdown(f'<p class="big-font">Rainfall</p>', unsafe_allow_html=True)
    col2.markdown(f'<p class="big-font">{rain} in</p>', unsafe_allow_html=True)

    #col3, col4 = col2.columns(2)
    col2.image("gg.png")