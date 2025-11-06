import json


def load_grants(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_grants(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def add_grant(grants, name, deadline, amount):
    if name not in grants:
        grants[name] = {"deadline": deadline, "amount": amount}
    return grants


def update_grant(grants, name, new_details):
    if name not in grants:
        return grants

    if "new_name" in new_details:
        new_name = new_details["new_name"]

        if new_name in grants and new_name != name:
            print(f"Помилка: Грант з назвою {new_name} вже існує.")
            return grants

        grant_data = grants.pop(name)

        other_updates = {k: v for k, v in new_details.items() if k != "new_name"}
        grant_data.update(other_updates)

        grants[new_name] = grant_data

    else:
        grants[name].update(new_details)

    return grants


def delete_grant(grants, name):
    if name in grants:
        del grants[name]
    return grants


def format_grants_for_output(grants):
    output_lines = ["Список грантів:"]

    if not grants:
        output_lines.append("Список грантів порожній.")
        return "\n".join(output_lines)

    for name, details in grants.items():
        line = f"- {name}: Дедлайн: {details['deadline']}, Сума: {details['amount']} UAH"
        output_lines.append(line)

    return "\n".join(output_lines)