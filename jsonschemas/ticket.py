TICKET_TOPIC_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "type": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "properties": {
            "type": "object",
            "properties": {
                "ask": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "description"
                    ]
                },
                "bid": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "description"
                    ]
                },
                "last": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "description"
                    ]
                },
                "pre": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "description"
                    ]
                },
                "open": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "description"
                    ]
                },
                "qualityId": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "enum": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        }
                    },
                    "required": [
                        "type",
                        "description",
                        "enum"
                    ]
                }
            },
            "required": [
                "ask",
                "bid",
                "last",
                "pre",
                "open",
                "qualityId"
            ]
        },
        "required": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                }
            ]
        }
    },
    "required": [
        "title",
        "type",
        "description",
        "properties",
        "required"
    ]
}
