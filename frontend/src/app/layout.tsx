import "./globals.css";
import { ReactNode } from "react";

export const metadata = {
  title: "AiroSense",
  description: "Air quality insights and predictions",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-slate-950 text-slate-100">
        <header className="border-b border-slate-800 bg-slate-900/70 backdrop-blur">
          <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
            <span className="text-xl font-semibold">AiroSense</span>
            <nav className="flex gap-4 text-sm text-slate-300">
              <a href="/predict">Predict</a>
              <a href="/dashboard">Dashboard</a>
              <a href="/train">Training</a>
            </nav>
          </div>
        </header>
        <main className="mx-auto max-w-6xl px-6 py-10">{children}</main>
      </body>
    </html>
  );
}
