# from genericpath import exists
# from django.conf import settings
from backend.coremodels.transaction import Transaction

from django.contrib.auth.models import User
from backend.__init__ import serviceInjector as si
# from ..__init__ import dataAccessInjector as di
from django.contrib.auth.backends import BaseBackend
from backend.dataAccess.userAccess import UserAccess


@si.register()
class UserService(BaseBackend):
    '''User service.'''

    def get_users(self):
        return UserAccess.get_users()

    def get_user_with_barcode(self, barcode_id):
        '''Calls the access layer to get the user with the specified barcode id'''
        return UserAccess.get_user_with_barcode(barcode_id)

    def get_user_with_nfc(self, nfc_id):
        '''Calls the access layer to get the user with the specified nfc id'''
        return UserAccess.get_user_with_nfc(nfc_id)

    def create_auth_token(self, request):
        '''Calls the access layer to create an auth token'''
        return UserAccess.create_auth_token(request=request)

    def get_all_transactions_by_user(self, current_user) -> dict:
        '''Return every transaction made by user.'''
        user_convert = list(current_user)
        all_transactions = Transaction.objects.filter(
            by_user=user_convert[0]).all().values()

        return all_transactions

    def get_user_info(self, user_id):
        '''Calls access layer and returns user info for specified user_id'''
        return UserAccess.get_user_info(user_id)
