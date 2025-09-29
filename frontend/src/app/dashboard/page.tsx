export default function DashboardPage() {
  return (
    <section className="space-y-6">
      <header className="flex items-center justify-between">
        <h1 className="text-2xl font-semibold">Operational Dashboard</h1>
        <span className="rounded bg-slate-800 px-3 py-1 text-xs uppercase tracking-wide text-slate-400">
          beta
        </span>
      </header>
      <div className="grid gap-6 md:grid-cols-3">
        <div className="rounded border border-slate-800 bg-slate-900 p-4">
          <h2 className="text-sm text-slate-400">Latest AQI</h2>
          <p className="text-3xl font-semibold text-emerald-400">118</p>
        </div>
        <div className="rounded border border-slate-800 bg-slate-900 p-4">
          <h2 className="text-sm text-slate-400">Model Version</h2>
          <p className="text-3xl font-semibold text-slate-100">model-v0</p>
        </div>
        <div className="rounded border border-slate-800 bg-slate-900 p-4">
          <h2 className="text-sm text-slate-400">Data Freshness</h2>
          <p className="text-3xl font-semibold text-amber-300">45 min</p>
        </div>
      </div>
      <section className="rounded border border-slate-800 bg-slate-900 p-6">
        <h2 className="mb-4 text-lg font-medium">Prediction Timeline</h2>
        <div className="h-60 rounded bg-slate-950/60" />
      </section>
    </section>
  );
}
