import os

profiling_enabled = os.environ.get("DD_PROFILING_ENABLED", "true") == "true"
if profiling_enabled:
    print("Starting profiler")

    from ddtrace.profiling import Profiler
    prof = Profiler()
    prof.start()

import faulthandler

faulthandler.enable()

import pandas as pd


def predict(i):
    print(f"Run {i}")

    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    df2 = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    df.merge(df2)


for i in range(1, 5000):
    predict(i)
