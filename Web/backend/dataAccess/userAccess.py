from backend.coremodels.user_info import UserInfo
from backend.coremodels.cost_center import CostCenter
from django.contrib.auth.models import User, Group
from ..__init__ import dataAccessInjector as di
from rest_framework.authtoken.models import Token


@di.register(name="UserAccess")
class UserAccess():
    '''User access.'''

    def get_users() -> User:
        try:
            return UserInfo.objects.filter()
        except Exception:
            return None

    def create_user(username, password, barcode_id, nfc_id, cost_centers, group_id):
        try:
            # Have to add an mock email since this is required in the User auth model.
            new_user = User.objects.create_user(
                username=username, email='email@email.com', password=password)
            new_user.save()

            group = Group.objects.get(id=group_id)

            centers = CostCenter.objects.filter(id__in=cost_centers)

            new_user_info = UserInfo.objects.create(
                user=new_user, barcode_id=barcode_id, nfc_id=nfc_id, group=group)
            new_user_info.save()

            new_user_info.cost_center.add(*centers)
            return new_user_info
        except Exception:
            return None

    def get_user_with_barcode(barcode_id) -> User:
        '''Returns user corresponding to the sent in barcode id, 
        or None if user does not exist.'''
        try:
            return UserInfo.objects.filter(barcode_id=barcode_id).first()
        except Exception:
            return None

    def get_user_with_nfc(nfc_id) -> User:
        '''Returns user corresponding to the sent in nfc id, 
        or None if user does not exist.'''
        try:
            return UserInfo.objects.filter(nfc_id=nfc_id).first()
        except Exception:
            return None

    def get_user_cost_center(self, user: User) -> CostCenter:
        '''Return cost center of user.'''
        try:
            user_info = UserInfo.objects.get(user=user)
            cost_center = user_info.cost_center
            return cost_center
        except Exception:
            return None

    def create_auth_token(request):
        '''Creates and returns authentication token for user in request.'''
        try:
            token, created = Token.objects.get_or_create(user=request.user)
            return token.key
        except Exception:
            return None

    def get_user_info(user_id):
        try:
            return UserInfo.objects.filter(user=user_id).first()
        except Exception:
            return None

    def update_user(self, user_id, barcode_id, nfc_id, username,
                    password, cost_center, group):
        '''Updates the user info'''
        try:
            updated_user = self.get_user_info(user_id=user_id)
            django_user_model = User.objects.get(username=updated_user.user)
            if username is not None:
                django_user_model.username = username
            if password is not None:
                django_user_model.password = password
            django_user_model.save()
            updated_user = self.get_user_info(user_id=user_id)
            if barcode_id is not None:
                updated_user.barcode_id = barcode_id,
            if nfc_id is not None:
                updated_user.nfc_id = nfc_id
            if cost_center is not None:
                try:
                    new_cost_center = []
                    for cost_c in cost_center:
                        print(CostCenter.objects.filter(id=cost_c).first())
                        new_cost_center.append(
                            CostCenter.objects.filter(id=cost_c).first())
                    updated_user.cost_center.set(new_cost_center)
                except:
                    Exception
            if group is not None:
                try:
                    new_group = Group.objects.filter(id=group).first()
                    updated_user.group = new_group
                except:
                    Exception
            updated_user.save()
            return updated_user
        except Exception:
            return None

    def delete_user(self, user_id):
        '''Deletes user'''
        try:
            user = self.get_user_info(user_id)
            User.objects.filter(user=user).delete()
            return UserInfo.objects.filter(user=user_id).delete()
        except Exception:
            return None
