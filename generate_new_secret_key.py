from django.core.management.utils import get_random_secret_key
import os

ENV_FILE = ".env"


def update_env_file(secret_key):
    lines = []
    key_written = False

    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r") as f:
            for line in f:
                if line.startswith("DJANGO_SECRET_KEY="):
                    lines.append(f"DJANGO_SECRET_KEY={secret_key}\n")
                    key_written = True
                else:
                    lines.append(line)

    if not key_written:
        lines.append(f"DJANGO_SECRET_KEY={secret_key}\n")

    with open(ENV_FILE, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    secret = get_random_secret_key()
    update_env_file(secret)
    print(f"✅ New DJANGO_SECRET_KEY added to {ENV_FILE}")
