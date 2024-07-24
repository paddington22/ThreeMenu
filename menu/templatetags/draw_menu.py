from django import template
from menu.models import Item


register = template.Library()


@register.inclusion_tag("menu/draw_menu.html", takes_context=True)
def draw_menu(context, menu):
    context["menu"] = menu

    items = Item.objects.filter(menu__title=menu)
    item_values = items.values()
    super_parents = [item for item in item_values.filter(parent=None)]

    try:
        selected_item = items.get(id=context['request'].GET[menu])
        opened_items = get_opened_items(selected_item)
        for parent in super_parents:
            if parent['id'] in opened_items:
                parent['child_items'] = get_child_items(item_values, parent['id'], opened_items)
        context["items"] = super_parents
    except:
        print('gege')
        context["items"] = super_parents

    return context


def get_opened_items(child):
    opened_items_id_list = []
    while child:
        opened_items_id_list.append(child.id)
        child = child.parent
    return opened_items_id_list


def get_child_items(item_values, current_parent_id, opened_items):
    current_parent_child_list = [item for item in item_values.filter(parent_id=current_parent_id)]

    for child in current_parent_child_list:
        if child['id'] in opened_items:
            child['child_items'] = get_child_items(item_values, child['id'], opened_items)

    return current_parent_child_list
