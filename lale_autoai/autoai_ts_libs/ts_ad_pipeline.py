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

from autoai_ts_libs.anomaly_detection.estimators.api.base import (  # type: ignore # noqa
    TSADPipeline as model_to_be_wrapped,
)

import lale.docstrings
import lale.operators


class _TSADPipelineImpl:
    def __init__(self, steps, **kwargs):
        self._wrapped_model = model_to_be_wrapped(
            steps=steps,
            **kwargs)

    def fit(self, X, y=None, **fit_params):
        self._wrapped_model.fit(X, y, **fit_params)
        return self

    def predict(self, X=None, **predict_params):
        return self._wrapped_model.predict(X, **predict_params)


_hyperparams_schema = {
    "allOf": [
        {
            "description": "This first object lists all constructor arguments with their types, but omits constraints for conditional hyperparameters.",
            "type": "object",
            "additionalProperties": True,
            "required": ["steps"],
            "relevantToOptimizer": [],
            "properties": {
                "steps": {
                    "description": "List of (name, transform) tuples (implementing fit/transform) that are chained, in the order in which they are chained, with the last object an estimator.",
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
            },
        }
    ]
}

_input_fit_schema = {
    "type": "object",
    "required": ["X"],
    "additionalProperties": False,
    "properties": {
        "X": {  # Handles 1-D arrays as well
            "anyOf": [
                {"type": "array", "items": {"laleType": "Any"}},
                {
                    "type": "array",
                    "items": {"type": "array", "items": {"laleType": "Any"}},
                },
            ]
        },
        "y": {"laleType": "Any"},
    },
}

_input_predict_schema = {
    "type": "object",
    "required": ["X"],
    "additionalProperties": False,
    "properties": {
        "X": {  # Handles 1-D arrays as well
            "anyOf": [
                {"type": "array", "items": {"laleType": "Any"}},
                {
                    "type": "array",
                    "items": {"type": "array", "items": {"laleType": "Any"}},
                },
            ]
        }
    },
}

_output_predict_schema = {
    "description": "Features; the outer array is over samples.",
    "anyOf": [
        {"type": "array", "items": {"laleType": "Any"}},
        {
            "type": "array",
            "items": {"type": "array", "items": {"laleType": "Any"}},
        },
    ],
}

_combined_schemas = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": """Operator from `autoai_ts_libs`_.
.. _`autoai_ts_libs`: https://pypi.org/project/autoai-ts-libs""",
    "documentation_url": "https://lale-autoai.readthedocs.io/en/latest/modules/lale_autoai.autoai_ts_libs.ts_ad_pipeline.html",
    "import_from": "autoai_ts_libs.anomaly_detection.estimators.api.base",
    "type": "object",
    "tags": {"pre": [], "op": ["classifer", "regressor", "estimator"], "post": []},
    "properties": {
        "hyperparams": _hyperparams_schema,
        "input_fit": _input_fit_schema,
        "input_predict": _input_predict_schema,
        "output_predict": _output_predict_schema,
    },
}

TSADPipeline = lale.operators.make_operator(_TSADPipelineImpl, _combined_schemas)
lale.docstrings.set_docstrings(TSADPipeline)
