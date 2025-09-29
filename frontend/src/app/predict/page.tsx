"use client";

import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import axios from "axios";

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export default function PredictPage() {
  const [lat, setLat] = useState(28.6139);
  const [lon, setLon] = useState(77.2090);
  const [result, setResult] = useState<any>(null);

  const predictMutation = useMutation({
    mutationFn: async () => {
      const payload = {
        coordinates: { latitude: lat, longitude: lon },
        timestamp_utc: new Date().toISOString(),
        horizon_hours: 1,
        include_explanations: true,
      };
      const res = await axios.post(`${API_BASE}/api/v1/predictions/predict`, payload);
      return res.data;
    },
    onSuccess: (data) => setResult(data),
  });

  return (
    <section className="space-y-6">
      <h1 className="text-2xl font-semibold">Predict AQI</h1>
      <div className="flex flex-col gap-4 md:flex-row">
        <label className="flex flex-1 flex-col gap-2 text-sm">
          Latitude
          <input
            className="rounded border border-slate-700 bg-slate-900 px-3 py-2"
            type="number"
            step="0.0001"
            value={lat}
            onChange={(e) => setLat(Number(e.target.value))}
          />
        </label>
        <label className="flex flex-1 flex-col gap-2 text-sm">
          Longitude
          <input
            className="rounded border border-slate-700 bg-slate-900 px-3 py-2"
            type="number"
            step="0.0001"
            value={lon}
            onChange={(e) => setLon(Number(e.target.value))}
          />
        </label>
      </div>
      <button
        onClick={() => predictMutation.mutate()}
        className="rounded bg-emerald-500 px-4 py-2 text-sm font-medium text-emerald-900 hover:bg-emerald-400"
      >
        {predictMutation.isPending ? "Predicting..." : "Predict"}
      </button>
      {result && (
        <pre className="rounded border border-slate-700 bg-slate-900 p-4 text-xs text-slate-200">
{JSON.stringify(result, null, 2)}
        </pre>
      )}
    </section>
  );
}
