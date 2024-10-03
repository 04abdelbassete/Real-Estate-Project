class ListingRouter:
    """A router to control all database operations on models in the listings application. """

    route_app_labels = {'listings',}

    def db_for_read(self, model, **hints):
        """
        Attempts to read listings
        """
        if model._meta.app_label in self.route_app_labels:
            return "listings"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write listings
        """
        if model._meta.app_label in self.route_app_labels:
            return "listings"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the listings app is
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
        Make sure the listings app only appears in the
        'listings' database.
        """
        if app_label in self.route_app_labels:
            return db == "listings"
        return None

class PayPalRouter:
    route_app_labels = {'paypal_ipn'}

    def db_for_read(self, model, **hints):
        """Direct read operations for PayPal IPN to the 'paypal_ipn'."""
        if model._meta.db_table == 'paypal_ipn':
            return 'paypal_ipn'  # The name of your PayPal database
        return None

    def db_for_write(self, model, **hints):
        """Direct write operations for PayPal IPN to the 'paypal_ipn'."""
        if model._meta.db_table == 'paypal_ipn':
            return 'paypal_ipn'  # The name of your PayPal database
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in the PayPal IPN is involved."""
        if obj1._meta.db_table == 'paypal_ipn' or obj2._meta.db_table == 'paypal_ipn':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure PayPal IPN migration is applied only on the 'paypal_ipn'."""
        if app_label == 'paypal_ipn':
            return db == 'paypal_ipn'
        return None
