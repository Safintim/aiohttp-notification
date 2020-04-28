notification_request_scheme = {
    'type': 'object',
    'properties': {
        'user_ids': {
            'type': 'array',
            'items': {
                'type': 'number',
            },
        },
        'is_notification': {'type': 'boolean'},
        'is_message': {'type': 'boolean'},
        'title': {'type': 'string'},
        'body': {'type': 'string'},
        'typeEvent': {'type': 'string'},
    },
    'required': ['user_ids', 'title', 'body'],
}

notification_response_scheme = {
    'type': 'object',
    'properties': {
        'message': {
            'type': 'string',
        },
        'code': {
            'type': 'number',
        },
    },
}
