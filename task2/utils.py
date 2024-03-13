from pyspark.sql import DataFrame

def get_product_category_pairs(products: DataFrame, categories: DataFrame, product_has_category: DataFrame) -> DataFrame:
    df_joined = products.join(product_has_category, on='product_id', how='left')
    pairs = df_joined.join(categories, on='category_id', how='left')
    return pairs.select('product_name', 'category_name')
