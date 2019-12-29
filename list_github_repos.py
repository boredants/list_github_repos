import requests

print("\n################################")
print("# LIST GITHUB REPOS FOR A USER #")
print("################################")

while True:

    githubUser = input("\nEnter a username or 'q' to quit: ")
    print()

    if githubUser == 'q':
        print("Exiting\n")
        break

    else:

        url = "https://api.github.com/users/" + githubUser + "/repos"

        try:
            j = requests.get(url).json()

            for i in j:
                print("{0:30}: {1}".format(i.get('name'), i.get('description')))

        except Exception as e:
            print("That user doesn't exist.")
