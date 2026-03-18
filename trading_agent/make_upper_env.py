with open(".env", "r") as f:
    env_vars = f.readlines()

with open(".env2", "w") as f:
    for var in env_vars :
        key,value = var.split('=')
        f.write(f"{key.upper()}={value}")
