export default function HomePage() {
  return (
    <section className="space-y-6">
      <h1 className="text-3xl font-semibold">Welcome to AiroSense</h1>
      <p className="max-w-2xl text-slate-300">
        Explore air pollution forecasts, manage model training jobs, and monitor system health from a single unified interface.
      </p>
      <div className="grid gap-4 md:grid-cols-3">
        <a href="/predict" className="rounded-lg border border-slate-800 bg-slate-900 p-4">
          <h2 className="text-xl font-medium">Predict</h2>
          <p className="text-sm text-slate-400">Generate on-demand AQI predictions for any coordinate.</p>
        </a>
        <a href="/dashboard" className="rounded-lg border border-slate-800 bg-slate-900 p-4">
          <h2 className="text-xl font-medium">Dashboard</h2>
          <p className="text-sm text-slate-400">Visualize trends, monitor model metrics, and inspect data health.</p>
        </a>
        <a href="/train" className="rounded-lg border border-slate-800 bg-slate-900 p-4">
          <h2 className="text-xl font-medium">Training</h2>
          <p className="text-sm text-slate-400">Upload new data, trigger retraining, and inspect model versions.</p>
        </a>
      </div>
    </section>
  );
}
