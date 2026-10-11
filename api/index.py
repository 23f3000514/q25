from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 151.15,
    "uptime_pct": 99.297,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 130.93,
    "uptime_pct": 97.599,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 133.4,
    "uptime_pct": 99.343,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 227.02,
    "uptime_pct": 98.207,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 157.89,
    "uptime_pct": 98.336,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 233.64,
    "uptime_pct": 99.42,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 143.3,
    "uptime_pct": 97.345,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 197.15,
    "uptime_pct": 98.533,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 147.92,
    "uptime_pct": 98.188,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 148.36,
    "uptime_pct": 98.976,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 201.25,
    "uptime_pct": 98.174,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 227.01,
    "uptime_pct": 97.144,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 182.77,
    "uptime_pct": 98.998,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 131.97,
    "uptime_pct": 98.904,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 207.02,
    "uptime_pct": 99.249,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 203.12,
    "uptime_pct": 98.627,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 196.87,
    "uptime_pct": 98.75,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 203.16,
    "uptime_pct": 97.164,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 206.14,
    "uptime_pct": 97.197,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 146.26,
    "uptime_pct": 98.869,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 118.23,
    "uptime_pct": 97.534,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 207.47,
    "uptime_pct": 98.847,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 163.6,
    "uptime_pct": 97.681,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 141.26,
    "uptime_pct": 97.132,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 164.59,
    "uptime_pct": 99.413,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 201.81,
    "uptime_pct": 99.356,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 144.78,
    "uptime_pct": 98.215,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 123.79,
    "uptime_pct": 98.36,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 142.97,
    "uptime_pct": 97.345,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 163.13,
    "uptime_pct": 98.467,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 195.55,
    "uptime_pct": 98.661,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 163.68,
    "uptime_pct": 97.942,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 120.7,
    "uptime_pct": 97.391,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 167.04,
    "uptime_pct": 98.564,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 204.72,
    "uptime_pct": 99.06,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 154.28,
    "uptime_pct": 98.296,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
