from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_confusion_matrix, create_model_input_table, preprocess_companies, preprocess_shuttles


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="companies",
                outputs=["companies_columns", "preprocessed_companies"],
                name="preprocess_companies_node",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocess_shuttles_node",
            ),
            node(
                func=create_model_input_table,
                inputs=["preprocessed_shuttles",
                        "preprocessed_companies", "reviews"],
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
            node(
                func=create_confusion_matrix,
                inputs="companies",
                outputs="confusion_matrix",
            ),
        ]
    )
