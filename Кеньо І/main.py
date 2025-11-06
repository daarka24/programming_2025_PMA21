import grants as gm

GRANTS_FILE = "grants_data.json"
OUTPUT_FILE = "output.txt"

initial_grants = {
    "EcoStart": {"deadline": "2025-12-01", "amount": 50000},
    "TechInnovate": {"deadline": "2025-11-15", "amount": 150000},
    "ArtFuture": {"deadline": "2026-01-10", "amount": 75000}
}

gm.save_grants(GRANTS_FILE, initial_grants)

current_grants = gm.load_grants(GRANTS_FILE)

print(gm.format_grants_for_output(current_grants))

current_grants = gm.add_grant(current_grants, "Science Leap", "2026-02-01", 200000)

current_grants = gm.update_grant(current_grants, "EcoStart", {"amount": 65000})

current_grants = gm.update_grant(current_grants, "TechInnovate", {"deadline": "2025-11-30"})

current_grants = gm.update_grant(current_grants, "ArtFuture", {"new_name": "Modern Art Grant"})

current_grants = gm.update_grant(
    current_grants,
    "Science Leap",
    {"amount": 150000, "deadline": "2026-02-15"}
)

current_grants = gm.delete_grant(current_grants, "Modern Art Grant")

gm.save_grants(GRANTS_FILE, current_grants)

final_output_str = gm.format_grants_for_output(current_grants)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(final_output_str)


print(final_output_str)