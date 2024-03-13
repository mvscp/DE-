from task1.shape import Circle, Triangle, calculate_area
from pyspark.sql import SparkSession
from task2.data import get_product_category_pairs

# Пример использования библиотеки
if __name__ == "__main__":
    # Создание экземпляров фигур
    circle = Circle(radius=5)
    triangle = Triangle(a=3, b=4, c=5)

    # Вычисление площади фигур без знания их типа в compile-time
    circle_area = calculate_area(circle)
    triangle_area = calculate_area(triangle)

    print("Площадь круга:", circle_area)
    print("Площадь треугольника:", triangle_area)

    # Выборка пар "Продукт - Категория"
    spark = SparkSession.builder \
        .appName("ProductCategoryPairs") \
        .getOrCreate()

    products_data = [(1, "product1"),
                     (2, "product2"),
                     (3, "product3")]
    products_columns = ["product_id", "product_name"]
    df_products = spark.createDataFrame(data=products_data, schema=products_columns)

    categories_data = [(1, "category1"),
                       (2, "category2"),
                       (3, "category3")]
    categories_columns = ["category_id", "category_name"]
    df_categories = spark.createDataFrame(data=categories_data, schema=categories_columns)

    products_categories_data = [(1, 2), (1, 1), (3, 2)]
    products_categories_columns = ["product_id", "category_id"]
    df_products_categories = spark.createDataFrame(data=products_categories_data, schema=products_categories_columns)

    product_category_pairs = get_product_category_pairs(df_products, df_categories, df_products_categories)

    print("Product-Category Pairs:")
    product_category_pairs.show()

    spark.stop()
