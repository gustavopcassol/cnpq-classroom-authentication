import { useEffect, useState } from "react";
import "./App.css";

function App(): JSX.Element {
  const [latitude, setLatitude] = useState(0);
  const [longitude, setLongitude] = useState(0);
  const [accuracy, setAccuracy] = useState(0);
  const [ip, setIp] = useState("");

  useEffect(() => {
    (async () => {
      const response = await fetch("https://api64.ipify.org");
      setIp(await response.text());
    })();
  }, []);

  function positionCallback(position: GeolocationPosition): void {
    setLatitude(position.coords.latitude);
    setLongitude(position.coords.longitude);
    setAccuracy(position.coords.accuracy);
  }

  function positionErrorCallback(
    positionError: GeolocationPositionError
  ): void {
    console.warn(`ERROR(${positionError.code}): ${positionError.message}`);
  }

  const positionOptions = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0,
  };

  navigator.geolocation.getCurrentPosition(
    positionCallback,
    positionErrorCallback,
    positionOptions
  );

  return (
    <div className="App">
      <header className="App-header">
        <p>IP: {ip}</p>
        <p>-</p>
        <p>Latitude: {latitude}</p>
        <p>Longitude: {longitude}</p>
        <p>Accuracy: {accuracy}</p>
        <a
          className="App-link"
          href={`https://www.google.com/maps/search/?api=1&query=${latitude},${longitude}`}
          target="_blank"
          rel="noreferrer"
        >
          See in Maps
        </a>
      </header>
    </div>
  );
}

export default App;
