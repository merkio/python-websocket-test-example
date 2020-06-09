INSTRUMENT_TOPIC_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "active": {
            "type": "boolean"
        },
        "exchangeIds": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                },
                {
                    "type": "string"
                }
            ]
        },
        "exchanges": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "slug": {
                            "type": "string"
                        },
                        "active": {
                            "type": "boolean"
                        },
                        "nameAtExchange": {
                            "type": "string"
                        },
                        "symbolAtExchange": {
                            "type": "string"
                        },
                        "firstSeen": {
                            "type": "integer"
                        },
                        "lastSeen": {
                            "type": "integer"
                        },
                        "firstTradingDay": {
                            "type": "null"
                        },
                        "lastTradingDay": {
                            "type": "null"
                        },
                        "tradingTimes": {
                            "type": "null"
                        }
                    },
                    "required": [
                        "slug",
                        "active",
                        "nameAtExchange",
                        "symbolAtExchange",
                        "firstSeen",
                        "lastSeen",
                        "firstTradingDay",
                        "lastTradingDay",
                        "tradingTimes"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "slug": {
                            "type": "string"
                        },
                        "active": {
                            "type": "boolean"
                        },
                        "nameAtExchange": {
                            "type": "string"
                        },
                        "symbolAtExchange": {
                            "type": "string"
                        },
                        "firstSeen": {
                            "type": "integer"
                        },
                        "lastSeen": {
                            "type": "integer"
                        },
                        "firstTradingDay": {
                            "type": "null"
                        },
                        "lastTradingDay": {
                            "type": "null"
                        },
                        "tradingTimes": {
                            "type": "null"
                        }
                    },
                    "required": [
                        "slug",
                        "active",
                        "nameAtExchange",
                        "symbolAtExchange",
                        "firstSeen",
                        "lastSeen",
                        "firstTradingDay",
                        "lastTradingDay",
                        "tradingTimes"
                    ]
                }
            ]
        },
        "dividends": {
            "type": "array",
            "items": {}
        },
        "splits": {
            "type": "array",
            "items": {}
        },
        "cfi": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "typeId": {
            "type": "string"
        },
        "wkn": {
            "type": "string"
        },
        "legacyTypeChar": {
            "type": "string"
        },
        "isin": {
            "type": "string"
        },
        "priceFactor": {
            "type": "integer"
        },
        "shortName": {
            "type": "string"
        },
        "homeSymbol": {
            "type": "string"
        },
        "intlSymbol": {
            "type": "string"
        },
        "homeNsin": {
            "type": "string"
        },
        "tags": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "id": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "icon": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "id",
                        "name",
                        "icon"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "id": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "icon": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "id",
                        "name",
                        "icon"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "id": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "icon": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "id",
                        "name",
                        "icon"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "id": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "icon": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "id",
                        "name",
                        "icon"
                    ]
                }
            ]
        },
        "derivativeProductCategories": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                },
                {
                    "type": "string"
                }
            ]
        },
        "company": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "ipoDate": {
                    "type": "null"
                }
            },
            "required": [
                "name",
                "description",
                "ipoDate"
            ]
        },
        "marketCap": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string"
                },
                "currencyId": {
                    "type": "null"
                }
            },
            "required": [
                "value",
                "currencyId"
            ]
        },
        "lastDividend": {
            "type": "null"
        },
        "shareType": {
            "type": "string"
        },
        "custodyType": {
            "type": "string"
        },
        "kidRequired": {
            "type": "boolean"
        },
        "kidLink": {
            "type": "null"
        },
        "tradable": {
            "type": "boolean"
        },
        "fundInfo": {
            "type": "null"
        },
        "derivativeInfo": {
            "type": "null"
        },
        "targetMarket": {
            "type": "object",
            "properties": {
                "investorType": {
                    "type": "null"
                },
                "investorExperience": {
                    "type": "null"
                }
            },
            "required": [
                "investorType",
                "investorExperience"
            ]
        },
        "savable": {
            "type": "boolean"
        },
        "fractionalTradingAllowed": {
            "type": "boolean"
        },
        "issuer": {
            "type": "null"
        }
    },
    "required": [
        "active",
        "exchangeIds",
        "exchanges",
        "dividends",
        "splits",
        "cfi",
        "name",
        "typeId",
        "wkn",
        "legacyTypeChar",
        "isin",
        "priceFactor",
        "shortName",
        "homeSymbol",
        "intlSymbol",
        "homeNsin",
        "tags",
        "derivativeProductCategories",
        "company",
        "marketCap",
        "lastDividend",
        "shareType",
        "custodyType",
        "kidRequired",
        "kidLink",
        "tradable",
        "fundInfo",
        "derivativeInfo",
        "targetMarket",
        "savable",
        "fractionalTradingAllowed",
        "issuer"
    ]
}
