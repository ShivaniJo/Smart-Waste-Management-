import { useEffect, useState } from "react";
import Map, { Marker } from "react-map-gl";
import { fetchOptimizedRoutes } from "../services/api";

export default function WasteMap() {
  const [routes, setRoutes] = useState([]);

  useEffect(() => {
    fetchOptimizedRoutes().then(setRoutes);
  }, []);

  return (
    <Map
      initialViewState={{
        latitude: 37.7749,
        longitude: -122.4194,
        zoom: 12,
      }}
      mapboxAccessToken="YOUR_MAPBOX_API_KEY"
      mapStyle="mapbox://styles/mapbox/streets-v11"
      className="h-[400px] w-full"
    >
      {routes.map((route, index) => (
        <Marker key={index} latitude={route.latitude} longitude={route.longitude}>
          🗑️
        </Marker>
      ))}
    </Map>
  );
}
