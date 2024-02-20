<a name="readme-top"></a>


[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]




<br />
<div align="center">
  <a href="https://github.com/vasilm1/WeatherApp">
  </a>

<h3 align="center">Weather App</h3>

  <p align="center">
    Gathers Weather Data
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


[![Weather during Daytime][lightscreenshot]](https://cdn.discordapp.com/attachments/1100850066127863959/1209187017674596352/image.png?ex=65e6022a&is=65d38d2a&hm=100ad0a17e0259a8dae58d6a8c21ae24fbba54ea2f86f84d567f3051e4c5714b&)
[![Weather at Night][darkscreenshot]](https://cdn.discordapp.com/attachments/1045537111576694855/1209294253075857498/Light.png?ex=65e66609&is=65d3f109&hm=411a6f4948f772d2067347a24f5c0680300637edad0ba8d63322fa73128541e4&)

Simple WeatherApp which uses a free Weather API and GMAPS API.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Make sure you have Python 3.13+ installed.

### Prerequisites

* poetry
  ```sh
  pip install poetry
  ```

### Installation

1. Get a free API Keys at [Weather API](https://www.weatherapi.com/) and [Google API](https://developers.google.com/maps/documentation/javascript/get-api-key)
2. Clone the repo
   ```sh
   git clone https://github.com/vasilm1/WeatherApp.git
   ```
3. Install NPM packages
   ```sh
   pip install requirements.txt
   ```
4. Enter your API in `weather.py`
   ```py
   GMAP_API = 'YOUR GMAPS API'
   WEATHER_API = 'YOUR WEATHER API'
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this to find the weather in any area in the world by the search of an address/city.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/vasilm1/WeatherApp](https://github.com/vasilm1/WeatherApp)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/vasilm1/WeatherApp.svg?style=for-the-badge
[contributors-url]: https://github.com/vasilm1/WeatherApp/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/vasilm1/WeatherApp.svg?style=for-the-badge
[forks-url]: https://github.com/vasilm1/WeatherApp/network/members
[stars-shield]: https://img.shields.io/github/stars/vasilm1/WeatherApp.svg?style=for-the-badge
[stars-url]: https://github.com/vasilm1/WeatherApp/stargazers
[issues-shield]: https://img.shields.io/github/issues/vasilm1/WeatherApp.svg?style=for-the-badge
[issues-url]: https://github.com/vasilm1/WeatherApp/issues
[license-shield]: https://img.shields.io/github/license/vasilm1/WeatherApp.svg?style=for-the-badge
[license-url]: https://github.com/vasilm1/WeatherApp/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[lightscreenshot]: images/Light.png
[darkscreenshot]: images/Dark.png
