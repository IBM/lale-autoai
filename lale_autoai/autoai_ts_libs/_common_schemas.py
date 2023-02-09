# Copyright 2023 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict

JSON_TYPE = Dict[str, Any]


def get_schema_feature_columns(default=[0]) -> JSON_TYPE:
    return {
        "description": """Column indices for columns to be included as features in the model.""",
        "anyOf": [
            {"type": "array", "items": {"type": "integer", "minimum": 0}},
            {"enum": [-1], "description": ""}
        ],
        "default": default,
    }


schema_feature_columns: JSON_TYPE = get_schema_feature_columns()


def get_schema_target_columns(default=[0]) -> JSON_TYPE:
    return {
        "description": """Column indices for columns to be forecasted.""",
        "anyOf": [
            {"type": "array", "items": {"type": "integer", "minimum": 0}},
            {"enum": [-1], "description": ""}
        ],
        "default": default,
    }


schema_target_columns: JSON_TYPE = get_schema_target_columns()


def get_schema_time_column(default=-1) -> JSON_TYPE:
    return {
        "description": "Column index for column containing timestamps for the time series data.",
        "anyOf": [
            {"type": "integer", "minimum": 0, "description": "Index of timestamps column"},
            {"enum": [-1], "description": "No timestamps column specified"}
        ],
        "default": default,
    }


schema_time_column: JSON_TYPE = get_schema_time_column()


def get_schema_lookback_win(default=1) -> JSON_TYPE:
    return {
        "description": "The number of time points to include in the generated feature windows.",
        "type": "integer",
        "minimum": 1,
        "default": default,
    }


schema_lookback_win: JSON_TYPE = get_schema_lookback_win()


schema_store_lookback_history: JSON_TYPE = {
    "description": "Whether the last lookback window should be stored in the model.",
    "type": "boolean",
    "default": True,
}

schema_distance_metric: JSON_TYPE = {
    "description": "The distance metric to be used at the final estimator stage of the pipeline",
    "enum": [
        "mse",
        "euclidean",
        "logdet",
        "riemannian",
        "kullback",
        "Mahalanobis_Distance",
        "min"
    ],
    "default": "mse",
}

schema_observation_window: JSON_TYPE = {
    "description": "Observation window is used to compute anomaly scores by specified scoring_method",
    "type": "integer",
    "default": 10,
}

schema_scoring_method: JSON_TYPE = {
    "description": """Anomaly scoring method to compute anomaly score in specified mathematical,
    or statistical method. The computed score is used to label anomalies by
    analyzing residuals computed. Defaults to Chi-Square.""",
    "enum": [
        "iid",
        "Contextual-Anomaly",
        "Chi-Square",
        "Q-Score",
        "Sliding-Window",
        "Adaptive-Sliding-Window",
        'otsu', 'otsu_label', 'otsu_oneshot_label',
        'contamination', 'contamination_oneshot_label', 'contamination_label',
        'adaptivecontamination', 'adaptivecontamination_label', 'adaptivecontamination_oneshot_label',
        'qfunction', 'qfunction_oneshot_label', 'qfunction_label',
        'medianabsolutedev', 'medianabsolutedev_label', 'medianabsolutedev_oneshot_label',
        'std', 'std_oneshot_label', 'std_label',
        'max', 'max_oneshot_label', 'max_label'
    ],
    "default": "otsu_label",
}


schema_scoring_threshold: JSON_TYPE = {
    "description": "Scoring threshold is used to label computed anomaly score as anomaly or normal.",
    "type": "integer",
    "default": 2,
}


def get_schema_pred_win(default=0) -> JSON_TYPE:
    return {
        "description": "The number of time points to include in the generated target windows.",
        "type": "integer",
        "default": default,
    }


def get_schema_two_steps(default: str) -> JSON_TYPE:
    return {
        "description": "List of (name, transform) tuples (implementing fit/transform) that are chained, in the order in which they are chained, with the last object an estimator.",
        "anyOf": [
            {
                "type": "array",
                "items": {
                    "description": "Tuple of (name, transform).",
                    "type": "array",
                    "laleType": "tuple",
                    "minItems": 2,
                    "maxItems": 2,
                    "items": [
                        {"description": "Name.", "type": "string"},
                        {
                            "anyOf": [
                                {
                                    "description": "Transform.",
                                    "laleType": "operator",
                                },
                                {
                                    "description": "NoOp",
                                    "enum": [None, "passthrough"],
                                },
                            ]
                        },
                    ],
                },
            },
            {
                "enum": [None],
                "description": default,
            },
        ],
        "default": None,
    }


