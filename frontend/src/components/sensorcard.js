export default function SensorCard({ sensor }) {
    return (
      <div className="bg-white p-4 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold">{sensor.location}</h3>
        <p>Current Fill: {sensor.current_fill} / {sensor.bin_capacity}</p>
        <p>Last Updated: {new Date(sensor.last_updated).toLocaleString()}</p>
      </div>
    );
  }
  