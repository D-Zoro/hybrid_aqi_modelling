"use client";

import { useState } from "react";

export default function TrainPage() {
  const [status, setStatus] = useState<string | null>(null);

  const triggerJob = async (endpoint: string) => {
    setStatus("Submitting...");
    await new Promise((resolve) => setTimeout(resolve, 500));
    setStatus(`Triggered ${endpoint}`);
  };

  return (
    <section className="space-y-6">
      <h1 className="text-2xl font-semibold">Training Operations</h1>
      <div className="grid gap-4 md:grid-cols-2">
        <button
          onClick={() => triggerJob("/training/train")}
          className="rounded bg-cyan-500 px-4 py-3 text-left font-medium text-cyan-950 hover:bg-cyan-400"
        >
          Run Daily Training
        </button>
        <button
          onClick={() => triggerJob("/training/retrain")}
          className="rounded bg-amber-500 px-4 py-3 text-left font-medium text-amber-950 hover:bg-amber-400"
        >
          Force Retraining
        </button>
      </div>
      <form className="rounded border border-slate-800 bg-slate-900 p-6">
        <h2 className="mb-4 text-lg font-medium">Upload Dataset</h2>
        <input type="file" className="text-sm text-slate-300" />
        <button
          type="submit"
          className="mt-4 rounded bg-emerald-500 px-4 py-2 text-sm font-medium text-emerald-900 hover:bg-emerald-400"
        >
          Upload
        </button>
      </form>
      {status && <p className="text-sm text-slate-300">{status}</p>}
    </section>
  );
}
