from src.PheQTK.helpers.variant_validation import parse_variants


raw_input = input("Enter variant id(s): '20-13093478-G-A, 20-13091168-C-T':\n")

variants = parse_variants(raw_input)

for variant in variants:
  print(f"The following variants have been saved: {variant}.")

user_approval = input("Are you ready to proceed? (y/n):")
print(user_approval)