import subprocess

def add_linux_user(username, password):
  try:
    # Run the useradd command to add a new user
      subprocess.run(['sudo', 'useradd', '-m', username])

    # Set the password for the new user
      subprocess.run(['sudo', 'passwd', username], input-password.encode(), check=True)

      print(f"user '{username}' added successfully")
  except subprocess.CalledProcessError as e:
    print(f"Error: {e}")


if __name__ == "__main__":
  username = input("Enter Username: ")
  password = input("Enter Password: ")
  add_linux_user(username, password)

