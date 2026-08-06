"""TEST-only factory helpers — synthetic codes only, not Nelna operational data."""

from __future__ import annotations

from apps.access_control.models import Role
from apps.access_control.services import assign_role, create_role
from apps.accounts.models import User
from apps.accounts.validators import normalize_employee_code
from apps.organizations.models import Department, Organization, Site
from apps.organizations.services import create_department, create_organization, create_site
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


def make_user(
    *,
    employee_code: str = "TST001",
    password: str = "Complex-Test-Pass-123!",
    is_active: bool = True,
    is_superuser: bool = False,
    is_staff: bool = False,
    must_change_password: bool = False,
) -> User:
    code = normalize_employee_code(employee_code)
    if is_superuser:
        user = User.objects.create_superuser(username=code, password=password)
        user.employee_code = code
        user.save(update_fields=["employee_code"])
    else:
        user = User.objects.create_user(
            username=code,
            password=password,
            employee_code=code,
            is_active=is_active,
            is_staff=is_staff,
        )
    if must_change_password:
        user.must_change_password = True
        user.save(update_fields=["must_change_password"])
    return user


def make_org(*, code: str = "ORGTEST1", name: str = "Test Organization 1") -> Organization:
    return create_organization(code=code, name=name)


def make_site(
    organization: Organization,
    *,
    code: str = "SITETEST1",
    name: str = "Test Site 1",
) -> Site:
    return create_site(organization=organization, code=code, name=name)


def make_department(
    organization: Organization,
    *,
    code: str = "DEPTTEST1",
    name: str = "Test Department 1",
    site: Site | None = None,
) -> Department:
    return create_department(
        organization=organization,
        code=code,
        name=name,
        site=site,
    )


def make_permission(
    *,
    codename: str = "test_permission",
    name: str = "Test permission",
) -> Permission:
    ct = ContentType.objects.get_for_model(User)
    permission, _ = Permission.objects.get_or_create(
        content_type=ct,
        codename=codename,
        defaults={"name": name},
    )
    return permission


def make_role_with_permission(
    *,
    code: str = "ROLETEST1",
    name: str = "Test Role 1",
    permission: Permission | None = None,
) -> Role:
    perm = permission or make_permission()
    role = create_role(code=code, name=name, permissions=[perm])
    return role


def grant_role(
    user: User,
    role: Role,
    *,
    organization: Organization | None = None,
    site: Site | None = None,
    department: Department | None = None,
) -> object:
    return assign_role(
        user=user,
        role=role,
        organization=organization,
        site=site,
        department=department,
    )
