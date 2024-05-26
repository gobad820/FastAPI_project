<!--<script>-->
<!--    let weather = null;-->

<!--    // 사용자의 위치 정보를 가져옵니다.-->
<!--    navigator.geolocation.getCurrentPosition(position => {-->
<!--        const { latitude, longitude } = position.coords;-->

<!--        // OpenWeatherMap API를 호출합니다.-->
<!--        const weatherApiUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${import.meta.env.VITE_OPEN_WEATHER_MAP_API_KEY}`;-->

<!--        fetch(weatherApiUrl)-->
<!--            .then(response => response.json())-->
<!--            .then(data => {-->
<!--                // 날씨 정보를 저장합니다.-->
<!--                weather = {-->
<!--                    temperature: data.main.temp,-->
<!--                    description: data.weather[0].main-->
<!--                };-->
<!--            })-->
<!--            .catch(error => console.error('Error:', error));-->
<!--    }, error => {-->
<!--        console.error('Error:', error);-->
<!--    });-->
<!--</script>-->

<!--{#if weather}-->
<!--    <div class="card text-center">-->
<!--        <div class="card-header">-->
<!--            Current Weather-->
<!--        </div>-->
<!--        <div class="card-body">-->
<!--            <h5 class="card-title">Temperature: {(weather.temperature-273).toFixed(2)}°C</h5>-->
<!--            <p class="card-text">Description: {weather.description}</p>-->
<!--        </div>-->
<!--        <div class="card-footer text-muted">-->
<!--            Weather data provided by OpenWeatherMap-->
<!--        </div>-->
<!--    </div>-->
<!--{:else}-->
<!--    <div class="d-flex justify-content-center">-->
<!--        <div class="spinner-border" role="status">-->
<!--&lt;!&ndash;            <span class="sr-only"></span>&ndash;&gt;-->
<!--        </div>-->
<!--    </div>-->
<!--{/if}-->

<script>
    let weather = null;

    // 사용자의 위치 정보를 가져옵니다.
    navigator.geolocation.getCurrentPosition(position => {
        const { latitude, longitude } = position.coords;

        // OpenWeatherMap API를 호출합니다.
        const weatherApiUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${import.meta.env.VITE_OPEN_WEATHER_MAP_API_KEY}`;

        fetch(weatherApiUrl)
            .then(response => response.json())
            .then(data => {
                // 날씨 정보를 저장합니다.
                weather = {
                    temperature: data.main.temp,
                    description: data.weather[0].main
                };
            })
            .catch(error => console.error('Error:', error));
    }, error => {
        console.error('Error:', error);
    });

    // 날씨에 따른 이모티콘을 반환하는 함수
    function getWeatherEmoji(description) {
        switch (description.toLowerCase()) {
            case 'clear':
                return '☀️';
            case 'clouds':
                return '☁️';
            case 'rain':
                return '🌧️';
            // 추가적인 날씨 조건들...
            default:
                return '❓';
        }
    }
</script>

{#if weather}
    <div class="card text-center">
        <div class="card-header">
            Current Weather {getWeatherEmoji(weather.description)}
        </div>
        <div class="card-body">
            <h5 class="card-title">Temperature: {(weather.temperature-273.15).toFixed(2)}°C</h5>
            <p class="card-text">Description: {weather.description}</p>
        </div>
        <div class="card-footer text-muted">
            Weather data provided by OpenWeatherMap
        </div>
    </div>
{:else}
    <div class="d-flex justify-content-center">
        <div class="spinner-border" role="status">
        </div>
    </div>
{/if}