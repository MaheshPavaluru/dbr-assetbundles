import pipelines as pd

@pd.table
def transformed():
    return spark.range(10)