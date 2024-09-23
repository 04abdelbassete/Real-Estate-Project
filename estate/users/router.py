class AuthRouter:
    """A router to control all database operations on models in the
    users and contenttypes applications. """

    route_app_labels = {'users', 'admin', 'contenttypes', 'sessions', 'auth', 'account', 'socialaccount'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read users
        """
        if model._meta.app_label in self.route_app_labels:
            return "users"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write users
        """
        if model._meta.app_label in self.route_app_labels:
            return "users"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the users app is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the users app only appears in the
        'users' database.
        """
        if app_label in self.route_app_labels:
            return db == "users"
        return None
