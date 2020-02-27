import graphene
from graphene_django.types import DjangoObjectType
from .models import Permission, Role, User, Case

''' Types '''
class PermissionType(DjangoObjectType):
    class Meta:
        model = Permission

class RoleType(DjangoObjectType):
	class Meta:
		model = Role

class UserType(DjangoObjectType):
	class Meta:
		model = User
		exclude = ('user_status',)
		convert_choices_to_enum  =  False
	user_status = graphene.String()
	def resolve_user_status(self, info):
		return self.user_get_status()

class CaseType(DjangoObjectType):
    class Meta:
        model = Case
        exclude = ('case_status',)
        convert_choices_to_enum  =  False
    case_status = graphene.String()
    def resolve_case_status(self, info):
        return self.case_get_status()


''' Inputs '''
class PermissionInput(graphene.InputObjectType):
	perm_name = graphene.String()

class RoleInput(graphene.InputObjectType):
	role_name = graphene.String()
	role_description = graphene.String()

class UserInput(graphene.InputObjectType):
	user_user = graphene.String()
	user_password = graphene.String()
	user_status = graphene.Int()


''' Query '''
class Query(object):
    all_permissions = graphene.List(PermissionType)
    all_roles       = graphene.List(RoleType)
    all_users       = graphene.List(UserType)
    all_cases       = graphene.List(CaseType)
    permission = graphene.Field(PermissionType, id=graphene.Int(), perm_name=graphene.String())
    role       = graphene.Field(RoleType, id=graphene.Int(), role_name=graphene.String())
    user       = graphene.Field(UserType, id=graphene.Int(), user_user=graphene.String())

    def resolve_all_permissions(self, info, **kwargs):
        return Permission.objects.all()

    def resolve_all_roles(self, info, **kwargs):
        return Role.objects.all()

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_cases(self, info, **kwargs):
        return Case.objects.all()

    def resolve_permission(self, info, **kwargs):
    	id = kwargs.get('id')
    	name = kwargs.get('perm_name')
    	if id is not None:
    		return Permission.Objects.get(pk=id)
    	if name is not None:
    		return Permission.Objects.get(perm_name=name)
    	return None

    def resolve_role(self, info, **kwargs):
    	id = kwargs.get('id')
    	name = kwargs.get('role_name')
    	if id is not None:
    		return Role.Objects.get(pk=id)
    	if name is not None:
    		return Role.Objects.get(role_name=name)
    	return None

    def resolve_user(self, info, **kwargs):
    	id = kwargs.get('id')
    	name = kwargs.get('user_user')
    	if id is not None:
    		return User.Objects.get(pk=id)
    	if name is not None:
    		return User.Objects.get(user_user=name)
    	return None


''' Mutations '''
