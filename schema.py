USER_CREATE = {
	"type": "object",
	"properties": {
		"title": {
			"type": "string"
		},
		"descriptions": {
			"type": "string",
		},
		"create_date": {
			"type": "string",
			"pattern": "^\d{4}-\d{2}-\d{2}$"
		},
		"owner": {
			"type": "integer"
		}
	},
	"required": ["title", "descriptions", "create_date", "owner"]
}