# Importing the PasswordResetTokenGenerator class from Django's authentication tokens module

from django.contrib.auth.tokens import PasswordResetTokenGenerator
# Importing the six library for compatibility between Python 2 and 3
import six

# Defining a custom token generator class that inherits from PasswordResetTokenGenerator
class TokenGenerator(PasswordResetTokenGenerator):
    # Overriding the _make_hash_value method to customize the token generation
    def _make_hash_value(self, user, timestamp):
        # Creating a hash value based on the user's primary key, the current timestamp, and the user's active status
        return (six.text_type(user.pk) + 
                six.text_type(timestamp) + 
                six.text_type(user.is_active))

# Creating an instance of the custom token generator
generate_token = TokenGenerator()

