# Insight Store
A simple insight store that saves and loads insights to and from a file system.

## Usage
1. Create an instance of the `InsightStore` class, passing in the directory where you want to store the insights.
2. Create an instance of the `Insight` class, passing in the title, creation date, last modified date, and data.
3. Call the `save_insight` method on the `InsightStore` instance, passing in the `Insight` instance.
4. Call the `load_insights` method on the `InsightStore` instance to retrieve a list of all saved insights.
5. Call the `delete_insight` method on the `InsightStore` instance, passing in the ID of the insight you want to delete.
6. Call the `duplicate_insight` method on the `InsightStore` instance, passing in the ID of the insight you want to duplicate.
