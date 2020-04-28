from notification.views import index_greet, notification


def setup_routes(app):
    app.router.add_get('/great/', index_greet)
    app.router.add_post('/notification/', notification)
