from django import template

register = template.Library()


def response_url(params):
    prepared = []

    for key, value in params.items():
        if type(value) == set:
            for item in value:
                prepared.append(f"{key}={item}")
        else:
            prepared.append(f"{key}={value}")

    return None if not params else "?" + "&".join(prepared)


@register.simple_tag
def append_params(*, request, start_with_unique="-", unique=True, **kwargs):
    """
    Append to already existed GET params new values or create list of elements.

    Examples:
        1. Use unique append:
            Current page is /?a=1&a=2&a=3.

            In template:
                {% append_params request=request a=4 %}
            Rendered:
                "?a=4"

        2. Use not-unqiue append (list):
            Current page is /?a=1&b=3&c=5.

            In template:
                {% append_params request=request unique=0 a=4 %}
            Rendered:
                "?a=1&b=3&c=5&a=4"

        3. If needed replace same keys use "start_with_unique". Smart replace for not unique keys:
            Current page is /?sort=name&sort=-date

            In template:
                {% append_params request=request sort="date" %}
            Rendered:
                "?sort=name&sort=date"

        4. Use "start_with_unique" with custom value:
            Current page is /?sort=abc

            In template:
                {% append_params request=request sort="abc" start_with_unique="+" %}
            Rendered:
                "?sort=+abc
    """
    params = {key: set(values) for (key, values) in request.GET.lists()}
    for key, value in kwargs.items():
        value = str(value)

        if not unique and key in params:
            if value in params[key]:
                params[key].remove(value)
                params[key].add(start_with_unique + value)
            elif (start_with_unique + value) in params[key]:
                params[key].remove(start_with_unique + value)
                params[key].add(value)
            else:
                params[key].add(value)
        else:
            params[key] = set([value] if type(value) in (str, int) else value)

    return response_url(params)


@register.simple_tag
def remove_params(*args, request, start_with_unique="-", **kwargs):
    """
    Remove from request.GET some keys.

    Examples:
        1. Remove simple key:
            Current page is /?per_page=10&sort=name&page=5

            In template:
                {% remove_params request=request sort=name %}
            Rendered:
                /?per_page=10&page=5

        2. Remove key with "start_with_unique":
            Current page is /?sort=abc&sort=-fge&sort=nmo

            In template:
                {% remove_params request=request sort="-fge" %}
            Rendered:
                /?sort=abc&sort=nmo

        3. Remove key without value:
            Current page is /?page=1&sort=name

            In template:
                {% remove_params request=request "page" %}
            Rendered:
                /?sort=name
    """
    params = {}

    for (key, values) in request.GET.lists():
        if key in args:
            pass
        elif key in kwargs or key[1:] in kwargs:
            params.setdefault(key, set(values))

            for value in values:
                if kwargs[key] == value or (start_with_unique + kwargs[key]) == value:
                    params[key].remove(value)
        else:
            params[key] = set(values)

    return response_url(params)


@register.filter
def to_list(obj, separator=" "):
    """
    Use string as list.

    Examples:
        1. Use with for loop:
            In template:
                {% for item in "1 2 3 4 5 6 7 8 9"|to_list %}
                    {{ item }}
                {% endfor %}
        2. Use custom separator:
            In template:
                {% for item in "1_2_3_4"|to_list:"_" %}
                    {{ item }}
                {% endfor %}
    """
    return obj.split(separator)


@register.filter
def get_list(obj, key):
    return obj.getlist(key)


@register.simple_tag
def list_position(*, request, key, value, start_with_unique="-"):
    """
    Return position from request.GET.getlist objects.

    Examples:
        1. Current page is /?sort=name&sort=created&sort=abc&sort=description:
            In template:
                {% list_position request=request key="sort" value="abc" %}
            Rendered:
                3
        2. Current page is /?sort=name&sort=created
            In template:
                {% list_position request=request key="sort" value="label" %}
            Rendered:
                ""
    """
    selected_list = request.GET.getlist(key)

    if (current_value := start_with_unique + value) and current_value in selected_list or (
            current_value := value) in selected_list:
        return selected_list.index(current_value) + 1
