import { useEffect, useState } from "react";
import { fetchSensors } from "../services/api";
import SensorCard from "../components/SensorCard";
import Chart from "../components/chart";

export default function Dashboard() {
  const [sensors, setSensors] = useState([]);
  const [chartData, setChartData] = useState([]);

  useEffect(() => {
    fetchSensors().then((data) => {
      setSensors(data);
      // Convert sensor data into chart format
      setChartData(
        data.map((sensor) => ({
          timestamp: sensor.last_updated,
          fill_ratio: sensor.current_fill / sensor.bin_capacity,
        }))
      );
    });
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Waste Bin Status</h2>
      <div className="grid grid-cols-3 gap-4">
        {sensors.map((sensor) => (
          <SensorCard key={sensor.id} sensor={sensor} />
        ))}
      </div>
      <div className="mt-6">
        <Chart data={chartData} />
      </div>
    </div>
  );
}
